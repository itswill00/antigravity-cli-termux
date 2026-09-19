#!/usr/bin/env python3
# ponytail: stdlib only, one file web UI for agy. No deps.
import http.server, json, os, pathlib, mimetypes, urllib.parse, time
import subprocess, base64, tempfile, shutil, threading, re, sys, hashlib

ROOT = pathlib.Path(__file__).parent.parent
BIN_DIR = pathlib.Path(__file__).parent
DATA_DIR = pathlib.Path(os.environ.get("AGY_WEB_DATA", str(pathlib.Path.home() / ".agy" / "web")))
DATA_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_DIR = pathlib.Path(tempfile.gettempdir()) / "agy-web-uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

AGY_BIN = shutil.which("agy") or str(BIN_DIR / "agy")

def agy_models():
    try:
        p = subprocess.run([AGY_BIN, "models"], capture_output=True, text=True, timeout=10)
        out = p.stdout.strip() + "\n" + p.stderr.strip()
        models = []
        for line in out.splitlines():
            line=line.strip()
            if not line or line.startswith("Fetching"): continue
            parts = line.split("\t") if "\t" in line else line.split("  ")
            mid = parts[0].strip()
            if mid and not mid.startswith("-") and " " not in mid or "-" in mid or "/" in mid or "." in mid:
                if mid not in ("Available","Usage"):
                    models.append({"id": mid, "label": parts[-1].strip() if len(parts)>1 else mid})
        if not models:
            models = [{"id":"gemini-3.8-flash-medium","label":"Gemini 3.8 Flash (Medium)"}]
        return models
    except Exception as e:
        return [{"id":"gemini-3.8-flash-medium","label":"Gemini 3.8 Flash (Medium)"}]

def model_has_effort(mid: str) -> bool:
    low = mid.lower()
    return ("-high" in low or "-low" in low or "-medium" in low)

def resolve_model_effort(model: str, effort: str):
    if model and model_has_effort(model):
        return model, ""
    if effort not in ("low","medium","high"):
        return model, ""
    return model, effort

def _model_group(model_id: str) -> str:
    low = (model_id or "").lower()
    # agy: gemini-* → Gemini Models, else Claude/GPT → Claude and GPT models
    if low.startswith("gemini"):
        return "gemini"
    if low.startswith("claude") or low.startswith("gpt-"):
        return "3p"
    return "gemini"  # default

def agy_quota():
    try:
        p = subprocess.run([AGY_BIN, "--output-format", "json", "-p", "/usage"], capture_output=True, text=True, timeout=10)
        out = p.stdout.strip()
        if out.startswith("{"):
            j = json.loads(out)
            cmd = j.get("command", {}).get("data", {})
            groups = cmd.get("groups", [])
            res=[]
            for g in groups:
                gid = g.get("name","")
                # normalize group key: "Gemini Models" → gemini, "Claude and GPT models" → 3p
                low = gid.lower()
                if "gemini" in low:
                    key = "gemini"
                elif "claude" in low or "gpt" in low or "3p" in low:
                    key = "3p"
                else:
                    key = gid
                buckets=[]
                for b in g.get("buckets", []):
                    rem = b.get("remaining_fraction", 1.0)
                    try: rem = float(rem)
                    except: rem=1.0
                    used = 1.0 - rem
                    bid = b.get("id","") or b.get("name","")
                    win = b.get("window","") or ("5h" if "5" in bid or "5h" in b.get("name","").lower() else "weekly" if "weekly" in bid.lower() or "weekly" in b.get("name","").lower() else "")
                    buckets.append({"id": bid, "name": b.get("name",""), "window": win, "used_pct": int(round(used*100)), "avail_pct": int(round(rem*100)), "remaining": rem, "reset": b.get("reset_time","")})
                res.append({"key": key, "name": gid, "buckets": buckets})
            return res
        return []
    except Exception:
        return []

def agy_commands():
    try:
        p = subprocess.run([AGY_BIN, "--output-format", "json", "-p", "/help"], capture_output=True, text=True, timeout=10)
        out = p.stdout.strip()
        if out.startswith("{"):
            j = json.loads(out)
            cmds = j.get("command", {}).get("data", {}).get("commands", [])
            return [{"name": c.get("name",""), "description": c.get("description","")} for c in cmds]
        return []
    except Exception:
        return []

def agy_version():
    try:
        pp = subprocess.run([AGY_BIN, "--version"], capture_output=True, text=True, timeout=5)
        v = (pp.stdout.strip() + "\n" + pp.stderr.strip()).strip().splitlines()[0].strip() if (pp.stdout.strip() or pp.stderr.strip()) else ""
        if not v or v.startswith("Usage"):
            return ""
        return v.lstrip("v").strip()
    except Exception:
        return ""

def agy_sessions(limit=30):
    import sqlite3
    db = pathlib.Path.home() / ".gemini" / "antigravity-cli" / "conversation_summaries.db"
    if not db.exists():
        return []
    try:
        con = sqlite3.connect(str(db))
        cur = con.cursor()
        cur.execute("select conversation_id, title, preview, step_count, last_modified_time, workspace_uris, project_id from conversation_summaries order by last_modified_time desc limit ?", (limit,))
        rows=[]
        for cid, title, preview, sc, lm, ws, pid in cur.fetchall():
            # compact workspace
            ws_short=""
            if ws:
                try:
                    ws_short = ws.replace("file:///data/data/com.termux/files/home", "~")
                except:
                    ws_short = ws
            rows.append({"id": cid, "title": title or preview or cid[:8], "preview": preview or title or "", "steps": sc, "updated": str(lm), "workspace": ws_short[:80], "project": pid})
        con.close()
        return rows
    except Exception:
        return []

def agy_session_messages(cid, limit=80):
    import sqlite3, re
    db = pathlib.Path.home() / ".gemini" / "antigravity-cli" / "conversations" / f"{cid}.db"
    if not db.exists():
        return None
    def extract(payload):
        if not payload:
            return None
        strs = re.findall(rb'[\x20-\x7E]{4,}', payload)
        cands=[]
        uuid_pat = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
        for s in strs:
            txt=s.decode(errors='ignore')
            if len(txt)<6: continue
            # skip skill mention noise
            if not txt or len(txt)<6: continue
            low=txt.lower()
            if txt.lstrip().startswith('?') and '/.gemini/' in txt: continue
            if '/.gemini/antigravity-cli/' in txt or 'antigravity-cli/brain' in txt or 'antigravity-cli/skills' in txt: continue
            if txt.startswith('/data/') or txt.startswith('file://') or txt.startswith('/proc/'): continue
            if txt.startswith('//data/'): continue
            if txt.strip().startswith('//data/'): continue
            # skip base64-like hash (no spaces, no vowels, >20 chars)
            if ' ' not in txt and len(txt)>20 and not any(c in 'aeiou' for c in low): continue
            if '"AbsolutePath"' in txt or '"CommandLine"' in txt or '"AllowMultiple"' in txt: continue
            if 'sessionID' in txt or txt.count('$')>0: continue
            if uuid_pat.search(txt): continue
            if txt.count('"')>4 and ':' in txt: continue
            if not any(c.isalpha() for c in txt): continue
            # skip hashed blob names
            if re.match(r'^[A-Za-z0-9+/=]{30,}$', txt) and txt.count(' ')==0: continue
            # natural language heuristic
            if ' ' in txt:
                # at least some vowels
                lower=txt.lower()
                vowels=sum(c in 'aeiou' for c in lower)
                if len(txt)>20 and vowels < len(txt)*0.12: continue
            else:
                if len(txt)<10: continue
            cands.append(txt)
        if not cands: return None
        def score(s):
            return len(s) + s.count(' ')*6 - s.count('"')*2 - s.count('{')*3 - s.count(':')*1
        best=max(cands, key=score)
        if '"//data' in best:
            best=best.split('"//data')[0]
        return best.strip().strip('"')[:4000]
    try:
        con=sqlite3.connect(str(db))
        cur=con.cursor()
        cur.execute("select step_type, step_payload, metadata from steps order by idx")
        msgs=[]
        for stype, payload, meta in cur.fetchall():
            if stype not in (14,15):
                continue
            role='user' if stype==14 else 'assistant'
            txt=extract(payload)
            if not txt:
                txt=extract(meta)
            if not txt:
                continue
            if len(txt)<3: continue
            # role-aware noise filter
            low=txt.lower()
            if txt.lstrip().startswith('?') or txt.lstrip().startswith('#'):
                if '.gemini' in txt or 'timeout' in low or 'skill' in low:
                    continue
                # keep short user prompt starting with ? only if no path? already filtered above, but allow '??'
                if len(txt)<6: continue
            # assistant must be natural language
            if role=='assistant':
                if ' ' not in txt:
                    continue
                if len(txt.split())<2 and len(txt)<30:
                    continue
                # base64-like single token
                import re as _re
                if _re.match(r'^[A-Za-z0-9_\-]{16,}$', txt.strip()):
                    continue
            # user single-word prompts allowed but must be alphabetic word 2-20
            if role=='user' and ' ' not in txt:
                if not (2 <= len(txt) <= 30 and txt.replace('-','').replace('_','').isalpha()):
                    # allow short like 'haloo' but skip hash IDs
                    if not txt.isalpha():
                        continue
            msgs.append({"role": role, "text": txt, "type": stype})
            if len(msgs)>=limit:
                pass
        con.close()
        # keep last limit messages (recent)
        if len(msgs)>limit:
            msgs=msgs[-limit:]
        return msgs
    except Exception:
        return []

