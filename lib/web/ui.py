HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,maximum-scale=1,interactive-widget=resizes-content">
<title>Antigravity Web</title>
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#09090b">
<style>
*,*::before,*::after{box-sizing:border-box}
:root{
  --bg:#09090b;
  --surface:#111114;
  --surface-hover:#18181c;
  --surface-active:#202026;
  --surface-card:#101013;
  --border:#27272a;
  --border-light:#3f3f46;
  --border-focus:#52525b;
  --text:#fafafa;
  --text-sub:#a1a1aa;
  --text-muted:#71717a;
  --accent:#38bdf8;
  --accent-blue:#4285f4;
  --success:#34a853;
  --warning:#fbbc04;
  --danger:#ea4335;
  --radius-sm:6px;
  --radius-md:10px;
  --radius-lg:14px;
  --radius-xl:18px;
  --hdr-h:48px;
  --composer-h:120px;
}
html,body{height:100%}
body{
  margin:0;
  font:14px/1.6 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  color:var(--text);
  background:var(--bg);
  -webkit-font-smoothing:antialiased;
  padding-top:var(--hdr-h);
  overscroll-behavior-y:contain;
  min-height:100dvh;
}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
button,select,textarea,input{font:inherit;color:inherit;transition:background .15s ease,border-color .15s ease,color .15s ease,box-shadow .15s ease,transform .1s cubic-bezier(0.16,1,0.3,1)}
button:active,.hdr-btn:active,.chip:active,.action-btn:active,.send-btn:active,.tool-action-btn:active{transform:scale(0.96)}
*:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

::selection{background:rgba(56,189,248,0.28);color:#fff}
::-webkit-scrollbar{width:6px;height:6px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#27272a;border-radius:999px}
::-webkit-scrollbar-thumb:hover{background:#3f3f46}

.logo-ans{line-height:0;flex:0 0 auto;display:flex;align-items:center}
.logo-ans pre{margin:0;font:3.8px/3.8px ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;white-space:pre;display:block;letter-spacing:0}

header{
  position:fixed;
  top:0;left:0;right:0;
  height:var(--hdr-h);
  z-index:25;
  background:rgba(9,9,11,0.9);
  backdrop-filter:blur(16px);
  -webkit-backdrop-filter:blur(16px);
  border-bottom:1px solid var(--border);
  display:flex;
  align-items:center;
}
.hdr-inner{
  width:100%;
  max-width:920px;
  margin:0 auto;
  padding:0 14px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:10px;
}
.hdr-left{display:flex;align-items:center;gap:8px;min-width:0;flex:0 1 auto}
.brand{display:flex;align-items:center;gap:9px;user-select:none;text-decoration:none;color:var(--text);min-width:0}
.brand b{font-size:13.5px;font-weight:700;letter-spacing:-0.2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ver-pill{font-size:9.5px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--text-muted);border:1px solid var(--border);padding:1.5px 6px;border-radius:999px;background:rgba(255,255,255,0.03);white-space:nowrap;flex:0 0 auto}

.hdr-center{display:flex;align-items:center;min-width:0;flex:1 1 auto;justify-content:center}
.pill-group{display:flex;align-items:center;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md);padding:2px 4px;max-width:100%;min-width:0}
.pill-select-wrap{position:relative;display:flex;align-items:center;min-width:0;max-width:100%}
.pill-select-wrap select{
  appearance:none;
  background:transparent;
  border:0;
  color:var(--text);
  font-size:12px;
  font-weight:600;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  padding:4px 22px 4px 8px;
  border-radius:6px;
  cursor:pointer;
  max-width:260px;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
  min-width:0;
}
.pill-select-wrap select:hover{background:var(--surface-hover)}
.pill-select-wrap .chevron{position:absolute;right:6px;pointer-events:none;width:11px;height:11px;color:var(--text-muted)}

.hdr-right{display:flex;align-items:center;gap:6px;flex:0 0 auto}
.hdr-btn{
  background:transparent;
  border:1px solid var(--border);
  color:var(--text-sub);
  padding:5px 9px;
  border-radius:var(--radius-md);
  font-size:11.5px;
  cursor:pointer;
  display:inline-flex;
  align-items:center;
  gap:5px;
  white-space:nowrap;
  transition:all 0.15s ease;
}
.hdr-btn svg{width:13px;height:13px;flex:0 0 13px}
.hdr-btn:hover{background:var(--surface);color:var(--text);border-color:var(--border-light)}
.hdr-btn:active{transform:scale(0.97)}

#chat{
  max-width:920px;
  margin:0 auto;
  padding:14px 14px var(--composer-h);
  min-height:calc(100vh - var(--hdr-h));
}

.empty-state{max-width:620px;margin:28px auto 20px;padding:0 8px;text-align:center}
.empty-logo-box{
  margin:0 auto 16px;
  display:inline-flex;
  padding:14px 18px;
  border-radius:18px;
  background:linear-gradient(180deg, #16161b, #0c0c0f);
  border:1px solid var(--border);
  box-shadow:0 12px 30px rgba(0,0,0,0.4);
}
.empty-logo-box .logo-ans pre{font:7px/7px ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace}
.empty-title{font-size:19px;font-weight:700;letter-spacing:-0.4px;margin:0;color:var(--text)}
.empty-sub{margin:6px 0 20px;color:var(--text-sub);font-size:13px;line-height:1.5}

.quick-resume-card{
  display:inline-flex;
  align-items:center;
  gap:8px;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:999px;
  padding:6px 14px;
  margin-bottom:20px;
  font-size:12px;
  color:var(--text-sub);
  cursor:pointer;
  transition:border-color 0.15s, background 0.15s;
}
.quick-resume-card:hover{border-color:var(--accent);background:var(--surface-hover);color:var(--text)}
.quick-resume-card svg{width:13px;height:13px;color:var(--accent)}
.quick-resume-card b{color:var(--text);font-weight:550;max-width:240px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

.suggestions-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;text-align:left;margin-top:6px}
.chip{
  border:1px solid var(--border);
  background:var(--surface);
  border-radius:var(--radius-lg);
  padding:12px 14px;
  cursor:pointer;
  display:flex;
  align-items:flex-start;
  gap:10px;
  transition:all 0.15s ease;
  width:100%;
}
.chip:hover{border-color:var(--border-light);background:var(--surface-hover);transform:translateY(-1px)}
.chip:active{transform:translateY(0)}
.chip-icon{font-size:16px;line-height:1;flex:0 0 auto;margin-top:2px}
.chip-text{min-width:0;flex:1}
.chip-text b{font-size:12.5px;font-weight:600;display:block;color:var(--text);line-height:1.3}
.chip-text span{font-size:11px;color:var(--text-muted);display:block;margin-top:2px;line-height:1.3}
.shortcuts-bar{display:flex;gap:6px;flex-wrap:wrap;justify-content:center;margin-top:20px}
.sc-tag{
  font-size:10.5px;
  color:var(--text-muted);
  background:rgba(255,255,255,0.02);
  border:1px solid var(--border);
  padding:3px 8px;
  border-radius:999px;
  display:inline-flex;
  align-items:center;
  gap:4px;
}
.sc-tag kbd{
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  background:var(--surface);
  border:1px solid var(--border-light);
  padding:1px 4px;
  border-radius:4px;
  font-size:9.5px;
  color:var(--text-sub);
}

.msg{margin:14px 0;display:flex;gap:10px;min-width:0;animation:msg-in 0.2s cubic-bezier(0.16,1,0.3,1) both}
@keyframes msg-in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.msg .avatar{
  width:28px;
  height:28px;
  border-radius:999px;
  display:grid;
  place-items:center;
  font-size:10.5px;
  font-weight:750;
  flex:0 0 28px;
  margin-top:2px;
  border:1px solid var(--border);
  user-select:none;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
}
.msg.user .avatar{background:#27272a;color:#fafafa}
.msg.assistant .avatar{background:#fafafa;color:#09090b;border-color:#fafafa}
.msg .bubble{
  flex:1;
  min-width:0;
  max-width:100%;
  padding:12px 14px;
  border-radius:var(--radius-lg);
  border:1px solid var(--border);
  word-break:break-word;
  overflow-wrap:anywhere;
  position:relative;
}
.msg.user .bubble{background:var(--surface-hover);color:#f4f4f5;border-color:var(--border)}
.msg.assistant .bubble{background:var(--surface-card);color:var(--text);border-color:var(--border)}
.bubble img{max-width:min(340px, 100%);border-radius:var(--radius-md);border:1px solid var(--border);display:block;margin-bottom:8px}

.bubble .md{white-space:normal;line-height:1.65;font-size:13.5px}
.bubble .md p{margin:6px 0}
.bubble .md p:first-child{margin-top:0}
.bubble .md p:last-child{margin-bottom:0}
.bubble .md h1,.bubble .md h2,.bubble .md h3,.bubble .md h4{
  margin:14px 0 6px;
  font-weight:700;
  letter-spacing:-0.2px;
  line-height:1.3;
  color:var(--text);
}
.bubble .md h1{font-size:17px}
.bubble .md h2{font-size:15px}
.bubble .md h3{font-size:14px}
.bubble .md h4{font-size:13px;color:var(--text-sub)}
.bubble .md ul,.bubble .md ol{margin:6px 0;padding-left:20px}
.bubble .md li{margin:3px 0}
.bubble .md blockquote{
  border-left:3px solid var(--accent);
  padding-left:10px;
  color:var(--text-sub);
  margin:8px 0;
  background:rgba(56,189,248,0.04);
  border-radius:0 6px 6px 0;
  padding-top:2px;
  padding-bottom:2px;
}
.bubble .md table{border-collapse:collapse;width:100%;margin:10px 0;font-size:12.5px;display:block;overflow-x:auto}
.bubble .md th,.bubble .md td{border:1px solid var(--border);padding:7px 10px;text-align:left;white-space:nowrap}
.bubble .md th{background:var(--surface);font-weight:600}
.bubble .md hr{border:0;border-top:1px solid var(--border);margin:12px 0}
.bubble .md pre{
  position:relative;
  background:#070709;
  border:1px solid var(--border);
  padding:12px;
  border-radius:var(--radius-md);
  overflow-x:auto;
  font:12px/1.55 ui-monospace,SFMono-Regular,Menlo,monospace;
  margin:10px 0;
}
.bubble .md code{
  font:12px/1.45 ui-monospace,SFMono-Regular,Menlo,monospace;
  background:#1e1e23;
  padding:2px 5px;
  border-radius:4px;
  border:1px solid var(--border);
}
.bubble .md pre code{background:transparent;border:0;padding:0}
.code-header{
  display:flex;
  justify-content:space-between;
  align-items:center;
  font-size:10.5px;
  color:var(--text-muted);
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  margin-bottom:6px;
  padding-bottom:5px;
  border-bottom:1px solid #1f1f23;
  user-select:none;
}
.copy-code{
  font-size:10px;
  padding:2px 8px;
  border-radius:5px;
  background:var(--surface);
  border:1px solid var(--border);
  color:var(--text-sub);
  cursor:pointer;
  transition:all 0.15s ease;
}
.copy-code:hover{color:var(--text);border-color:var(--border-light)}

.thinking-box{display:flex;flex-direction:column;gap:6px;padding:2px 0}
.thinking-header{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;color:var(--text-sub);font-style:italic}
.pulse-dot{
  width:7px;
  height:7px;
  border-radius:999px;
  background:var(--accent);
  animation:living-glow 1.3s infinite ease-in-out;
}
@keyframes living-glow{
  0%,100%{transform:scale(0.85);opacity:0.35;box-shadow:0 0 0 0 rgba(56,189,248,0)}
  50%{transform:scale(1.18);opacity:1;box-shadow:0 0 10px rgba(56,189,248,0.55)}
}

.tools-stream{display:flex;flex-direction:column;gap:4px;margin-top:4px;padding-left:10px;border-left:2px solid var(--border)}
.tool-pill{
  display:inline-flex;
  align-items:center;
  gap:6px;
  font-size:11px;
  color:var(--text-sub);
  background:var(--surface);
  border:1px solid var(--border);
  padding:2px 8px;
  border-radius:6px;
  max-width:100%;
  animation:tool-in 0.16s cubic-bezier(0.16,1,0.3,1) both;
}
@keyframes tool-in{from{opacity:0;transform:translateX(-5px)}to{opacity:1;transform:translateX(0)}}
.tool-pill .tool-dot{width:6px;height:6px;border-radius:999px;flex:0 0 6px}
.tool-dot.running{background:var(--warning);animation:living-glow 1s infinite}
.tool-dot.done{background:var(--success)}
.tool-pill code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--accent);font-size:10.5px}
.tool-pill .tool-summary{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:320px}
.copy-pop{animation:pop-bounce 0.22s cubic-bezier(0.34,1.56,0.64,1)}
@keyframes pop-bounce{0%{transform:scale(0.8)}50%{transform:scale(1.15)}100%{transform:scale(1)}}

.msg-actions{margin-top:10px;display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.action-btn{
  background:transparent;
  border:1px solid var(--border);
  color:var(--text-muted);
  font-size:11px;
  padding:3px 8px;
  border-radius:6px;
  cursor:pointer;
  display:inline-flex;
  align-items:center;
  gap:4px;
  transition:all 0.15s ease;
}
.action-btn:hover{color:var(--text);border-color:var(--border-light);background:var(--surface)}
.action-btn svg{width:11px;height:11px}
.msg-meta{font-size:10.5px;color:var(--text-muted);display:inline-flex;align-items:center;gap:5px;margin-left:auto}
.msg-meta-tag{
  border:1px solid var(--border);
  padding:1px 6px;
  border-radius:999px;
  background:var(--surface);
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:9.5px;
}
.msg-error{
  color:var(--danger);
  background:rgba(234,67,53,0.08);
  border:1px solid rgba(234,67,53,0.25);
  border-radius:6px;
  padding:6px 10px;
  font-size:12px;
  margin-top:8px;
}

#composer{
  position:fixed;
  bottom:0;left:0;right:0;
  z-index:20;
  background:rgba(9,9,11,0.92);
  backdrop-filter:blur(16px);
  -webkit-backdrop-filter:blur(16px);
  border-top:1px solid var(--border);
  padding-bottom:calc(env(safe-area-inset-bottom) + var(--kb, 0px));
  transition:padding-bottom 0.12s ease;
}
.composer-inner{max-width:920px;margin:0 auto;padding:8px 14px 10px}
#preview{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
#preview:empty{display:none}
.preview-card{display:flex;align-items:center;gap:8px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-md);padding:4px 8px;min-width:0}
.preview-card img{width:38px;height:38px;object-fit:cover;border-radius:6px;border:1px solid var(--border);flex:0 0 38px}
.preview-meta{font-size:11px;color:var(--text-sub);min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:180px}
.preview-card .rm-btn{background:transparent;border:0;color:var(--text-muted);cursor:pointer;padding:2px 4px;font-size:14px;border-radius:4px}
.preview-card .rm-btn:hover{color:var(--danger)}

.composer-box{
  background:var(--surface-card);
  border:1px solid var(--border);
  border-radius:var(--radius-xl);
  padding:8px 10px;
  display:flex;
  flex-direction:column;
  gap:6px;
  position:relative;
  transition:border-color 0.15s, box-shadow 0.15s;
}
.composer-box:focus-within{
  border-color:var(--border-focus);
  box-shadow:0 0 0 1px var(--border-focus), 0 4px 20px rgba(0,0,0,0.3);
}
#prompt{
  width:100%;
  min-height:40px;
  max-height:150px;
  resize:none;
  background:transparent;
  color:var(--text);
  border:0;
  padding:4px 2px;
  font:14px/1.55 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,sans-serif;
  outline:none;
}
#prompt::placeholder{color:var(--text-muted)}

.composer-toolbar{display:flex;align-items:center;justify-content:space-between;gap:8px;min-width:0}
.toolbar-left{display:flex;align-items:center;gap:6px;min-width:0;flex:1 1 auto;overflow-x:auto;scrollbar-width:none}
.toolbar-left::-webkit-scrollbar{display:none}
.toolbar-right{display:flex;align-items:center;gap:6px;flex:0 0 auto}

.tool-action-btn{
  height:30px;
  padding:0 10px;
  border-radius:var(--radius-md);
  background:var(--surface);
  border:1px solid var(--border);
  color:var(--text-sub);
  font-size:11.5px;
  cursor:pointer;
  display:inline-flex;
  align-items:center;
  gap:5px;
  white-space:nowrap;
  flex:0 0 auto;
  transition:all 0.15s ease;
}
.tool-action-btn:hover{background:var(--surface-hover);color:var(--text);border-color:var(--border-light)}
.tool-action-btn svg{width:13px;height:13px;flex:0 0 13px}

.quota-pill{
  height:30px;
  padding:0 10px;
  border-radius:999px;
  background:var(--surface);
  border:1px solid var(--border);
  color:var(--text-sub);
  font-size:11px;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  cursor:pointer;
  display:inline-flex;
  align-items:center;
  gap:6px;
  white-space:nowrap;
  flex:0 1 auto;
  overflow:hidden;
  text-overflow:ellipsis;
  max-width:280px;
  transition:all 0.15s ease;
}
.quota-pill:hover{border-color:var(--border-light);color:var(--text)}
.quota-pill .quota-dot{width:6px;height:6px;border-radius:999px;background:var(--success);flex:0 0 6px;transition:background .2s ease}
.quota-pill.exhausted .quota-dot{background:var(--danger)}
.quota-pill.warning .quota-dot{background:var(--warning)}
.quota-pill.refreshing .quota-dot{animation:quota-spin .6s linear infinite}
@keyframes quota-spin{0%{transform:scale(1.25) rotate(0deg)}100%{transform:scale(1.25) rotate(360deg)}}

.char-counter{
  font-size:11px;
  color:var(--text-muted);
  font-variant-numeric:tabular-nums;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  white-space:nowrap;
}
.char-counter:empty{display:none}

.send-btn{
  height:32px;
  min-width:64px;
  padding:0 14px;
  border-radius:var(--radius-md);
  border:1px solid transparent;
  font-size:12px;
  font-weight:650;
  cursor:pointer;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:5px;
  transition:all 0.15s ease;
  user-select:none;
}
.send-btn.primary{background:var(--text);color:var(--bg);border-color:var(--text)}
.send-btn.primary:hover{opacity:0.92}
.send-btn.primary:disabled{opacity:0.4;cursor:not-allowed}
.send-btn.danger{
  background:var(--danger);
  color:#fff;
  border-color:var(--danger);
  animation:stop-pulse 1.8s infinite;
}
@keyframes stop-pulse{0%,100%{box-shadow:0 0 0 0 rgba(234,67,53,0.4)}50%{box-shadow:0 0 0 4px rgba(234,67,53,0)}}

#slashMenu{
  position:absolute;
  bottom:calc(100% + 6px);
  left:0;right:0;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--radius-lg);
  box-shadow:0 10px 30px rgba(0,0,0,0.5);
  max-height:220px;
  overflow-y:auto;
  display:none;
  z-index:30;
}
#slashMenu.on{display:block}
.slash-item{
  padding:8px 12px;
  display:flex;
  align-items:center;
  gap:10px;
  cursor:pointer;
  border-bottom:1px solid rgba(255,255,255,0.03);
}
.slash-item:last-child{border-bottom:0}
.slash-item:hover,.slash-item.active{background:var(--surface-hover)}
.slash-item b{font-size:12px;color:var(--accent);font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.slash-item span{font-size:11.5px;color:var(--text-sub);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

.modal-overlay{
  position:fixed;
  inset:0;
  z-index:50;
  background:rgba(0,0,0,0.7);
  backdrop-filter:blur(10px);
  -webkit-backdrop-filter:blur(10px);
  display:none;
  align-items:center;
  justify-content:center;
  padding:14px;
}
.modal-overlay.on{
  display:flex;
  animation:fade-in 0.18s cubic-bezier(0.16,1,0.3,1);
}
@keyframes fade-in{from{opacity:0}to{opacity:1}}
.modal-card{
  width:100%;
  max-width:540px;
  max-height:82vh;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--radius-xl);
  display:flex;
  flex-direction:column;
  box-shadow:0 24px 50px rgba(0,0,0,0.7);
  overflow:hidden;
  animation:modal-pop 0.2s cubic-bezier(0.16,1,0.3,1);
}
@keyframes modal-pop{from{opacity:0;transform:scale(0.96) translateY(6px)}to{opacity:1;transform:scale(1) translateY(0)}}
.sheet-handle{display:none}
.modal-head{
  padding:12px 16px;
  border-bottom:1px solid var(--border);
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:10px;
}
.modal-head-title{display:flex;align-items:center;gap:8px}
.modal-head h2{margin:0;font-size:14.5px;font-weight:700;letter-spacing:-0.2px}
.session-total-pill{
  font-size:10px;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  color:var(--text-muted);
  border:1px solid var(--border);
  padding:1px 6px;
  border-radius:999px;
  background:var(--surface-hover);
}
.modal-actions{
  display:flex;
  align-items:center;
  gap:6px;
}
.modal-btn-new{
  display:inline-flex;
  align-items:center;
  gap:5px;
  background:var(--surface);
  color:var(--text);
  border:1px solid var(--border);
  padding:0 9px;
  border-radius:var(--radius-sm);
  font-size:11.5px;
  font-weight:600;
  cursor:pointer;
  transition:all 0.14s ease;
  height:28px;
}
.modal-btn-new:hover{
  background:var(--surface-hover);
  border-color:var(--border-light);
  color:var(--text-bright);
}
.modal-btn-new:active{
  transform:scale(0.96);
}
.modal-btn-new svg{
  width:12px;
  height:12px;
  stroke-width:2.2;
}
.modal-close-btn{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  width:28px;
  height:28px;
  border-radius:var(--radius-sm);
  background:transparent;
  border:1px solid transparent;
  color:var(--text-muted);
  cursor:pointer;
  transition:all 0.14s ease;
  padding:0;
}
.modal-close-btn:hover{
  background:var(--surface-hover);
  border-color:var(--border);
  color:var(--text);
}
.modal-close-btn:active{
  transform:scale(0.94);
}
.modal-close-btn svg{
  width:14px;
  height:14px;
  stroke-width:2;
}
.modal-search-wrap{padding:8px 14px;border-bottom:1px solid var(--border);background:var(--bg)}
.modal-search-box{
  display:flex;
  align-items:center;
  gap:8px;
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:var(--radius-md);
  padding:0 10px;
  transition:border-color 0.15s ease, box-shadow 0.15s ease;
}
.modal-search-box:focus-within{
  border-color:var(--accent);
  box-shadow:0 0 0 1px var(--accent);
}
.modal-search-box svg{width:13px;height:13px;color:var(--text-muted);flex:0 0 13px}
.modal-search-input{
  flex:1;
  background:transparent;
  border:0;
  padding:7px 0;
  font-size:12px;
  color:var(--text);
  outline:none;
}
.session-count-badge{
  font-size:10px;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  color:var(--text-muted);
}
.modal-body{padding:8px 10px;overflow-y:auto;display:flex;flex-direction:column;gap:4px;flex:1}
.session-item{
  background:var(--surface-card);
  border:1px solid var(--border);
  border-radius:var(--radius-md);
  padding:8px 10px;
  cursor:pointer;
  display:flex;
  align-items:center;
  gap:9px;
  text-align:left;
  transition:background 0.14s ease, border-color 0.14s ease, transform 0.14s cubic-bezier(0.16,1,0.3,1);
  width:100%;
}
.session-item:hover{
  background:var(--surface-hover);
  border-color:var(--border-light);
  transform:translateX(2px);
}
.session-item:active{transform:scale(0.98)}
.session-item.active{
  border-color:var(--accent);
  background:rgba(56,189,248,0.06);
  box-shadow:inset 2px 0 0 0 var(--accent);
}
.session-item.nav-focused{
  border-color:var(--border-focus);
  background:var(--surface-active);
}
.session-dot{
  width:6px;
  height:6px;
  border-radius:999px;
  background:var(--border-light);
  flex:0 0 6px;
  transition:all 0.15s ease;
}
.session-item.active .session-dot{
  background:var(--success);
  box-shadow:0 0 6px rgba(52,168,83,0.7);
}
.session-main{flex:1;min-width:0}
.session-line-1{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:8px;
  min-width:0;
}
.session-title{
  font-size:12.5px;
  font-weight:600;
  color:var(--text);
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
  min-width:0;
  flex:1 1 auto;
  line-height:1.3;
}
.session-right-meta{
  display:flex;
  align-items:center;
  gap:5px;
  flex:0 0 auto;
  font-size:10px;
  color:var(--text-muted);
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
}
.session-steps{
  border:1px solid var(--border);
  padding:1px 5px;
  border-radius:4px;
  background:var(--surface);
  white-space:nowrap;
}
.session-time{white-space:nowrap}
.session-line-2{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:8px;
  margin-top:2px;
  font-size:11px;
  color:var(--text-muted);
  min-width:0;
}
.session-snippet{
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
  flex:1 1 auto;
  line-height:1.2;
}
.session-ws{
  flex:0 0 auto;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size:9.5px;
  color:var(--text-muted);
  background:rgba(255,255,255,0.03);
  padding:1px 4px;
  border-radius:3px;
  max-width:110px;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}
.modal-empty{padding:30px;text-align:center;color:var(--text-muted);font-size:12.5px}

.drop-overlay{
  position:fixed;
  inset:0;
  background:rgba(0,0,0,0.6);
  backdrop-filter:blur(4px);
  display:none;
  place-items:center;
  z-index:60;
  padding:20px;
}
.drop-overlay.show{display:grid}
.drop-box{
  border:2px dashed var(--accent);
  background:rgba(17,17,20,0.95);
  border-radius:var(--radius-xl);
  padding:24px 20px;
  text-align:center;
  max-width:380px;
  width:100%;
}

@media(max-width:640px){
  :root{--hdr-h:46px}
  .hdr-inner{padding:0 8px;gap:5px;flex-wrap:nowrap;overflow:hidden}
  .brand{gap:6px}
  .brand b{font-size:12px;max-width:88px}
  .logo-ans pre{font:3.2px/3.2px ui-monospace,SFMono-Regular,Menlo,monospace}
  .ver-pill{display:none}
  .pill-group{padding:2px 4px}
  .pill-select-wrap select{max-width:185px;font-size:11px;padding:4px 18px 4px 6px}
  .hdr-btn{min-height:32px;min-width:32px;padding:0;justify-content:center}
  .hdr-btn .btn-text{display:none}
  .empty-logo-box{padding:10px 14px}
  .empty-logo-box .logo-ans pre{font:5.2px/5.2px ui-monospace,SFMono-Regular,Menlo,monospace}
  .empty-title{font-size:17px}
  .suggestions-grid{grid-template-columns:1fr}
  .composer-inner{padding:6px 8px 8px}
  .composer-box{padding:7px 8px}
  .quota-pill{max-width:180px;font-size:10px;padding:0 8px;height:32px}
  .tool-action-btn{height:32px;min-width:32px;padding:0 8px;justify-content:center}
  .tool-action-btn .btn-text{display:none}
  .send-btn{height:32px;padding:0 12px;min-width:54px;font-size:11px}

  .modal-overlay{align-items:flex-end;padding:0}
  .modal-card{
    width:100%;
    max-height:84vh;
    border-radius:20px 20px 0 0;
    border-bottom:0;
    border-left:0;
    border-right:0;
    box-shadow:0 -10px 40px rgba(0,0,0,0.7);
    animation:slide-up 0.2s cubic-bezier(0.16,1,0.3,1);
  }
  @keyframes slide-up{from{transform:translateY(100%)}to{transform:translateY(0)}}
  .sheet-handle{
    display:block;
    width:36px;
    height:4px;
    border-radius:999px;
    background:var(--border-light);
    margin:8px auto 2px;
    flex:0 0 auto;
  }
}
@media(max-width:380px){
  .brand b{display:none}
  .pill-select-wrap select{max-width:145px}
  .quota-pill{max-width:130px;font-size:9.5px;padding:0 6px}
}
</style>
</head>
<body>

<header id="hdr">
  <div class="hdr-inner">
    <div class="hdr-left">
      <a href="#" class="brand" id="brandLink" title="Antigravity Web">
        <div class="logo-ans"><pre>         <span style="color:rgb(154,159,53)">▄</span><span style="color:rgb(189,171,65);background:rgb(186,143,36)">▄</span><span style="color:rgb(198,146,68);background:rgb(228,143,46)">▄</span><span style="color:rgb(212,120,70);background:rgb(234,113,53)">▄</span><span style="color:rgb(227,97,68);background:rgb(198,75,48)">▄</span><span style="color:rgb(195,67,54)">▄</span>
        <span style="color:rgb(106,161,87)">▄</span><span style="color:rgb(113,178,116);background:rgb(148,185,88)">▄</span><span style="color:rgb(109,164,130);background:rgb(148,168,95)">▄</span><span style="color:rgb(118,147,137);background:rgb(159,148,99)">▄</span><span style="color:rgb(140,130,135);background:rgb(180,126,97)">▄</span><span style="color:rgb(168,112,122);background:rgb(202,105,89)">▄</span><span style="color:rgb(196,96,106);background:rgb(223,87,79)">▄</span><span style="color:rgb(176,68,74)">▄</span>
       <span style="color:rgb(45,91,69)">▄</span><span style="color:rgb(77,171,155);background:rgb(100,182,126)">▄</span><span style="color:rgb(65,159,180);background:rgb(84,169,148)">▄</span><span style="color:rgb(60,149,199);background:rgb(78,157,166)">▄</span><span style="color:rgb(63,141,210);background:rgb(84,144,177)">▄</span><span style="color:rgb(75,133,210);background:rgb(102,132,175)">▄</span><span style="color:rgb(98,126,200);background:rgb(130,119,163)">▄</span><span style="color:rgb(127,116,182);background:rgb(162,106,143)">▄</span><span style="color:rgb(157,107,159);background:rgb(191,94,121)">▄</span>
       <span style="color:rgb(58,158,184);background:rgb(57,134,128)">▄</span><span style="color:rgb(53,150,210);background:rgb(62,160,184)">▄</span><span style="color:rgb(50,142,228);background:rgb(54,149,207)">▄</span><span style="color:rgb(49,137,240);background:rgb(51,142,224)">▄</span><span style="color:rgb(49,135,246);background:rgb(53,138,233)">▄</span><span style="color:rgb(53,134,247);background:rgb(60,134,234)">▄</span><span style="color:rgb(62,133,244);background:rgb(75,130,228)">▄</span><span style="color:rgb(76,131,237);background:rgb(97,126,215)">▄</span><span style="color:rgb(97,129,225);background:rgb(124,120,197)">▄</span><span style="color:rgb(118,124,207);background:rgb(111,86,136)">▄</span>
      <span style="color:rgb(29,96,139)">▄</span><span style="color:rgb(47,142,228);background:rgb(51,149,209)">▄</span><span style="color:rgb(48,137,242);background:rgb(50,142,229)">▄</span><span style="color:rgb(35,97,180);background:rgb(49,137,242)">▄</span><span style="background:rgb(45,124,230)">▄</span><span style="background:rgb(32,89,168)">▄</span><span style="background:rgb(34,90,169)">▄</span><span style="background:rgb(51,125,234)">▄</span><span style="color:rgb(43,101,188);background:rgb(64,135,249)">▄</span><span style="color:rgb(66,137,251);background:rgb(78,135,243)">▄</span><span style="color:rgb(79,138,247);background:rgb(96,135,234)">▄</span><span style="color:rgb(56,86,151)">▄</span>
      <span style="color:rgb(44,138,237);background:rgb(40,135,214)">▄</span><span style="color:rgb(46,135,247);background:rgb(46,138,240)">▄</span><span style="background:rgb(42,118,218)">▄</span>      <span style="background:rgb(53,122,227)">▄</span><span style="color:rgb(59,136,253);background:rgb(67,138,252)">▄</span><span style="color:rgb(66,138,252);background:rgb(71,129,232)">▄</span>
     <span style="color:rgb(45,136,243);background:rgb(35,113,192)">▄</span><span style="color:rgb(44,127,236);background:rgb(46,136,244)">▄</span><span style="background:rgb(34,97,181)">▄</span>        <span style="background:rgb(41,102,192)">▄</span><span style="color:rgb(51,129,243);background:rgb(59,136,253)">▄</span><span style="color:rgb(57,135,253);background:rgb(49,107,198)">▄</span>
   <span style="color:rgb(41,120,218)">▄</span><span style="color:rgb(44,125,231);background:rgb(43,130,232)">▄</span><span style="background:rgb(46,132,244)">▄</span>            <span style="background:rgb(51,132,251)">▄</span><span style="color:rgb(47,125,238);background:rgb(51,126,238)">▄</span><span style="color:rgb(41,109,207)">▄</span></pre></div>
        <b>Antigravity Web</b>
        <span class="ver-pill" id="verBadge">—</span>
      </a>
    </div>

    <div class="hdr-center">
      <div class="pill-group">
        <div class="pill-select-wrap" title="Active Model (Ctrl+K)">
          <select id="hdrModel" aria-label="Model"></select>
          <svg class="chevron" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z" clip-rule="evenodd"/></svg>
        </div>
      </div>
    </div>

    <div class="hdr-right">
      <button id="hdrSessionsBtn" class="hdr-btn" type="button" title="Sessions (Ctrl+L)" aria-label="Sessions">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span class="btn-text">Sessions</span>
      </button>
      <button id="clearBtn" class="hdr-btn" type="button" title="New Chat (Ctrl+N)" aria-label="New Chat">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 5v14M5 12h14"/></svg>
        <span class="btn-text">New</span>
      </button>
    </div>
  </div>
</header>

<main id="chat" role="log" aria-live="polite" aria-label="Chat history"></main>

<div id="composer">
  <div class="composer-inner">
    <div id="preview"></div>
    <div class="composer-box">
      <div id="slashMenu" role="listbox" aria-label="Slash commands"></div>
      <textarea id="prompt" rows="1" placeholder="Message Antigravity… (Enter to send, / for commands)" aria-label="Prompt"></textarea>
      
      <div class="composer-toolbar">
        <div class="toolbar-left">
          <button id="attachBtn" class="tool-action-btn" type="button" title="Attach image (max 10MB)" aria-label="Attach image">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/></svg>
            <span class="btn-text">Attach</span>
          </button>
          <input id="file" type="file" accept="image/*,.jpg,.jpeg,.png,.webp" style="display:none">

          <button id="quotaBadge" class="quota-pill" type="button" title="Quota: click to refresh" role="status">
            <span class="quota-dot"></span>
            <span id="quotaText">quota —</span>
          </button>
        </div>

        <div class="toolbar-right">
          <span class="char-counter" id="counter" aria-live="polite"></span>
          <button id="send" class="send-btn primary" type="button" aria-label="Send message">
            <svg class="send-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            <span id="sendLabel">Send</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</div>

<div id="dropOverlay" class="drop-overlay" aria-hidden="true">
  <div class="drop-box">
    <b style="font-size:14px;color:var(--text)">Drop image to attach</b>
    <div style="color:var(--text-muted);font-size:12px;margin-top:4px">JPG, PNG, WEBP • max 10MB</div>
  </div>
</div>

<div id="sessionOverlay" class="modal-overlay" aria-hidden="true">
  <div class="modal-card">
    <div class="sheet-handle"></div>
    <div class="modal-head">
      <div class="modal-head-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:15px;height:15px;color:var(--text-muted)"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <h2>Sessions</h2>
        <span class="session-total-pill" id="sessionTotalCount">0</span>
      </div>
      <div class="modal-actions">
        <button id="newSessionBtn" class="modal-btn-new" type="button" title="Start new session">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          <span>New Chat</span>
        </button>
        <button id="closeSessionsBtn" class="modal-close-btn" type="button" title="Close (Esc)" aria-label="Close">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
    </div>
    <div class="modal-search-wrap">
      <div class="modal-search-box">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="sessionSearch" class="modal-search-input" placeholder="Search sessions by title or path…" aria-label="Search sessions">
        <span class="session-count-badge" id="sessionCount">0</span>
      </div>
    </div>
    <div id="sessionList" class="modal-body"></div>
  </div>
</div>

<script>
const chatEl=document.getElementById('chat'), promptEl=document.getElementById('prompt');
const fileEl=document.getElementById('file'), attachBtn=document.getElementById('attachBtn'), previewEl=document.getElementById('preview');
const counterEl=document.getElementById('counter'), dropOverlay=document.getElementById('dropOverlay');
const quotaBadge=document.getElementById('quotaBadge'), quotaText=document.getElementById('quotaText');
const slashMenu=document.getElementById('slashMenu'), verBadge=document.getElementById('verBadge'), sendBtn=document.getElementById('send'), sendLabel=document.getElementById('sendLabel');
const hdrModelEl=document.getElementById('hdrModel');
const hdrSessionsBtn=document.getElementById('hdrSessionsBtn'), clearBtn=document.getElementById('clearBtn');
const sessionOverlay=document.getElementById('sessionOverlay'), sessionList=document.getElementById('sessionList'), sessionSearch=document.getElementById('sessionSearch');

let pendingImage=null;
let history=[];
let modelCache=[];
let currentAbort=null;
let currentConversation=null;
let sessionCache=[];
let quotaCache=null;
let slashCommands=[];
let slashActive=-1;

function cidKey(id){ return `agy_web_history:${id||'local'}`; }
function loadHistory(){
  const raw=localStorage.getItem(cidKey(currentConversation));
  try{ return raw ? JSON.parse(raw) : []; }catch(e){ return []; }
}
function saveHistory(){
  if(currentConversation) localStorage.setItem(cidKey(currentConversation), JSON.stringify(history.slice(-100)));
  else localStorage.setItem('agy_web_history', JSON.stringify(history.slice(-100)));
  localStorage.setItem('agy_web_last_cid', currentConversation||'');
}

function esc(s){ return String(s||'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;'); }
function md(s){
  if(!s) return '—';
  const blocks=[];
  let html=s.replace(/```([a-z0-9_-]*)\n?([\s\S]*?)```/gi, (m, lang, code)=>{
    const idx=blocks.length; blocks.push({lang:lang.trim(), code:code}); return `@@CODE${idx}@@`;
  });
  html=esc(html);
  html=html.replace(/`([^`]+?)`/g, '<code>$1</code>');
  html=html.replace(/^######\s+(.+)$/gm, '<h6>$1</h6>');
  html=html.replace(/^#####\s+(.+)$/gm, '<h5>$1</h5>');
  html=html.replace(/^####\s+(.+)$/gm, '<h4>$1</h4>');
  html=html.replace(/^###\s+(.+)$/gm, '<h3>$1</h3>');
  html=html.replace(/^##\s+(.+)$/gm, '<h2>$1</h2>');
  html=html.replace(/^#\s+(.+)$/gm, '<h1>$1</h1>');
  html=html.replace(/^\|(.+\|)\n\|[-:\s|]+\|\n((?:\|.+\|\n?)+)/gm, (m,hdr,rows)=>{
    const ths=hdr.split('|').slice(1,-1).map(c=>`<th>${esc(c.trim())}</th>`).join('');
    const trs=rows.trim().split('\n').map(r=>{
      const tds=r.split('|').slice(1,-1).map(c=>`<td>${esc(c.trim())}</td>`).join('');
      return `<tr>${tds}</tr>`;
    }).join('');
    return `<table><thead><tr>${ths}</tr></thead><tbody>${trs}</tbody></table>`;
  });
  html=html.replace(/\*\*\*(.+?)\*\*\*/g, '<b><i>$1</i></b>');
  html=html.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
  html=html.replace(/__(.+?)__/g, '<b>$1</b>');
  html=html.replace(/(?<!\w)\*(?!\*)(.+?)(?<!\*)\*(?!\w)/g, '<i>$1</i>');
  html=html.replace(/(?<!\w)_(.+?)_(?!\w)/g, '<i>$1</i>');
  html=html.replace(/^&gt;\s+(.+)$/gm, '<blockquote>$1</blockquote>');
  html=html.replace(/^\s*---+\s*$/gm, '<hr>');
  html=html.replace(/((?:^[-*]\s+.+(?:\n|$))+)/gm, (m)=>{
    const items=m.trim().split('\n').map(l=>l.replace(/^[-*]\s+/, '').trim()).map(l=>`<li>${l}</li>`).join('');
    return `<ul>${items}</ul>`;
  });
  html=html.replace(/((?:^\d+\.\s+.+(?:\n|$))+)/gm, (m)=>{
    const items=m.trim().split('\n').map(l=>l.replace(/^\d+\.\s+/, '').trim()).map(l=>`<li>${l}</li>`).join('');
    return `<ol>${items}</ol>`;
  });
  html=html.replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');
  html=html.replace(/@@CODE(\d+)@@/g, (m, idx)=>{
    const b=blocks[Number(idx)];
    const langLabel=b.lang || 'code';
    return `<pre><div class="code-header"><span>${esc(langLabel)}</span><button class="copy-code" type="button" aria-label="Copy code">Copy</button></div><code>${esc(b.code)}</code></pre>`;
  });
  const parts=html.split(/\n{2,}/).map(b=>{
    b=b.trim(); if(!b) return '';
    if(/^<(h[1-6]|ul|ol|pre|blockquote|hr|table|p)/.test(b)) return b;
    if(b.includes('<pre')||b.includes('<table')||b.includes('<ul')||b.includes('<ol')||b.includes('<blockquote')||b.includes('<h')) return b;
    return `<p>${b.replace(/\n/g,'<br>')}</p>`;
  }).filter(Boolean);
  return `<div class="md">${parts.join('') || `<p>${html.replace(/\n/g,'<br>')}</p>`}</div>`;
}

function syncLayout(){
  const c=document.getElementById('composer');
  const h=c ? c.offsetHeight : 120;
  const vv=window.visualViewport;
  if(vv){
    const kb=Math.max(0, window.innerHeight - vv.height - vv.offsetTop);
    document.documentElement.style.setProperty('--kb', kb+'px');
  } else {
    document.documentElement.style.setProperty('--kb', '0px');
  }
  document.documentElement.style.setProperty('--composer-h', (h + 16)+'px');
}

function autoSize(){
  promptEl.style.height='auto';
  promptEl.style.height=Math.min(promptEl.scrollHeight, 150)+'px';
  const len=promptEl.value.length;
  counterEl.textContent=len ? `${len}` : '';
  syncLayout();
}
promptEl.addEventListener('input', autoSize);
promptEl.addEventListener('focus', ()=>{
  setTimeout(()=>{ window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' }); }, 180);
});
new ResizeObserver(syncLayout).observe(document.getElementById('composer'));
window.addEventListener('resize', syncLayout);
if(window.visualViewport){
  window.visualViewport.addEventListener('resize', syncLayout);
  window.visualViewport.addEventListener('scroll', syncLayout);
}

function render(){
  chatEl.innerHTML='';
  if(history.length===0){
    const lastSessionId=localStorage.getItem('agy_web_last_cid');
    chatEl.innerHTML=`
      <div class="empty-state">
        <div class="empty-logo-box">
          <div class="logo-ans"><pre>         <span style="color:rgb(154,159,53)">▄</span><span style="color:rgb(189,171,65);background:rgb(186,143,36)">▄</span><span style="color:rgb(198,146,68);background:rgb(228,143,46)">▄</span><span style="color:rgb(212,120,70);background:rgb(234,113,53)">▄</span><span style="color:rgb(227,97,68);background:rgb(198,75,48)">▄</span><span style="color:rgb(195,67,54)">▄</span>
        <span style="color:rgb(106,161,87)">▄</span><span style="color:rgb(113,178,116);background:rgb(148,185,88)">▄</span><span style="color:rgb(109,164,130);background:rgb(148,168,95)">▄</span><span style="color:rgb(118,147,137);background:rgb(159,148,99)">▄</span><span style="color:rgb(140,130,135);background:rgb(180,126,97)">▄</span><span style="color:rgb(168,112,122);background:rgb(202,105,89)">▄</span><span style="color:rgb(196,96,106);background:rgb(223,87,79)">▄</span><span style="color:rgb(176,68,74)">▄</span>
       <span style="color:rgb(45,91,69)">▄</span><span style="color:rgb(77,171,155);background:rgb(100,182,126)">▄</span><span style="color:rgb(65,159,180);background:rgb(84,169,148)">▄</span><span style="color:rgb(60,149,199);background:rgb(78,157,166)">▄</span><span style="color:rgb(63,141,210);background:rgb(84,144,177)">▄</span><span style="color:rgb(75,133,210);background:rgb(102,132,175)">▄</span><span style="color:rgb(98,126,200);background:rgb(130,119,163)">▄</span><span style="color:rgb(127,116,182);background:rgb(162,106,143)">▄</span><span style="color:rgb(157,107,159);background:rgb(191,94,121)">▄</span>
       <span style="color:rgb(58,158,184);background:rgb(57,134,128)">▄</span><span style="color:rgb(53,150,210);background:rgb(62,160,184)">▄</span><span style="color:rgb(50,142,228);background:rgb(54,149,207)">▄</span><span style="color:rgb(49,137,240);background:rgb(51,142,224)">▄</span><span style="color:rgb(49,135,246);background:rgb(53,138,233)">▄</span><span style="color:rgb(53,134,247);background:rgb(60,134,234)">▄</span><span style="color:rgb(62,133,244);background:rgb(75,130,228)">▄</span><span style="color:rgb(76,131,237);background:rgb(97,126,215)">▄</span><span style="color:rgb(97,129,225);background:rgb(124,120,197)">▄</span><span style="color:rgb(118,124,207);background:rgb(111,86,136)">▄</span>
      <span style="color:rgb(29,96,139)">▄</span><span style="color:rgb(47,142,228);background:rgb(51,149,209)">▄</span><span style="color:rgb(48,137,242);background:rgb(50,142,229)">▄</span><span style="color:rgb(35,97,180);background:rgb(49,137,242)">▄</span><span style="background:rgb(45,124,230)">▄</span><span style="background:rgb(32,89,168)">▄</span><span style="background:rgb(34,90,169)">▄</span><span style="background:rgb(51,125,234)">▄</span><span style="color:rgb(43,101,188);background:rgb(64,135,249)">▄</span><span style="color:rgb(66,137,251);background:rgb(78,135,243)">▄</span><span style="color:rgb(79,138,247);background:rgb(96,135,234)">▄</span><span style="color:rgb(56,86,151)">▄</span>
      <span style="color:rgb(44,138,237);background:rgb(40,135,214)">▄</span><span style="color:rgb(46,135,247);background:rgb(46,138,240)">▄</span><span style="background:rgb(42,118,218)">▄</span>      <span style="background:rgb(53,122,227)">▄</span><span style="color:rgb(59,136,253);background:rgb(67,138,252)">▄</span><span style="color:rgb(66,138,252);background:rgb(71,129,232)">▄</span>
     <span style="color:rgb(45,136,243);background:rgb(35,113,192)">▄</span><span style="color:rgb(44,127,236);background:rgb(46,136,244)">▄</span><span style="background:rgb(34,97,181)">▄</span>        <span style="background:rgb(41,102,192)">▄</span><span style="color:rgb(51,129,243);background:rgb(59,136,253)">▄</span><span style="color:rgb(57,135,253);background:rgb(49,107,198)">▄</span>
   <span style="color:rgb(41,120,218)">▄</span><span style="color:rgb(44,125,231);background:rgb(43,130,232)">▄</span><span style="background:rgb(46,132,244)">▄</span>            <span style="background:rgb(51,132,251)">▄</span><span style="color:rgb(47,125,238);background:rgb(51,126,238)">▄</span><span style="color:rgb(41,109,207)">▄</span></pre></div>
        </div>
        <h1 class="empty-title">Antigravity</h1>
        <p class="empty-sub">Local pairing agent on Termux. Fast, modular & full-featured.</p>

        <div id="quickResumeWrap" style="display:none">
          <div class="quick-resume-card" id="quickResumeBtn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg>
            <span>Resume previous: <b id="quickResumeTitle">—</b></span>
          </div>
        </div>

        <div class="suggestions-grid">
          <button class="chip" data-prompt="Explain this codebase architecture in 5 bullets">
            <div class="chip-icon">📂</div>
            <div class="chip-text"><b>Explain codebase</b><span>Architecture & structure</span></div>
          </button>
          <button class="chip" data-prompt="Review recent changes for bugs and over-engineering">
            <div class="chip-icon">⚡</div>
            <div class="chip-text"><b>Review changes</b><span>Bugs & ponytail check</span></div>
          </button>
          <button class="chip" data-prompt="Write a minimal, dependency-free script to solve this">
            <div class="chip-icon">🛠️</div>
            <div class="chip-text"><b>Minimal script</b><span>Stdlib-only, clean path</span></div>
          </button>
          <button class="chip" data-prompt="Help me debug this error, suggest the smallest fix">
            <div class="chip-icon">🔍</div>
            <div class="chip-text"><b>Diagnose error</b><span>Smallest root-cause fix</span></div>
          </button>
        </div>

        <div class="shortcuts-bar">
          <span class="sc-tag"><kbd>Enter</kbd> send</span>
          <span class="sc-tag"><kbd>Shift+Enter</kbd> newline</span>
          <span class="sc-tag"><kbd>/</kbd> commands</span>
          <span class="sc-tag"><kbd>Ctrl+K</kbd> models</span>
          <span class="sc-tag"><kbd>Ctrl+L</kbd> sessions</span>
        </div>
      </div>
    `;

    chatEl.querySelectorAll('.chip').forEach(b=>{
      b.onclick=()=>{ promptEl.value=b.dataset.prompt; autoSize(); promptEl.focus(); };
    });

    if(lastSessionId){
      fetch('/api/sessions').then(r=>r.json()).then(j=>{
        const found=(j.sessions||[]).find(s=>s.id===lastSessionId);
        if(found && chatEl.querySelector('#quickResumeWrap')){
          const wrap=chatEl.querySelector('#quickResumeWrap');
          const titleEl=chatEl.querySelector('#quickResumeTitle');
          titleEl.textContent=found.title || found.preview || found.id.slice(0,8);
          wrap.style.display='block';
          chatEl.querySelector('#quickResumeBtn').onclick=()=>resumeSession(found.id);
        }
      }).catch(()=>{});
    }

    syncLayout();
    return;
  }

  history.forEach((m, i)=>{
    const row=document.createElement('div');
    row.className='msg '+(m.role==='user'?'user':'assistant');
    row.dataset.idx=String(i);

    const av=document.createElement('div');
    av.className='avatar';
    av.textContent=m.role==='user'?'You':'agy';
    row.appendChild(av);

    const bub=document.createElement('div');
    bub.className='bubble';

    if(m.image){
      const img=document.createElement('img');
      img.src=m.image;
      img.loading='lazy';
      img.alt='attached photo';
      bub.appendChild(img);
    }

    const txt=document.createElement('div');
    if(m.thinking){
      txt.className='thinking-box';
      txt.innerHTML='<div class="thinking-header"><span class="pulse-dot"></span> Thinking…</div>';
    } else if(m.role==='assistant'){
      txt.innerHTML=md(m.text);
    } else {
      txt.innerHTML=esc(m.text).replace(/\n/g,'<br>');
    }
    bub.appendChild(txt);

    if(m.role==='assistant' && !m.thinking){
      const acts=document.createElement('div');
      acts.className='msg-actions';

      const cp=document.createElement('button');
      cp.className='action-btn';
      cp.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg><span>Copy</span>';
      cp.onclick=()=>{
        navigator.clipboard.writeText(m.text);
        cp.classList.add('copy-pop');
        cp.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="#34a853" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg><span style="color:#34a853">Copied</span>';
        setTimeout(()=>{
          cp.classList.remove('copy-pop');
          cp.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg><span>Copy</span>';
        }, 1200);
      };
      acts.appendChild(cp);

      if(m.error){
        const rt=document.createElement('button');
        rt.className='action-btn';
        rt.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"/></svg><span>Retry</span>';
        rt.onclick=()=>{ promptEl.value=history[i-1]?.text||''; autoSize(); promptEl.focus(); };
        acts.appendChild(rt);
      }

      if(m.duration || m.model){
        const meta=document.createElement('div');
        meta.className='msg-meta';
        if(m.duration) meta.innerHTML+=`<span class="msg-meta-tag">${Number(m.duration).toFixed(1)}s</span>`;
        if(m.model) meta.innerHTML+=`<span class="msg-meta-tag">${esc(m.model)}</span>`;
        acts.appendChild(meta);
      }

      bub.appendChild(acts);
    }

    if(m.error){
      const errEl=document.createElement('div');
      errEl.className='msg-error';
      errEl.textContent='Error: '+m.error;
      bub.appendChild(errEl);
    }

    row.appendChild(bub);
    chatEl.appendChild(row);
  });

  window.scrollTo(0, document.body.scrollHeight);
  syncLayout();
}

async function loadModels(){
  try{
    const r=await fetch('/api/models');
    const j=await r.json();
    modelCache=j.models||[];
    hdrModelEl.innerHTML='';
    modelCache.forEach(m=>{
      const o=document.createElement('option');
      o.value=m.id;
      o.textContent=m.label||m.id;
      hdrModelEl.appendChild(o);
    });
    const saved=localStorage.getItem('agy_web_model');
    if(saved && [...hdrModelEl.options].some(o=>o.value===saved)) hdrModelEl.value=saved;
  }catch(e){}
}
hdrModelEl.addEventListener('change', ()=>{
  localStorage.setItem('agy_web_model', hdrModelEl.value);
  renderQuota(quotaCache||[]);
});
loadModels();

fetch('/api/health').then(r=>r.json()).then(j=>{
  if(j.version && verBadge){
    verBadge.textContent=`v${j.version}`;
    verBadge.style.display='inline-block';
  } else if(verBadge) verBadge.style.display='none';
}).catch(()=>{ if(verBadge) verBadge.style.display='none'; });

function modelGroup(id){
  const l=(id||'').toLowerCase();
  if(l.startsWith('gemini')) return 'gemini';
  if(l.startsWith('claude') || l.startsWith('gpt-') || l.startsWith('gpt_')) return '3p';
  return 'gemini';
}
function renderQuota(groups){
  if(!groups || !groups.length){
    quotaText.textContent='quota —';
    return;
  }
  const want=modelGroup(hdrModelEl.value);
  let g0=groups.find(g=>(g.key||'').toLowerCase()===want) || groups.find(g=>g.name.toLowerCase().includes(want==='gemini'?'gemini':'claude')) || groups[0];
  if(!g0){ quotaText.textContent='quota —'; return; }
  const buckets=g0.buckets||[];
  const w5=buckets.find(b=>(b.window||'').toLowerCase()==='5h'||(b.id||'').toLowerCase().includes('5h')) || buckets[0];
  const wk=buckets.find(b=>(b.window||'').toLowerCase()==='weekly'||(b.id||'').toLowerCase().includes('weekly')) || buckets[1] || buckets[0];
  const avail5=w5 ? w5.avail_pct : 0;
  const availW=wk ? wk.avail_pct : 0;
  const label=g0.key==='gemini' ? 'Gemini' : (g0.key==='3p' ? 'Claude/GPT' : g0.name.split(' ')[0]);

  quotaText.textContent=`${label} 5h ${avail5}% · wk ${availW}%`;

  quotaBadge.classList.remove('exhausted','warning');
  if(avail5 < 15 || availW < 15) quotaBadge.classList.add('exhausted');
  else if(avail5 < 40 || availW < 40) quotaBadge.classList.add('warning');

  const tipParts=[];
  for(const g of groups){
    const sname=g.key==='gemini'?'Gemini':g.key==='3p'?'Claude/GPT':g.name;
    for(const b of g.buckets){
      tipParts.push(`${sname} ${b.window||'window'}: ${b.avail_pct}% left`);
    }
  }
  quotaBadge.title=tipParts.join(' • ') + ' • Click to refresh';
}
async function loadQuota(){
  quotaBadge.classList.add('refreshing');
  try{
    const r=await fetch('/api/quota');
    const j=await r.json();
    quotaCache=j.groups||[];
    renderQuota(quotaCache);
  }catch(e){
    quotaText.textContent='quota —';
  }finally{
    setTimeout(()=>quotaBadge.classList.remove('refreshing'), 450);
  }
}
loadQuota();
quotaBadge.onclick=loadQuota;
setInterval(loadQuota, 45000);
document.addEventListener('visibilitychange', ()=>{ if(!document.hidden) loadQuota(); });

async function loadSlash(){
  try{
    const r=await fetch('/api/commands');
    const j=await r.json();
    slashCommands=j.commands||[];
  }catch(e){}
}
loadSlash();

function showSlash(filter){
  if(!slashCommands.length || filter===''){ slashMenu.classList.remove('on'); return; }
  const q=filter.toLowerCase();
  const matched=slashCommands.filter(c=>c.name.toLowerCase().includes(q)).slice(0, 10);
  if(!matched.length){ slashMenu.classList.remove('on'); return; }
  slashMenu.innerHTML='';
  matched.forEach((c, i)=>{
    const d=document.createElement('div');
    d.className='slash-item'+(i===slashActive?' active':'');
    d.innerHTML=`<b>/${esc(c.name)}</b><span>${esc(c.description||'')}</span>`;
    d.onclick=()=>{
      promptEl.value='/'+c.name+' ';
      autoSize();
      slashMenu.classList.remove('on');
      promptEl.focus();
      slashActive=-1;
    };
    slashMenu.appendChild(d);
  });
  slashMenu.classList.add('on');
}
promptEl.addEventListener('keydown', e=>{
  if(slashMenu.classList.contains('on')){
    if(e.key==='ArrowDown'){
      e.preventDefault();
      slashActive=Math.min(slashActive+1, slashMenu.children.length-1);
      [...slashMenu.children].forEach((el,i)=>el.classList.toggle('active', i===slashActive));
    } else if(e.key==='ArrowUp'){
      e.preventDefault();
      slashActive=Math.max(slashActive-1, 0);
      [...slashMenu.children].forEach((el,i)=>el.classList.toggle('active', i===slashActive));
    } else if(e.key==='Enter' && slashActive>=0){
      e.preventDefault();
      slashMenu.children[slashActive].click();
    } else if(e.key==='Escape'){
      slashMenu.classList.remove('on');
      slashActive=-1;
    }
  }
});
promptEl.addEventListener('input', ()=>{
  const v=promptEl.value;
  if(v.startsWith('/')){
    const m=v.slice(1).split(/\s/)[0];
    showSlash(m);
    slashActive=-1;
  } else {
    slashMenu.classList.remove('on');
  }
});
document.addEventListener('click', e=>{
  if(!slashMenu.contains(e.target) && e.target!==promptEl) slashMenu.classList.remove('on');
});

function timeAgo(s){
  try{
    const d=new Date(s);
    const diff=(Date.now()-d)/1000;
    if(diff<60) return 'just now';
    if(diff<3600) return Math.floor(diff/60)+'m ago';
    if(diff<86400) return Math.floor(diff/3600)+'h ago';
    if(diff<86400*7) return Math.floor(diff/86400)+'d ago';
    return d.toLocaleDateString();
  }catch(e){ return s; }
}

function formatWorkspace(ws){
  if(!ws) return '';
  let s=String(ws).replace(/^[\["']+|[\]"']+$/g, '').replace(/^file:\/\//, '').replace(/^\/data\/data\/com\.termux\/files\/home/, '~');
  const parts=s.split('/');
  if(parts.length>3) return '~/' + parts.slice(-2).join('/');
  return s;
}

function renderSessionList(sessions){
  sessionList.innerHTML='';
  if(!sessions.length){
    sessionList.innerHTML='<div class="modal-empty">No sessions found.</div>';
    return;
  }
  sessions.forEach(s=>{
    const isActive=s.id===currentConversation;
    const card=document.createElement('button');
    card.className='session-item'+(isActive?' active':'');
    card.type='button';
    card.dataset.id=s.id;

    const titleText=s.title || s.preview || s.id.slice(0,8);
    const snippetText=s.preview && s.preview!==titleText ? s.preview : (s.title ? s.id.slice(0,8) : '');
    const wsFormatted=formatWorkspace(s.workspace);

    card.innerHTML=`
      <div class="session-dot"></div>
      <div class="session-main">
        <div class="session-line-1">
          <span class="session-title">${esc(titleText)}</span>
          <div class="session-right-meta">
            <span class="session-steps">${esc(String(s.steps||0))} steps</span>
            <span class="session-time">${esc(timeAgo(s.updated))}</span>
          </div>
        </div>
        <div class="session-line-2">
          <span class="session-snippet">${esc(snippetText)}</span>
          ${wsFormatted ? `<span class="session-ws">${esc(wsFormatted)}</span>` : ''}
        </div>
      </div>
    `;

    card.onclick=()=>resumeSession(s.id);
    sessionList.appendChild(card);
  });
}

async function loadSessions(){
  sessionList.innerHTML='<div class="modal-empty">Loading sessions…</div>';
  try{
    const r=await fetch('/api/sessions');
    const j=await r.json();
    sessionCache=j.sessions||[];
    const totalEl=document.getElementById('sessionTotalCount');
    if(totalEl) totalEl.textContent=sessionCache.length;
    const countEl=document.getElementById('sessionCount');
    if(countEl) countEl.textContent=sessionCache.length;
    renderSessionList(sessionCache);
  }catch(e){
    sessionList.innerHTML=`<div class="modal-empty" style="color:var(--danger)">Failed to load: ${esc(String(e))}</div>`;
  }
}

sessionSearch.addEventListener('input', ()=>{
  const q=sessionSearch.value.trim().toLowerCase();
  const countEl=document.getElementById('sessionCount');
  if(!q){
    if(countEl) countEl.textContent=sessionCache.length;
    renderSessionList(sessionCache);
    return;
  }
  const filtered=sessionCache.filter(s=>
    (s.title||'').toLowerCase().includes(q) ||
    (s.preview||'').toLowerCase().includes(q) ||
    (s.workspace||'').toLowerCase().includes(q) ||
    s.id.toLowerCase().includes(q)
  );
  if(countEl) countEl.textContent=`${filtered.length}/${sessionCache.length}`;
  renderSessionList(filtered);
});

sessionSearch.addEventListener('keydown', e=>{
  const items=Array.from(sessionList.querySelectorAll('.session-item'));
  if(!items.length) return;
  const currentIdx=items.findIndex(it=>it.classList.contains('nav-focused'));

  if(e.key==='ArrowDown'){
    e.preventDefault();
    const nextIdx=currentIdx < items.length - 1 ? currentIdx + 1 : 0;
    items.forEach(it=>it.classList.remove('nav-focused'));
    items[nextIdx].classList.add('nav-focused');
    items[nextIdx].scrollIntoView({block:'nearest'});
  } else if(e.key==='ArrowUp'){
    e.preventDefault();
    const prevIdx=currentIdx > 0 ? currentIdx - 1 : items.length - 1;
    items.forEach(it=>it.classList.remove('nav-focused'));
    items[prevIdx].classList.add('nav-focused');
    items[prevIdx].scrollIntoView({block:'nearest'});
  } else if(e.key==='Enter'){
    e.preventDefault();
    if(currentIdx >= 0){
      items[currentIdx].click();
    } else if(items[0]){
      items[0].click();
    }
  }
});

function showSessions(){
  sessionOverlay.classList.add('on');
  sessionOverlay.setAttribute('aria-hidden','false');
  sessionSearch.value='';
  loadSessions();
  setTimeout(()=>sessionSearch.focus(), 60);
}
function hideSessions(){
  sessionOverlay.classList.remove('on');
  sessionOverlay.setAttribute('aria-hidden','true');
}
async function resumeSession(id){
  currentConversation=id;
  localStorage.setItem('agy_web_last_cid', id);
  try{
    const r=await fetch(`/api/session/${encodeURIComponent(id)}/messages`);
    const j=await r.json();
    if(j.messages && j.messages.length){
      history=j.messages.map(m=>({role:m.role, text:m.text}));
      saveHistory();
      hideSessions();
      render();
      return;
    }
  }catch(e){}
  history=loadHistory();
  hideSessions();
  render();
}
function newSession(){
  currentConversation=null;
  localStorage.removeItem('agy_web_last_cid');
  history=[];
  saveHistory();
  hideSessions();
  render();
  promptEl.focus();
}

hdrSessionsBtn.addEventListener('click', showSessions);
document.getElementById('newSessionBtn').addEventListener('click', newSession);
document.getElementById('closeSessionsBtn').addEventListener('click', hideSessions);
clearBtn.addEventListener('click', ()=>{
  if(confirm('Start a new chat?')){ newSession(); }
});
sessionOverlay.addEventListener('click', e=>{ if(e.target===sessionOverlay) hideSessions(); });

(function initSheetGesture(){
  const card=sessionOverlay.querySelector('.modal-card');
  let startY=0, currentY=0, isDragging=false;
  if(!card) return;

  card.addEventListener('touchstart', e=>{
    if(sessionList.scrollTop>0 && !e.target.closest('.sheet-handle') && !e.target.closest('.modal-head')) return;
    startY=e.touches[0].clientY;
    currentY=startY;
    isDragging=true;
  }, {passive:true});

  card.addEventListener('touchmove', e=>{
    if(!isDragging) return;
    currentY=e.touches[0].clientY;
    const dy=currentY - startY;
    if(dy>0){
      card.style.transform=`translateY(${dy}px)`;
      card.style.transition='none';
    }
  }, {passive:true});

  card.addEventListener('touchend', ()=>{
    if(!isDragging) return;
    isDragging=false;
    const dy=currentY - startY;
    card.style.transition='';
    card.style.transform='';
    if(dy>90){
      hideSessions();
    }
  });
})();

function setPreview(){
  previewEl.innerHTML='';
  if(!pendingImage){ syncLayout(); return; }
  const card=document.createElement('div');
  card.className='preview-card';
  const img=document.createElement('img');
  img.src=pendingImage.dataUrl;
  card.appendChild(img);

  const meta=document.createElement('div');
  meta.className='preview-meta';
  const kb=Math.round((pendingImage.size||0)/1024);
  meta.innerHTML=`<b>${esc(pendingImage.name||'image')}</b><br>${kb} KB`;
  card.appendChild(meta);

  const rm=document.createElement('button');
  rm.className='rm-btn';
  rm.type='button';
  rm.innerHTML='&times;';
  rm.title='Remove photo';
  rm.onclick=()=>{ pendingImage=null; setPreview(); };
  card.appendChild(rm);

  previewEl.appendChild(card);
  syncLayout();
}

function handleFile(f){
  if(!f) return;
  if(!f.type.startsWith('image/')){ alert('Only JPG, PNG, and WEBP image files are supported'); return; }
  if(f.size > 10*1024*1024){ alert('Image exceeds 10MB limit'); return; }
  const fr=new FileReader();
  fr.onload=()=>{
    pendingImage={
      dataUrl:fr.result,
      base64:fr.result.split(',')[1],
      mime:f.type||'image/jpeg',
      name:f.name,
      size:f.size
    };
    setPreview();
    promptEl.focus();
  };
  fr.readAsDataURL(f);
}
attachBtn.onclick=()=>fileEl.click();
fileEl.onchange=()=>{ const f=fileEl.files[0]; handleFile(f); fileEl.value=''; };

window.addEventListener('paste', e=>{
  const items=e.clipboardData?.items;
  if(!items) return;
  for(const it of items){
    if(it.type.startsWith('image/')){
      const f=it.getAsFile();
      if(!f) continue;
      const fr=new FileReader();
      fr.onload=()=>{
        pendingImage={
          dataUrl:fr.result,
          base64:fr.result.split(',')[1],
          mime:it.type,
          name:'pasted_image.'+(it.type.split('/')[1]||'png'),
          size:f.size
        };
        setPreview();
      };
      fr.readAsDataURL(f);
      e.preventDefault();
      break;
    }
  }
});

let dragDepth=0;
window.addEventListener('dragenter', e=>{ e.preventDefault(); dragDepth++; dropOverlay.classList.add('show'); });
window.addEventListener('dragover', e=>{ e.preventDefault(); });
window.addEventListener('dragleave', e=>{ e.preventDefault(); dragDepth=Math.max(0, dragDepth-1); if(dragDepth===0) dropOverlay.classList.remove('show'); });
window.addEventListener('drop', e=>{
  e.preventDefault();
  dragDepth=0;
  dropOverlay.classList.remove('show');
  const f=e.dataTransfer?.files?.[0];
  if(f) handleFile(f);
});
dropOverlay.addEventListener('click', ()=>dropOverlay.classList.remove('show'));

function setStreaming(on){
  if(on){
    sendLabel.textContent='Stop';
    sendBtn.classList.remove('primary');
    sendBtn.classList.add('danger');
    sendBtn.dataset.mode='stop';
    sendBtn.querySelector('.send-icon').innerHTML='<rect x="6" y="6" width="12" height="12" rx="1.5" fill="currentColor"/>';
    promptEl.disabled=true;
    attachBtn.disabled=true;
  } else {
    sendLabel.textContent='Send';
    sendBtn.classList.add('primary');
    sendBtn.classList.remove('danger');
    delete sendBtn.dataset.mode;
    sendBtn.querySelector('.send-icon').innerHTML='<path d="M5 12h14M12 5l7 7-7 7"/>';
    promptEl.disabled=false;
    attachBtn.disabled=false;
    promptEl.focus();
  }
}

async function send(){
  if(sendBtn.dataset.mode==='stop' && currentAbort){
    currentAbort.abort();
    return;
  }
  const text=promptEl.value.trim();
  if(!text && !pendingImage) return;

  if(text.startsWith('/model')){
    const parts=text.split(/\s+/).filter(Boolean);
    slashMenu.classList.remove('on');
    slashActive=-1;
    if(parts.length===1){
      hdrModelEl.focus();
      try{ hdrModelEl.showPicker && hdrModelEl.showPicker(); }catch(_){}
      return;
    }
    let want=parts[1].toLowerCase();
    let found=modelCache.find(m=>m.id.toLowerCase()===want) || modelCache.find(m=>m.id.toLowerCase().includes(want)) || modelCache.find(m=>(m.label||'').toLowerCase().includes(want));
    let mid=found ? found.id : parts[1];
    if(![...hdrModelEl.options].some(o=>o.value===mid)){
      const o=document.createElement('option'); o.value=mid; o.textContent=mid;
      hdrModelEl.appendChild(o);
      modelCache.push({id:mid, label:mid});
    }
    hdrModelEl.value=mid;
    localStorage.setItem('agy_web_model', mid);
    renderQuota(quotaCache||[]);
    const effPick=parts[2]||'';
    if(effPick) localStorage.setItem('agy_web_effort', effPick);
    history.push({role:'user', text});
    history.push({role:'assistant', text:`Model updated to \`${mid}\`${effPick ? ` (${effPick})`:''}`, model:mid});
    render();
    saveHistory();
    promptEl.value='';
    autoSize();
    return;
  }
  if(text==='/clear' || text==='/new'){
    slashMenu.classList.remove('on');
    promptEl.value='';
    autoSize();
    if(confirm('Start a new chat?')){ newSession(); }
    return;
  }

  const userMsg={role:'user', text: text||'(photo)', image: pendingImage ? pendingImage.dataUrl : null};
  history.push(userMsg);
  render();
  saveHistory();

  promptEl.value='';
  autoSize();
  const imgToSend=pendingImage;
  pendingImage=null;
  setPreview();

  const eff=localStorage.getItem('agy_web_effort')||'';
  const snapshotModel=hdrModelEl.value + (eff ? ` · ${eff}` : '');
  const th={role:'assistant', text:'', thinking:true, model:snapshotModel};
  history.push(th);
  render();

  setStreaming(true);
  const body={prompt:text, model:hdrModelEl.value, effort:eff, conversation_id:currentConversation||''};
  if(imgToSend) body.image={data:imgToSend.base64, mime:imgToSend.mime, name:imgToSend.name};

  const t0=performance.now();
  currentAbort=new AbortController();
  let fullText='';
  let usage=null;
  let duration=null;
  let gotFirst=false;
  let textEl=null;
  let toolLog=[];

  try{
    const lastRow=chatEl.lastElementChild;
    if(lastRow){
      const bubbleEl=lastRow.querySelector('.bubble');
      textEl=bubbleEl ? bubbleEl.querySelector('div') : null;
    }

    const r=await fetch('/api/chat_stream', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify(body),
      signal:currentAbort.signal
    });

    if(!r.ok){
      const txt=await r.text();
      throw new Error(txt.slice(0, 600) || r.statusText);
    }

    const reader=r.body.getReader();
    const dec=new TextDecoder();
    let buf='';

    function renderThinkingUI(){
      if(!textEl) return;
      const items=toolLog.slice(-4).map(to=>`
        <div class="tool-pill">
          <span class="tool-dot ${to.state==='DONE'?'done':'running'}"></span>
          <code>${esc(to.name)}</code>
          ${to.summary ? `<span class="tool-summary">${esc(to.summary.slice(0,60))}</span>` : ''}
        </div>
      `).join('');

      textEl.className='thinking-box';
      textEl.innerHTML=`
        <div class="thinking-header"><span class="pulse-dot"></span> Executing…</div>
        ${toolLog.length ? `<div class="tools-stream">${items}</div>` : ''}
      `;
    }

    while(true){
      const {value, done}=await reader.read();
      if(done) break;
      buf+=dec.decode(value, {stream:true});
      const lines=buf.split('\n');
      buf=lines.pop();

      for(const line of lines){
        if(!line.trim()) continue;
        let j;
        try{ j=JSON.parse(line); }catch(e){ continue; }

        if(j.t==='tool'){
          toolLog.push({name:j.name, summary:j.summary||'', state:j.state});
          if(toolLog.length>12) toolLog.shift();
          if(!gotFirst) renderThinkingUI();
        } else if(j.t==='tool_out'){
          if(toolLog.length) toolLog[toolLog.length-1].summary=(toolLog[toolLog.length-1].summary + ' → ' + String(j.output).slice(0,40)).slice(0, 80);
          if(!gotFirst) renderThinkingUI();
        } else if(j.t==='delta'){
          if(!gotFirst){
            gotFirst=true;
            if(textEl){ textEl.className=''; textEl.innerHTML=''; }
          }
          fullText+=j.d;
          history[history.length-1].text=fullText;
          history[history.length-1].thinking=false;
          if(textEl) textEl.innerHTML=md(fullText);
          window.scrollTo(0, document.body.scrollHeight);
        } else if(j.t==='done'){
          fullText=j.response || fullText;
          usage=j.usage;
          duration=j.duration || ((performance.now()-t0)/1000);
          if(j.conversation_id && !currentConversation){
            currentConversation=j.conversation_id;
            localStorage.setItem('agy_web_last_cid', currentConversation);
          }
          history[history.length-1].text=fullText;
          history[history.length-1].usage=usage;
          history[history.length-1].duration=duration;
          history[history.length-1].model=history[history.length-1].model || snapshotModel;
          history[history.length-1].thinking=false;
          if(j.status==='ERROR') history[history.length-1].error=j.error||'Generation error';
          if(textEl) textEl.innerHTML=md(fullText);
        } else if(j.t==='error'){
          history[history.length-1].error=j.error;
        }
      }
    }

    if(!gotFirst && fullText && textEl) textEl.innerHTML=md(fullText);
    if(!usage && fullText) duration=((performance.now()-t0)/1000);
    history[history.length-1].duration=history[history.length-1].duration || duration;
    history[history.length-1].thinking=false;
    render();
    saveHistory();
    loadQuota();
  }catch(e){
    history.pop();
    if(e.name==='AbortError'){
      history.push({role:'assistant', text:fullText||'(stopped)', error:'Stopped by user', duration:((performance.now()-t0)/1000)});
    } else {
      history.push({role:'assistant', text:fullText||'Request failed', error:String(e).slice(0,600)});
    }
    render();
    saveHistory();
  }finally{
    setStreaming(false);
    currentAbort=null;
    autoSize();
    syncLayout();
  }
}

sendBtn.onclick=send;
promptEl.addEventListener('keydown', e=>{
  if(e.key==='Enter' && !e.shiftKey){
    e.preventDefault();
    send();
  } else if(e.key==='ArrowUp' && !promptEl.value && !slashMenu.classList.contains('on')){
    const lastUserMsg=[...history].reverse().find(m=>m.role==='user');
    if(lastUserMsg && lastUserMsg.text && lastUserMsg.text!=='(photo)'){
      e.preventDefault();
      promptEl.value=lastUserMsg.text;
      autoSize();
    }
  }
});

document.addEventListener('keydown', e=>{
  if((e.ctrlKey||e.metaKey) && e.key.toLowerCase()==='k'){
    e.preventDefault();
    hdrModelEl.focus();
    try{ hdrModelEl.showPicker && hdrModelEl.showPicker(); }catch(_){}
    return;
  }
  if((e.ctrlKey||e.metaKey) && e.key.toLowerCase()==='l'){
    e.preventDefault();
    showSessions();
    return;
  }
  if((e.ctrlKey||e.metaKey) && e.key.toLowerCase()==='n'){
    e.preventDefault();
    clearBtn.click();
    return;
  }
  if(e.key==='Escape'){
    if(sessionOverlay.classList.contains('on')) hideSessions();
    slashMenu.classList.remove('on');
    if(sendBtn.dataset.mode==='stop' && currentAbort) currentAbort.abort();
  }
});

chatEl.addEventListener('click', e=>{
  const b=e.target.closest('.copy-code');
  if(b){
    const pre=b.closest('pre');
    const code=pre ? pre.querySelector('code')?.textContent : '';
    if(code){
      navigator.clipboard.writeText(code);
      b.textContent='Copied!';
      b.classList.add('copy-pop');
      setTimeout(()=>{
        b.textContent='Copy';
        b.classList.remove('copy-pop');
      }, 1200);
    }
  }
});

(function init(){
  const last=localStorage.getItem('agy_web_last_cid');
  if(last) currentConversation=last;
  history=loadHistory();
  if(!history.length && last){
    fetch(`/api/session/${encodeURIComponent(last)}/messages`).then(r=>r.json()).then(j=>{
      if(j.messages && j.messages.length){
        history=j.messages.map(m=>({role:m.role, text:m.text}));
        render();
      }
    }).catch(()=>{});
  }
  render();
  autoSize();
  syncLayout();
})();
</script>
</body>
</html>
"""
