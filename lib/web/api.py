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

_models_cache = {"ts": 0, "data": None}

def agy_models():
    global _models_cache
    now = time.time()
    if _models_cache["data"] and now - _models_cache["ts"] < 30:
        return _models_cache["data"]
    try:
        p = subprocess.run([AGY_BIN, "models"], capture_output=True, text=True, timeout=10)
        out = p.stdout.strip() + "\n" + p.stderr.strip()
        models = []
        for line in out.splitlines():
            line = line.strip()
            if not line or line.startswith("Fetching"):
                continue
            if "\t" in line:
                parts = line.split("\t")
            else:
                parts = re.split(r"\s{2,}", line, maxsplit=1)
            mid = parts[0].strip()
            label = parts[1].strip() if len(parts) > 1 else mid
            if not mid or mid in ("Available", "Usage"):
                continue
            if " " in mid and "/" not in mid and "-" not in mid:
                continue
            if not re.match(r"^[a-z0-9._/-]+$", mid.lower()):
                continue
            models.append({"id": mid, "label": label})
        if not models:
            models = [{"id": "gemini-3.8-flash-medium", "label": "Gemini 3.8 Flash (Medium)"}]
        _models_cache = {"ts": now, "data": models}
        return models
    except Exception:
        if _models_cache["data"]:
            return _models_cache["data"]
        return [{"id": "gemini-3.8-flash-medium", "label": "Gemini 3.8 Flash (Medium)"}]

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

_quota_cache = {"ts": 0, "data": None}

def agy_quota():
    global _quota_cache
    now = time.time()
    if _quota_cache["data"] is not None and now - _quota_cache["ts"] < 15:
        return _quota_cache["data"]
    try:
        p = subprocess.run([AGY_BIN, "--output-format", "json", "-p", "/usage"], capture_output=True, text=True, timeout=10)
        out = p.stdout.strip()
        if not out.startswith("{"):
            return _quota_cache["data"] if _quota_cache["data"] is not None else []
        j = json.loads(out)
        cmd = j.get("command", {}).get("data", {})
        groups = cmd.get("groups", [])
        res = []
        for g in groups:
            gid = g.get("name", "")
            low = gid.lower()
            if "gemini" in low:
                key = "gemini"
            elif "claude" in low or "gpt" in low or "3p" in low:
                key = "3p"
            else:
                key = gid
            buckets = []
            for b in g.get("buckets", []):
                rem = b.get("remaining_fraction", 1.0)
                try:
                    rem = float(rem)
                except Exception:
                    rem = 1.0
                rem = max(0.0, min(1.0, rem))
                used = 1.0 - rem
                bid = b.get("id", "") or b.get("name", "")
                bname = str(b.get("name", "")).lower()
                if b.get("window"):
                    win = b["window"]
                elif "5h" in bid or "5h" in bname:
                    win = "5h"
                elif "weekly" in bid.lower() or "weekly" in bname:
                    win = "weekly"
                else:
                    win = b.get("id", "")[:16] or "window"
                buckets.append({"id": bid, "name": b.get("name", ""), "window": win, "used_pct": int(round(used * 100)), "avail_pct": int(round(rem * 100)), "remaining": rem, "reset": b.get("reset_time", "")})
            res.append({"key": key, "name": gid, "buckets": buckets})
        _quota_cache = {"ts": now, "data": res}
        return res
    except Exception:
        if _quota_cache["data"] is not None:
            return _quota_cache["data"]
        return []

_cmds_cache = {"ts": 0, "data": None}

def agy_commands():
    global _cmds_cache
    now = time.time()
    if _cmds_cache["data"] is not None and now - _cmds_cache["ts"] < 60:
        return _cmds_cache["data"]
    try:
        p = subprocess.run([AGY_BIN, "--output-format", "json", "-p", "/help"], capture_output=True, text=True, timeout=10)
        out = p.stdout.strip()
        if out.startswith("{"):
            j = json.loads(out)
            raw = j.get("command", {}).get("data", {}).get("commands", [])
            seen = set()
            cmds = []
            for c in raw:
                name = (c.get("name") or "").strip()
                if not name or name in seen:
                    continue
                seen.add(name)
                desc = c.get("description") or ""
                cmds.append({"name": name, "description": desc, "aliases": c.get("aliases") or []})
            _cmds_cache = {"ts": now, "data": cmds}
            return cmds
        return _cmds_cache["data"] if _cmds_cache["data"] is not None else []
    except Exception:
        return _cmds_cache["data"] if _cmds_cache["data"] is not None else []

def agy_standalone_version():
    try:
        with open(pathlib.Path(__file__).parent.parent / "agy_helper.c", "r") as f:
            for line in f:
                if "AGY_TERMUX_VERSION" in line and "#define" in line:
                    import re as _re
                    m = _re.search(r'"([^"]+)"', line)
                    if m:
                        return m.group(1).lstrip("v").strip()
    except Exception:
        pass
    try:
        for cand in [pathlib.Path(AGY_BIN).parent / "agy", pathlib.Path(__file__).parent.parent / "bin" / "agy"]:
            try:
                s = cand.read_bytes()
                import re as _re
                m = _re.search(rb'(\d+\.\d+\.\d+)', s)
                if m:
                    return m.group(1).decode()
            except Exception:
                continue
    except Exception:
        pass
    return ""

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
    if limit < 1:
        limit = 30
    limit = min(limit, 100)
    try:
        con = sqlite3.connect(str(db))
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select conversation_id, title, preview, step_count, last_modified_time, workspace_uris, project_id from conversation_summaries order by last_modified_time desc limit ?", (limit,))
        rows = []
        for r in cur.fetchall():
            cid, title, preview, sc, lm, ws, pid = r[0], r[1], r[2], r[3], r[4], r[5], r[6]
            ws_short = ""
            if ws:
                try:
                    ws_short = str(ws).replace("file:///data/data/com.termux/files/home", "~")
                except Exception:
                    ws_short = str(ws)[:80]
            rows.append({"id": cid, "title": (title or preview or cid[:8])[:120], "preview": (preview or title or "")[:300], "steps": sc, "updated": str(lm), "workspace": ws_short[:80], "project": pid})
        con.close()
        return rows
    except Exception:
        return []
    finally:
        try:
            con.close()
        except Exception:
            pass


def agy_session_messages(cid, limit=80):
    import sqlite3, re
    if not cid or not re.match(r"^[0-9a-fA-F-]{8,64}$", cid):
        # still allow any non-empty but prevent path traversal
        if ".." in cid or "/" in cid or "\\" in cid:
            return None
    if limit < 1:
        limit = 80
    limit = min(limit, 200)
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
        con.close()
        if len(msgs) > limit:
            msgs = msgs[-limit:]
        return msgs
    except Exception:
        return []
    finally:
        try:
            con.close()
        except Exception:
            pass

