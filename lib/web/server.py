import http.server, json, os, pathlib, mimetypes, urllib.parse, time
import subprocess, base64, tempfile, shutil, threading, re, sys, hashlib, signal

from .api import agy_models, agy_quota, agy_commands, agy_version, agy_standalone_version, agy_sessions, agy_session_messages, AGY_BIN, UPLOAD_DIR, resolve_model_effort
from .ui import HTML

_rate = {"lock": threading.Lock(), "tokens": {}}

def _check_rate(ip: str) -> bool:
    now = time.time()
    with _rate["lock"]:
        rec = _rate["tokens"].get(ip)
        if not rec or now - rec["t"] > 60:
            _rate["tokens"][ip] = {"t": now, "n": 1}
            return True
        if rec["n"] >= 30:
            return False
        rec["n"] += 1
        return True


def _cleanup_uploads():
    try:
        now = time.time()
        for p in UPLOAD_DIR.glob("agy-*"):
            try:
                if now - p.stat().st_mtime > 3600:
                    p.unlink()
            except Exception:
                pass
    except Exception:
        pass


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args): pass

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except (BrokenPipeError, ConnectionResetError, OSError):
            try: self.close_connection = True
            except Exception: pass

    def end_headers(self):
        self.send_header("Cache-Control","no-store")
        self.send_header("X-Content-Type-Options","nosniff")
        super().end_headers()

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        try:
            self.send_response(code); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError, OSError): pass

    def _html(self, html: bytes):
        try:
            self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Length",str(len(html))); self.end_headers(); self.wfile.write(html)
        except (BrokenPipeError, ConnectionResetError, OSError): pass

    def do_GET(self):
        p = urllib.parse.urlparse(self.path).path
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if p in ("/","/index.html"):
            self._html(HTML.encode()); return
        if p == "/api/models":
            self._json({"models": agy_models()}); return
        if p == "/api/health":
            ok = shutil.which("agy") is not None
            ver = agy_version()
            sver = agy_standalone_version()
            self._json({"ok": ok, "agy": AGY_BIN, "version": ver, "standalone_version": sver}); return
        if p == "/api/quota":
            self._json({"groups": agy_quota()}); return
        if p == "/api/commands":
            self._json({"commands": agy_commands()}); return
        if p == "/api/sessions":
            limit = 30
            try: limit = min(100, max(1, int((q.get("limit", ["30"])[0]))))
            except Exception: pass
            self._json({"sessions": agy_sessions(limit=limit)}); return
        if p.startswith("/api/session/"):
            parts = p.split("/")
            if len(parts) >= 4 and parts[3]:
                cid = urllib.parse.unquote(parts[3])
                limit = 80
                try: limit = min(200, max(1, int((q.get("limit", ["80"])[0]))))
                except Exception: pass
                msgs = agy_session_messages(cid, limit=limit)
                if msgs is None:
                    self.send_error(404,"session not found"); return
                self._json({"id": cid, "messages": msgs}); return
            self.send_error(404,"not found"); return
        if p == "/api/export":
            cid = (q.get("id", [""])[0] or "").strip()
            if not cid:
                self.send_error(400,"missing id"); return
            msgs = agy_session_messages(cid, limit=200)
            if msgs is None:
                self.send_error(404,"session not found"); return
            lines = [f"# Antigravity session {cid}", ""]
            for m in msgs:
                role = "You" if m["role"] == "user" else "Antigravity"
                lines.append(f"## {role}")
                lines.append(m["text"])
                lines.append("")
            body = "\n".join(lines).encode()
            try:
                self.send_response(200); self.send_header("Content-Type","text/markdown; charset=utf-8"); self.send_header("Content-Disposition", f'attachment; filename="agy-{cid[:8]}.md"'); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError, OSError): pass
            return
        self.send_error(404,"not found")

    def do_POST(self):
        client_ip = self.client_address[0] if self.client_address else "0.0.0.0"
        if not _check_rate(client_ip):
            self.send_error(429,"too many requests"); return
        p = urllib.parse.urlparse(self.path).path
        if p == "/api/bash":
            length = int(self.headers.get("Content-Length","0"))
            if length > 4096: self.send_error(413,"too large"); return
            raw = self.rfile.read(length) if length else b"{}"
            try: data = json.loads(raw)
            except Exception as e: self.send_error(400,f"bad json {e}"); return
            cmd = (data.get("cmd") or "").strip()
            if not cmd: self._json({"error":"empty command"}, 400); return
            if len(cmd) > 2000: self._json({"error":"command too long"}, 400); return
            try:
                proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
                out = (proc.stdout or "") + (proc.stderr or "")
                if not out.strip(): out = f"(exit {proc.returncode})"
                self._json({"output": out[:12000], "code": proc.returncode})
            except subprocess.TimeoutExpired:
                self._json({"error":"timeout (15s)"}, 500)
            except Exception as e:
                self._json({"error": str(e)}, 500)
            return
        if p not in ("/api/chat","/api/chat_stream"):
            self.send_error(404,"not found"); return
        is_stream = (p == "/api/chat_stream")
        length = int(self.headers.get("Content-Length","0"))
        if length > 12*1024*1024:
            self.send_error(413,"too large"); return
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw)
        except Exception as e:
            self.send_error(400,f"bad json {e}"); return
        prompt = (data.get("prompt") or "").strip()
        model = (data.get("model") or "").strip()
        effort = (data.get("effort") or "").strip()
        conversation_id = (data.get("conversation_id") or "").strip()
        if conversation_id and (".." in conversation_id or "/" in conversation_id or "\\" in conversation_id):
            self.send_error(400,"bad conversation_id"); return
        image = data.get("image")
        if not prompt and not image:
            self.send_error(400,"empty prompt"); return
        img_path = None
        if image and isinstance(image, dict) and image.get("data"):
            try:
                b64 = image["data"]
                if "," in b64 and b64.startswith("data:"):
                    b64 = b64.split(",",1)[1]
                b64 = re.sub(r"\s+", "", b64)
                blob = base64.b64decode(b64, validate=True)
                if len(blob) > 10*1024*1024:
                    self._json({"error":"image too large (10MB)"}, 400); return
                if len(blob) < 16:
                    self._json({"error":"image too small"}, 400); return
                mime = image.get("mime") or "image/jpeg"
                ext = {"image/jpeg":".jpg","image/png":".png","image/webp":".webp","image/gif":".gif"}.get(mime, ".jpg")
                if blob[:2]==b"\xff\xd8": ext=".jpg"
                elif blob[:8]==b"\x89PNG\r\n\x1a\n": ext=".png"
                elif blob[:4]==b"RIFF" and b"WEBP" in blob[:16]: ext=".webp"
                elif blob[:6] in (b"GIF87a", b"GIF89a"): ext=".gif"
                else:
                    self._json({"error":"unsupported image format (jpg/png/webp/gif only)"}, 400); return
                fname = f"agy-{int(time.time()*1000)}-{hashlib.sha1(blob[:1024]).hexdigest()[:6]}{ext}"
                img_path = UPLOAD_DIR / fname
                img_path.write_bytes(blob)
                if prompt:
                    prompt = f"@{img_path} {prompt}"
                else:
                    prompt = f"@{img_path} describe this image"
            except Exception as e:
                self._json({"error":f"bad image: {e}"}, 400); return
        if not prompt:
            prompt = "hello"
        if len(prompt) > 120000:
            self._json({"error":"prompt too long (120k chars max)"}, 400); return
        model, effort = resolve_model_effort(model, effort)
        _cleanup_uploads()
        if is_stream:
            args = [AGY_BIN, "--output-format", "stream-json"]
            if conversation_id:
                args += ["--conversation", conversation_id]
            if model:
                args += ["--model", model]
            if effort:
                args += ["--effort", effort]
            args += ["-p", prompt]
            env = os.environ.copy()
            env["AGY_UPDATE_DEBUG"] = "0"
            try:
                self.send_response(200)
                self.send_header("Content-Type","application/x-ndjson; charset=utf-8")
                self.send_header("Cache-Control","no-store")
                self.send_header("X-Content-Type-Options","nosniff")
                self.send_header("Connection","close")
                self.end_headers()
                proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, env=env, start_new_session=True)
                try:
                    for line in proc.stdout:
                        if not line.strip():
                            continue
                        try:
                            j = json.loads(line)
                        except Exception:
                            continue
                        ev = j.get("event")
                        out = None
                        if ev == "step_update":
                            su = j.get("step_update",{})
                            tname = su.get("tool_name")
                            if tname and su.get("state") in ("ACTIVE","DONE"):
                                info = su.get("tool_info") or {}
                                params = (info.get("parameters") or {})
                                summary = ""
                                if params.get("CommandLine"):
                                    summary = params["CommandLine"][:120]
                                elif params.get("AbsolutePath"):
                                    summary = params["AbsolutePath"].split("/")[-1][:80]
                                elif info.get("name"):
                                    summary = info["name"]
                                out = json.dumps({"t":"tool","name": tname, "summary": summary, "state": su.get("state")}, ensure_ascii=False) + "\n"
                                try:
                                    self.wfile.write(out.encode()); self.wfile.flush()
                                except (BrokenPipeError, ConnectionResetError, OSError):
                                    break
                                if su.get("state")=="DONE" and info.get("output"):
                                    out2 = json.dumps({"t":"tool_out","name": tname, "output": str(info["output"])[:600]}, ensure_ascii=False) + "\n"
                                    try:
                                        self.wfile.write(out2.encode()); self.wfile.flush()
                                    except (BrokenPipeError, ConnectionResetError, OSError):
                                        break
                                continue
                            delta = su.get("text_delta")
                            if delta:
                                out = json.dumps({"t":"delta","d":delta}, ensure_ascii=False) + "\n"
                        elif ev == "command_result":
                            out = json.dumps({"t":"cmd","cmd": j.get("command",{})}, ensure_ascii=False) + "\n"
                        elif ev == "result":
                            res = j.get("result",{})
                            out = json.dumps({"t":"done","response": res.get("response",""), "usage": res.get("usage"), "duration": res.get("duration_seconds"), "status": res.get("status"), "error": res.get("error"), "conversation_id": res.get("conversation_id") or j.get("conversation_id")}, ensure_ascii=False) + "\n"
                            try:
                                self.wfile.write(out.encode()); self.wfile.flush()
                            except (BrokenPipeError, ConnectionResetError, OSError):
                                break
                            break
                        elif ev == "init":
                            continue
                        if out:
                            try:
                                self.wfile.write(out.encode()); self.wfile.flush()
                            except (BrokenPipeError, ConnectionResetError, OSError):
                                break
                    try:
                        proc.wait(timeout=2)
                    except Exception:
                        pass
                except (BrokenPipeError, ConnectionResetError, OSError):
                    pass
                finally:
                    try:
                        if proc.poll() is None:
                            try: os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
                            except Exception: proc.terminate()
                            try: proc.wait(timeout=1)
                            except Exception:
                                try: os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
                                except Exception: proc.kill()
                    except Exception:
                        pass
                    try: proc.stdout.close()
                    except Exception: pass
                    try: proc.stderr.close()
                    except Exception: pass
            except Exception as e:
                try:
                    err = json.dumps({"t":"error","error": str(e)}, ensure_ascii=False) + "\n"
                    self.wfile.write(err.encode())
                except Exception:
                    pass
            return
        args = [AGY_BIN, "--output-format", "json"]
        if conversation_id:
            args += ["--conversation", conversation_id]
        if model:
            args += ["--model", model]
        if effort:
            args += ["--effort", effort]
        args += ["-p", prompt]
        try:
            env = os.environ.copy()
            env["AGY_UPDATE_DEBUG"] = "0"
            proc = subprocess.run(args, capture_output=True, text=True, timeout=180, env=env)
            out = (proc.stdout or "").strip()
            err = (proc.stderr or "").strip()
            usage = None
            duration = None
            parsed = None
            resp_text = out
            try:
                if out.startswith("{"):
                    parsed = json.loads(out)
                    resp_text = (parsed.get("response") or "").strip() or out
                    usage = parsed.get("usage")
                    duration = parsed.get("duration_seconds")
                    if parsed.get("status") == "ERROR":
                        self._json({"error": parsed.get("error") or err or "agy error", "usage": usage, "duration": duration}); return
            except Exception:
                pass
            if proc.returncode != 0 and not resp_text:
                self._json({"error": err[:2000] or f"agy exit {proc.returncode}", "usage": usage, "duration": duration}); return
            if "AGY_ERROR" in err and not resp_text:
                self._json({"error": err[:3000], "usage": usage, "duration": duration}); return
            self._json({"response": resp_text or err or "(empty)", "usage": usage, "duration": duration, "model": model, "effort": effort, "conversation_id": parsed.get("conversation_id") if parsed else None})
        except subprocess.TimeoutExpired:
            self._json({"error":"agy timeout (180s) — prompt too long or model busy"})
        except Exception as e:
            import traceback; traceback.print_exc()
            self._json({"error": str(e)}, 500)

def main():
    import argparse, webbrowser, socket
    ap = argparse.ArgumentParser(description="agy web — browser UI for agy")
    ap.add_argument("--port", type=int, default=8765, help="port (default 8765)")
    ap.add_argument("--host", default="127.0.0.1", help="host (default 127.0.0.1)")
    ap.add_argument("--open", action="store_true", help="open browser")
    ap.add_argument("--no-open", action="store_true", help="do not auto-open browser")
    ap.add_argument("--allow-lan", action="store_true", help="bind 0.0.0.0")
    args = ap.parse_args()
    if args.allow_lan:
        args.host = "0.0.0.0"
    host, port = args.host, args.port
    srv = http.server.ThreadingHTTPServer((host, port), Handler)
    actual = srv.server_address[1]
    url = f"http://{host if host!='0.0.0.0' else '127.0.0.1'}:{actual}/"
    print(f"[agy web] serving at {url}  (agy: {AGY_BIN})")
    print(f"[agy web] image upload: {UPLOAD_DIR}  (max 10MB, jpg/png/webp)")
    should_open = args.open or (not args.no_open and os.environ.get("TERMUX_VERSION"))
    if should_open:
        try:
            if shutil.which("termux-open-url"):
                subprocess.Popen(["termux-open-url", url])
            else:
                webbrowser.open(url)
        except Exception:
            pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
