HTML = r"""<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,maximum-scale=1">
<title>Antigravity Web</title>
<meta name="color-scheme" content="dark">
<style>
*{box-sizing:border-box}
:root{--bg:#09090b;--panel:#111113;--panel2:#18181b;--line:#27272a;--line2:#3f3f46;--muted:#71717a;--sub:#a1a1aa;--text:#fafafa;--acc:#fafafa;--radius:16px;--radius2:12px;--composer-h:180px}
html,body{height:100%}
body{margin:0;font:14px/1.6 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;color:var(--text);background:var(--bg);-webkit-font-smoothing:antialiased}
a{color:#38bdf8;text-decoration:none}
a:hover{text-decoration:underline}
button,select,textarea{font:inherit}
*:focus-visible{outline:2px solid #52525b;outline-offset:2px}
header{position:sticky;top:0;z-index:20;background:rgba(9,9,11,.88);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.hdr{max-width:880px;margin:0 auto;padding:7px 14px;display:flex;gap:10px;align-items:center;flex-wrap:nowrap;min-width:0}
.brand{display:flex;align-items:center;gap:9px;min-width:0;flex:0 1 auto;overflow:hidden}
.logo-ans{line-height:0;flex:0 0 auto}
.logo-ans pre{margin:0;font:4px/4px ui-monospace,Menlo,monospace;white-space:pre;display:block}
.brand b{font-size:13.5px;letter-spacing:-.2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ver{font-size:9px;color:var(--muted);border:1px solid var(--line);padding:2px 6px;border-radius:999px;background:rgba(255,255,255,.02);font-family:ui-monospace,Menlo,monospace;white-space:nowrap;flex:0 0 auto}
.badge{font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);padding:3px 7px;border-radius:999px;background:rgba(255,255,255,.02)}
.controls{display:flex;gap:7px;align-items:center;flex-wrap:nowrap;margin-left:auto;flex:0 0 auto;min-width:0}
.controls label{font-size:10.5px;color:var(--muted);display:flex;align-items:center;gap:5px}
.controls select,.btn{appearance:none;background:var(--panel);color:var(--text);border:1px solid var(--line);border-radius:10px;padding:6px 9px;font-size:11.5px;line-height:1}
.controls select{min-width:0;max-width:180px}
.controls select:disabled{opacity:.45;cursor:not-allowed}
.btn{cursor:pointer;display:inline-flex;align-items:center;gap:6px;white-space:nowrap;flex:0 0 auto}
.btn:hover{border-color:var(--line2)}
.btn:active{transform:translateY(0.5px)}
.btn.primary{background:var(--acc);color:#09090b;border-color:var(--acc);font-weight:600}
.btn.primary:disabled{opacity:.45;cursor:not-allowed}
.btn.ghost{background:transparent}
.btn.danger{background:#7f1d1d;color:#fee2e2;border-color:#991b1b}
.btn.danger:hover{background:#991b1b}
#chat{max-width:880px;margin:0 auto;padding:18px 14px var(--composer-h,180px);min-height:calc(100vh - 56px);scroll-padding-bottom:var(--composer-h,180px)}
.empty{max-width:560px;margin:40px auto;padding:0}
.empty-card{border:1px solid var(--line);border-radius:18px;background:linear-gradient(180deg,rgba(24,24,27,.9),rgba(17,17,19,.6));padding:22px;text-align:center}
.empty-card h1{margin:0;font-size:18px;letter-spacing:-.3px}
.empty-card p{margin:6px 0 0;color:var(--sub);font-size:13px;line-height:1.5}
.suggestions{margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:8px;text-align:left}
@media(max-width:640px){.suggestions{grid-template-columns:1fr}}
.chip{border:1px solid var(--line);background:var(--panel);border-radius:12px;padding:10px 12px;cursor:pointer;text-align:left}
.chip:hover{border-color:var(--line2);background:var(--panel2)}
.chip b{font-size:12px;display:block}
.chip span{font-size:11px;color:var(--muted)}
.hint-row{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:14px}
.hint{font-size:11px;color:var(--muted);border:1px solid var(--line);padding:6px 9px;border-radius:999px;background:var(--panel)}
.msg{margin:14px 0;display:flex;gap:10px;min-width:0}
.msg .avatar{width:28px;height:28px;border-radius:999px;display:grid;place-items:center;font-size:11px;font-weight:700;flex:0 0 28px;margin-top:2px;border:1px solid var(--line)}
.user .avatar{background:#27272a;color:#fff}
.assistant .avatar{background:#fafafa;color:#09090b}
.bubble{flex:1;min-width:0;max-width:100%;padding:11px 13px;border-radius:16px;border:1px solid var(--line);word-break:break-word;overflow-wrap:anywhere;position:relative;overflow:hidden}
.user .bubble{background:var(--panel2);white-space:pre-wrap}
.assistant .bubble{background:#0f1115}
.bubble img{max-width:min(340px,100%);border-radius:12px;border:1px solid var(--line);display:block;margin-bottom:8px}
.bubble .md{white-space:normal;line-height:1.6}
.bubble .md{overflow:hidden}
.bubble .md p{margin:6px 0}
.bubble .md h1,.bubble .md h2,.bubble .md h3,.bubble .md h4{margin:12px 0 6px;font-weight:700;letter-spacing:-.2px;line-height:1.3}
.bubble .md h1{font-size:18px} .bubble .md h2{font-size:16px} .bubble .md h3{font-size:14px} .bubble .md h4{font-size:13px;color:var(--sub)}
.bubble .md ul,.bubble .md ol{margin:6px 0;padding-left:20px}
.bubble .md li{margin:3px 0}
.bubble .md blockquote{border-left:2px solid var(--line2);padding-left:10px;color:var(--sub);margin:8px 0;font-style:italic}
.bubble .md table{border-collapse:collapse;width:100%;max-width:100%;margin:8px 0;font-size:12px;display:block;overflow:auto}
.bubble .md th,.bubble .md td{border:1px solid var(--line);padding:6px 8px;text-align:left;white-space:nowrap}
.bubble .md th{background:var(--panel2);font-weight:600}
.bubble .md hr{border:0;border-top:1px solid var(--line);margin:10px 0}
.bubble .md pre{position:relative;background:#08080a;border:1px solid var(--line);padding:10px;border-radius:12px;overflow:auto;font:12px/1.5 ui-monospace,Menlo,monospace;white-space:pre;margin:8px 0;max-width:100%}
.bubble .md code{font:12px/1.5 ui-monospace,Menlo,monospace;background:#18181b;padding:1px 5px;border-radius:6px;border:1px solid var(--line)}
.bubble .md pre code{background:transparent;border:0;padding:0}
.bubble .md .copy-code{position:absolute;top:6px;right:6px;font-size:10px;padding:3px 7px;border-radius:7px;background:var(--panel);border:1px solid var(--line);color:var(--muted);cursor:pointer}
.bubble .md .copy-code:hover{color:var(--text);border-color:var(--line2)}
.bubble .md a{color:#38bdf8}
.bubble pre{margin:8px 0 0;background:#08080a;border:1px solid var(--line);padding:10px;border-radius:12px;overflow:auto;font:12px/1.5 ui-monospace,Menlo,monospace;white-space:pre}
.bubble code{font:12px/1.5 ui-monospace,Menlo,monospace;background:#18181b;padding:1px 5px;border-radius:6px;border:1px solid var(--line)}
.bubble .actions{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-start;align-items:center;position:relative;z-index:1}
.bubble .actions button{font-size:11px;padding:5px 10px;border-radius:8px;flex:0 0 auto;max-width:100%}
.bubble .actions button:active{transform:none}
.thinking{opacity:.75;font-style:italic;display:flex;align-items:center;gap:8px}
.dot{width:6px;height:6px;border-radius:999px;background:var(--muted);animation:pulse 1.1s infinite}
@keyframes pulse{0%,100%{opacity:.3}50%{opacity:1}}
.skeleton{height:10px;background:linear-gradient(90deg,var(--line) 25%,var(--panel2) 50%,var(--line) 75%);background-size:200% 100%;animation:shimmer 1.4s infinite;border-radius:6px;margin:7px 0}
.skeleton.w60{width:60%} .skeleton.w70{width:70%} .skeleton.w80{width:80%} .skeleton.w40{width:40%}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}
.meta{font-size:11px;color:var(--muted);margin-top:8px;display:flex;gap:7px;flex-wrap:wrap;align-items:center}
.meta span{border:1px solid var(--line);padding:3px 7px;border-radius:999px;background:var(--panel);display:inline-flex;align-items:center;gap:4px}
.meta .ok{color:#a3e635;border-color:#365314;background:#1a2e05}
.meta .err{color:#fca5a5;border-color:#7f1d1d;background:#450a0a}
#composer{position:fixed;bottom:0;left:0;right:0;z-index:15;background:rgba(9,9,11,.96);backdrop-filter:blur(12px);border-top:1px solid var(--line)}
.composer-inner{max-width:880px;margin:0 auto;padding:10px 14px 12px}
.drop-overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);backdrop-filter:blur(2px);display:none;place-items:center;z-index:30;padding:20px}
.drop-overlay.show{display:grid}
.drop-card{border:2px dashed #52525b;background:rgba(24,24,27,.9);border-radius:16px;padding:22px 18px;text-align:center;max-width:420px;width:100%}
#preview{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
#preview:empty{display:none}
.preview-card{display:flex;align-items:center;gap:10px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:6px 8px;min-width:0}
.preview-card img{height:52px;width:52px;object-fit:cover;border-radius:8px;border:1px solid var(--line);flex:0 0 52px}
.preview-meta{font-size:11px;color:var(--sub);line-height:1.3;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:180px}
.preview-meta b{color:var(--text);font-size:12px}
.composer-card{background:#101012;border:1px solid var(--line);border-radius:16px;padding:8px;display:flex;flex-direction:column;gap:8px;position:relative}
.composer-row{display:flex;gap:8px;align-items:flex-end}
#prompt{flex:1;min-height:44px;max-height:140px;resize:none;background:transparent;color:var(--text);border:0;padding:8px 4px;font:14px/1.5 ui-sans-serif,system-ui;outline:none}
#prompt::placeholder{color:var(--muted)}
.toolbar{display:flex;gap:8px;align-items:center;justify-content:space-between;flex-wrap:nowrap}
.toolbar-left{display:flex;gap:8px;align-items:center;min-width:0;flex:1 1 auto}
.toolbar-right{display:flex;gap:8px;align-items:center;flex:0 0 auto}
.counter{font-size:11px;color:var(--muted);white-space:nowrap;flex:0 0 auto}
button#send{padding:9px 16px;border-radius:12px;min-width:68px;justify-content:center;flex:0 0 auto}
.footer{max-width:880px;margin:6px auto 0;padding:0 14px 6px;font-size:10px;color:var(--muted);text-align:center;line-height:1.4;opacity:.85}
.footer a{color:var(--muted);text-decoration:underline;text-underline-offset:2px}
#slashMenu{position:absolute;bottom:100%;left:8px;right:8px;background:var(--panel);border:1px solid var(--line);border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,.4);max-height:240px;overflow:auto;display:none;z-index:5}
#slashMenu.on{display:block}
.slash-item{padding:8px 10px;display:flex;gap:8px;align-items:center;cursor:pointer;border-bottom:1px solid var(--line)}
.slash-item:last-child{border-bottom:0}
.slash-item:hover,.slash-item.active{background:var(--panel2)}
.slash-item b{font-size:12px;color:var(--text)}
.slash-item span{font-size:11px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.quota-badge{font-size:11px;color:var(--muted);border:1px solid var(--line);background:var(--panel);padding:4px 9px;border-radius:999px;display:inline-flex;gap:6px;align-items:center;min-width:0;max-width:240px;flex:0 1 auto;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.quota-badge b{color:var(--sub);font-weight:600}
#modelHint{max-width:160px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:inline-block}
#modelHint:empty{display:none}
@media(max-width:860px){
  .hdr{padding:7px 12px;gap:9px}
  .controls select{max-width:150px}
}
@media(max-width:640px){
  .hdr{padding:7px 10px;gap:7px;flex-wrap:wrap}
  .brand{gap:7px}
  .brand b{font-size:12.5px}
  .logo-ans pre{font:3.4px/3.4px ui-monospace,Menlo,monospace}
  .controls{width:100%;margin-left:0;gap:5px;flex-wrap:wrap}
  .controls label{font-size:9.5px}
  .controls select{max-width:none;flex:1 1 115px;font-size:10.5px;padding:5px 8px}
  .btn{padding:5px 8px;font-size:10.5px}
  #chat{padding:12px 10px var(--composer-h,180px)}
  .bubble{padding:10px 11px}
  .composer-inner{padding:7px 10px 9px}
  .toolbar{gap:5px}
  .quota-badge{max-width:40vw;padding:3px 7px;font-size:9.5px}
  #modelHint{display:none}
  .counter{font-size:9.5px}
  button#send{padding:7px 13px;min-width:58px}
  .footer{font-size:9px}
}
@media(max-width:380px){
  .logo-ans{display:none}
  .ver{display:none}
  .btn-label{display:none}
}
#sessionOverlay{position:fixed;inset:0;z-index:40;background:rgba(9,9,11,.97);backdrop-filter:blur(16px);display:none;overflow:auto}
#sessionOverlay.on{display:block}
.session-wrap{max-width:640px;margin:0 auto;padding:20px 14px 32px}
.session-head{display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:nowrap;min-width:0}
.session-head h1{margin:0;font-size:16px;letter-spacing:-.3px;white-space:nowrap}
.session-head p{margin:2px 0 0;color:var(--muted);font-size:12px}
.session-actions{display:flex;gap:6px;margin-left:auto;flex:0 0 auto}
.session-grid{display:grid;gap:6px}
.session-card{border:1px solid var(--line);background:var(--panel);border-radius:10px;padding:9px 10px;display:flex;gap:9px;align-items:center;cursor:pointer;transition:border-color .15s,background .15s;text-align:left;width:100%;min-width:0}
.session-card:hover{border-color:var(--line2);background:var(--panel2)}
.session-card.active{border-color:var(--line2);background:var(--panel2);box-shadow:inset 0 0 0 1px var(--line2)}
.session-icon{width:28px;height:28px;border-radius:7px;background:var(--panel2);border:1px solid var(--line);display:grid;place-items:center;font-size:11px;flex:0 0 28px}
.session-main{flex:1;min-width:0;overflow:hidden}
.session-main b{font-size:12px;line-height:1.3;display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.session-main span{font-size:11px;color:var(--sub);display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:1px;line-height:1.2}
.session-meta{font-size:10px;color:var(--muted);display:flex;gap:5px;flex-wrap:nowrap;margin-top:4px;align-items:center;overflow:hidden}
.session-meta i{font-style:normal;border:1px solid var(--line);padding:1px 5px;border-radius:999px;background:var(--panel2);font-size:9px;white-space:nowrap;flex:0 0 auto}
.session-empty{border:1px dashed var(--line);border-radius:10px;padding:20px;text-align:center;color:var(--muted);font-size:13px}
.session-empty b{color:var(--text)}
</style>
<header>
  <div class="hdr">
    <div class="brand"><div class="logo-ans"><pre>         <span style="color:rgb(154,159,53)">▄</span><span style="color:rgb(189,171,65);background:rgb(186,143,36)">▄</span><span style="color:rgb(198,146,68);background:rgb(228,143,46)">▄</span><span style="color:rgb(212,120,70);background:rgb(234,113,53)">▄</span><span style="color:rgb(227,97,68);background:rgb(198,75,48)">▄</span><span style="color:rgb(195,67,54)">▄</span>
        <span style="color:rgb(106,161,87)">▄</span><span style="color:rgb(113,178,116);background:rgb(148,185,88)">▄</span><span style="color:rgb(109,164,130);background:rgb(148,168,95)">▄</span><span style="color:rgb(118,147,137);background:rgb(159,148,99)">▄</span><span style="color:rgb(140,130,135);background:rgb(180,126,97)">▄</span><span style="color:rgb(168,112,122);background:rgb(202,105,89)">▄</span><span style="color:rgb(196,96,106);background:rgb(223,87,79)">▄</span><span style="color:rgb(176,68,74)">▄</span>
       <span style="color:rgb(45,91,69)">▄</span><span style="color:rgb(77,171,155);background:rgb(100,182,126)">▄</span><span style="color:rgb(65,159,180);background:rgb(84,169,148)">▄</span><span style="color:rgb(60,149,199);background:rgb(78,157,166)">▄</span><span style="color:rgb(63,141,210);background:rgb(84,144,177)">▄</span><span style="color:rgb(75,133,210);background:rgb(102,132,175)">▄</span><span style="color:rgb(98,126,200);background:rgb(130,119,163)">▄</span><span style="color:rgb(127,116,182);background:rgb(162,106,143)">▄</span><span style="color:rgb(157,107,159);background:rgb(191,94,121)">▄</span>
       <span style="color:rgb(58,158,184);background:rgb(57,134,128)">▄</span><span style="color:rgb(53,150,210);background:rgb(62,160,184)">▄</span><span style="color:rgb(50,142,228);background:rgb(54,149,207)">▄</span><span style="color:rgb(49,137,240);background:rgb(51,142,224)">▄</span><span style="color:rgb(49,135,246);background:rgb(53,138,233)">▄</span><span style="color:rgb(53,134,247);background:rgb(60,134,234)">▄</span><span style="color:rgb(62,133,244);background:rgb(75,130,228)">▄</span><span style="color:rgb(76,131,237);background:rgb(97,126,215)">▄</span><span style="color:rgb(97,129,225);background:rgb(124,120,197)">▄</span><span style="color:rgb(118,124,207);background:rgb(111,86,136)">▄</span>
      <span style="color:rgb(29,96,139)">▄</span><span style="color:rgb(47,142,228);background:rgb(51,149,209)">▄</span><span style="color:rgb(48,137,242);background:rgb(50,142,229)">▄</span><span style="color:rgb(35,97,180);background:rgb(49,137,242)">▄</span><span style="background:rgb(45,124,230)">▄</span><span style="background:rgb(32,89,168)">▄</span><span style="background:rgb(34,90,169)">▄</span><span style="background:rgb(51,125,234)">▄</span><span style="color:rgb(43,101,188);background:rgb(64,135,249)">▄</span><span style="color:rgb(66,137,251);background:rgb(78,135,243)">▄</span><span style="color:rgb(79,138,247);background:rgb(96,135,234)">▄</span><span style="color:rgb(56,86,151)">▄</span>
      <span style="color:rgb(44,138,237);background:rgb(40,135,214)">▄</span><span style="color:rgb(46,135,247);background:rgb(46,138,240)">▄</span><span style="background:rgb(42,118,218)">▄</span>      <span style="background:rgb(53,122,227)">▄</span><span style="color:rgb(59,136,253);background:rgb(67,138,252)">▄</span><span style="color:rgb(66,138,252);background:rgb(71,129,232)">▄</span>
     <span style="color:rgb(45,136,243);background:rgb(35,113,192)">▄</span><span style="color:rgb(44,127,236);background:rgb(46,136,244)">▄</span><span style="background:rgb(34,97,181)">▄</span>        <span style="background:rgb(41,102,192)">▄</span><span style="color:rgb(51,129,243);background:rgb(59,136,253)">▄</span><span style="color:rgb(57,135,253);background:rgb(49,107,198)">▄</span>
   <span style="color:rgb(41,120,218)">▄</span><span style="color:rgb(44,125,231);background:rgb(43,130,232)">▄</span><span style="background:rgb(46,132,244)">▄</span>            <span style="background:rgb(51,132,251)">▄</span><span style="color:rgb(47,125,238);background:rgb(51,126,238)">▄</span><span style="color:rgb(41,109,207)">▄</span></pre></div><b>Antigravity Web</b><span class="ver" id="verBadge">—</span></div>
     <div class="controls">
      <label>Model <select id="model" title="Model"></select></label>
      <label>Effort <select id="effort" title="Effort"><option value="">auto</option><option value="low">low</option><option value="medium" selected>medium</option><option value="high">high</option></select></label>
      <button id="clearBtn" class="btn ghost" title="New chat">New chat</button>
    </div>
  </div>
</header>
<div id="chat" role="log" aria-live="polite" aria-label="Chat history"></div>
<div id="composer">
  <div class="composer-inner">
    <div id="preview"></div>
    <div class="composer-card">
      <div id="slashMenu" role="listbox" aria-label="Slash commands"></div>
      <div class="composer-row">
        <textarea id="prompt" rows="1" placeholder="Ask anything…  Enter to send • Shift+Enter for newline" aria-label="Prompt"></textarea>
      </div>
      <div class="toolbar">
        <div class="toolbar-left">
          <button id="attachBtn" class="btn" type="button" title="Attach photo (jpg/png/webp, max 10MB)" aria-label="Attach photo">📎 Attach</button>
          <input id="file" type="file" accept="image/*,.jpg,.jpeg,.png,.webp" style="display:none">
          <span class="quota-badge" id="quotaBadge" title="quota — click to refresh" role="status">—</span>
        </div>
        <div class="toolbar-right">
          <span class="counter" id="counter" aria-live="polite"></span>
          <span class="counter" id="modelHint" title="active model"></span>
          <button id="sessionsBtn2" class="btn ghost" title="Sessions" aria-label="Sessions">Sessions</button>
          <button id="send" class="btn primary" type="button" aria-label="Send prompt">Send</button>
        </div>
      </div>
    </div>
  </div>
  <div class="footer">Local session • nothing stored on server • attach via 📎, paste, or drag & drop • <a href="#" id="aboutLink">About</a></div>
</div>
<div id="dropOverlay" class="drop-overlay" aria-hidden="true"><div class="drop-card"><b>Drop photo to attach</b><div style="color:var(--sub);font-size:13px;margin-top:4px">jpg / png / webp • max 10MB</div></div></div>
<div id="sessionOverlay" aria-hidden="true"><div class="session-wrap">
  <div class="session-head">
    <div style="display:flex;align-items:center;gap:8px;min-width:0;flex:1 1 auto;overflow:hidden">
      <div class="logo-ans" style="flex:0 0 auto;transform:scale(0.7);transform-origin:left center;margin:-6px 0"><pre>         <span style="color:rgb(154,159,53)">▄</span><span style="color:rgb(189,171,65);background:rgb(186,143,36)">▄</span><span style="color:rgb(198,146,68);background:rgb(228,143,46)">▄</span><span style="color:rgb(212,120,70);background:rgb(234,113,53)">▄</span><span style="color:rgb(227,97,68);background:rgb(198,75,48)">▄</span><span style="color:rgb(195,67,54)">▄</span></pre></div>
      <div style="min-width:0"><b style="font-size:13px;letter-spacing:-.2px;display:block;line-height:1.1">Sessions</b><span style="font-size:11px;color:var(--muted);display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">Resume via --conversation</span></div>
    </div>
    <div class="session-actions">
      <button id="newSessionBtn" class="btn primary" style="padding:6px 10px;font-size:12px">+ New</button>
      <button id="closeSessionsBtn" class="btn ghost" style="padding:6px 10px">Close</button>
    </div>
  </div>
  <div id="sessionList" class="session-grid"></div>
</div></div>
<script>
const chatEl=document.getElementById('chat'), promptEl=document.getElementById('prompt'), fileEl=document.getElementById('file'), attachBtn=document.getElementById('attachBtn'), modelEl=document.getElementById('model'), effortEl=document.getElementById('effort'), previewEl=document.getElementById('preview'), modelHint=document.getElementById('modelHint'), counterEl=document.getElementById('counter'), dropOverlay=document.getElementById('dropOverlay'), quotaBadge=document.getElementById('quotaBadge'), slashMenu=document.getElementById('slashMenu'), verBadge=document.getElementById('verBadge'), sendBtn=document.getElementById('send');
let pendingImage=null;
let history=[];
let modelCache=[];
let currentAbort=null;
let currentConversation=null;
let sessionCache=[];
function cidKey(id){ return `agy_web_history:${id||'local'}`; }
function loadHistory(){ const cid=currentConversation; const raw=localStorage.getItem(cidKey(cid)); try{ return raw?JSON.parse(raw):[]; }catch(e){ return []; } }
function saveHistory(){ if(currentConversation) localStorage.setItem(cidKey(currentConversation), JSON.stringify(history.slice(-100))); else localStorage.setItem('agy_web_history', JSON.stringify(history.slice(-100))); localStorage.setItem('agy_web_last_cid', currentConversation||''); }

function esc(s){return String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;')}
function md(s){
  if(!s) return '<span class="hint" style="padding:0;border:0;background:transparent">—</span>';
  const blocks=[];
  let html=s.replace(/```([a-z0-9_-]*)\n?([\s\S]*?)```/gi, (m, lang, code)=>{
    const idx=blocks.length; blocks.push({lang:lang.trim(),code:code}); return `@@CODE${idx}@@`;
  });
  html=esc(html);
  html=html.replace(/`([^`]+?)`/g,'<code>$1</code>');
  html=html.replace(/^######\s+(.+)$/gm,'<h6>$1</h6>');
  html=html.replace(/^#####\s+(.+)$/gm,'<h5>$1</h5>');
  html=html.replace(/^####\s+(.+)$/gm,'<h4>$1</h4>');
  html=html.replace(/^###\s+(.+)$/gm,'<h3>$1</h3>');
  html=html.replace(/^##\s+(.+)$/gm,'<h2>$1</h2>');
  html=html.replace(/^#\s+(.+)$/gm,'<h1>$1</h1>');
  html=html.replace(/^\|(.+\|)\n\|[-:\s|]+\|\n((?:\|.+\|\n?)+)/gm,(m,hdr,rows)=>{
    const ths=hdr.split('|').slice(1,-1).map(c=>`<th>${esc(c.trim())}</th>`).join('');
    const trs=rows.trim().split('\n').map(r=>{
      const tds=r.split('|').slice(1,-1).map(c=>`<td>${esc(c.trim())}</td>`).join(''); return `<tr>${tds}</tr>`;
    }).join('');
    return `<table><thead><tr>${ths}</tr></thead><tbody>${trs}</tbody></table>`;
  });
  html=html.replace(/\*\*\*(.+?)\*\*\*/g,'<b><i>$1</i></b>');
  html=html.replace(/\*\*(.+?)\*\*/g,'<b>$1</b>');
  html=html.replace(/__(.+?)__/g,'<b>$1</b>');
  html=html.replace(/(?<!\w)\*(?!\*)(.+?)(?<!\*)\*(?!\w)/g,'<i>$1</i>');
  html=html.replace(/(?<!\w)_(.+?)_(?!\w)/g,'<i>$1</i>');
  html=html.replace(/^&gt;\s+(.+)$/gm,'<blockquote>$1</blockquote>');
  html=html.replace(/^\s*---+\s*$/gm,'<hr>');
  html=html.replace(/((?:^[-*]\s+.+(?:\n|$))+)/gm,(m)=>{
    const items=m.trim().split('\n').map(l=>l.replace(/^[-*]\s+/,'').trim()).map(l=>`<li>${l}</li>`).join(''); return `<ul>${items}</ul>`;
  });
  html=html.replace(/((?:^\d+\.\s+.+(?:\n|$))+)/gm,(m)=>{
    const items=m.trim().split('\n').map(l=>l.replace(/^\d+\.\s+/,'' ).trim()).map(l=>`<li>${l}</li>`).join(''); return `<ol>${items}</ol>`;
  });
  html=html.replace(/(https?:\/\/[^\s<]+)/g,'<a href="$1" target="_blank" rel="noopener">$1</a>');
  html=html.replace(/@@CODE(\d+)@@/g,(m,idx)=>{
    const b=blocks[Number(idx)]; const ec=esc(b.code); const lang=b.lang?` data-lang="${esc(b.lang)}"`:''; return `<pre${lang}><code>${ec}</code><button class="copy-code" aria-label="Copy code">Copy</button></pre>`;
  });
  const parts=html.split(/\n{2,}/).map(b=>{
    b=b.trim(); if(!b) return '';
    if(/^<(h[1-6]|ul|ol|pre|blockquote|hr|table|p)/.test(b)) return b;
    if(b.includes('<pre')||b.includes('<table')||b.includes('<ul')||b.includes('<ol')||b.includes('<blockquote')||b.includes('<h')) return b;
    return `<p>${b.replace(/\n/g,'<br>')}</p>`;
  }).filter(Boolean);
  let out=parts.join('');
  if(!out.includes('<')) out=`<p>${html.replace(/\n/g,'<br>')}</p>`;
  return `<div class="md">${out}</div>`;
}
function syncLayout(){const c=document.getElementById('composer');const h=c?c.offsetHeight:180;document.documentElement.style.setProperty('--composer-h',(h+16)+'px')}
function autoSize(){promptEl.style.height='auto';promptEl.style.height=Math.min(promptEl.scrollHeight,140)+'px'; const len=promptEl.value.length; counterEl.textContent=len?`${len} chars`:''; syncLayout()}
promptEl.addEventListener('input',autoSize);
new ResizeObserver(syncLayout).observe(document.getElementById('composer'));
window.addEventListener('resize',syncLayout);

function render(){
  chatEl.innerHTML='';
  if(history.length===0){
    chatEl.innerHTML=`<div class="empty"><div class="empty-card"><h1>Start a conversation</h1><p>Chat with agy in your browser. Streaming, slash commands, and vision — all local.</p><div class="suggestions">
      <button class="chip" data-prompt="Explain this codebase in 5 bullets"><b>Explain codebase</b><span>5-bullet overview</span></button>
      <button class="chip" data-prompt="Review this file for bugs and over-engineering, be concise"><b>Review file</b><span>bugs + ponytail check</span></button>
      <button class="chip" data-prompt="Write a minimal Python HTTP server, stdlib only"><b>Minimal server</b><span>stdlib only</span></button>
      <button class="chip" data-prompt="Help me debug this error, suggest the smallest fix"><b>Debug error</b><span>smallest fix first</span></button>
    </div><div class="hint-row"><span class="hint">Enter = send</span><span class="hint">Shift+Enter = newline</span><span class="hint">Paste / drag photo</span><span class="hint">/ for commands</span></div></div></div>`;
    chatEl.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{promptEl.value=b.dataset.prompt;autoSize();promptEl.focus();});
    syncLayout(); return;
  }
  history.forEach((m,i)=>{
    const row=document.createElement('div');row.className='msg '+(m.role==='user'?'user':'assistant');
    const av=document.createElement('div');av.className='avatar';av.textContent=m.role==='user'?'You':'agy';av.style.fontSize=m.role==='user'?'10px':'9px';row.appendChild(av);
    const bub=document.createElement('div');bub.className='bubble';
    if(m.image){const img=document.createElement('img');img.src=m.image;img.loading='lazy';img.alt='attached image';bub.appendChild(img);}
    const txt=document.createElement('div');
    if(m.thinking){ txt.className='thinking'; txt.innerHTML='<span class="dot"></span> Thinking…<div style="flex:1;margin-left:8px;display:grid;gap:6px"><div class="skeleton w80"></div><div class="skeleton w60"></div><div class="skeleton w40"></div></div>'; }
    else if(m.role==='assistant'){ txt.innerHTML=md(m.text); }
    else{ txt.innerHTML=esc(m.text).replace(/\n/g,'<br>'); }
    bub.appendChild(txt);
    if(m.duration){
      const meta=document.createElement('div');meta.className='meta';meta.innerHTML=`<span>${Number(m.duration).toFixed(1)}s</span>${m.model?`<span>${esc(m.model)}</span>`:''}`; bub.appendChild(meta);
    }
    if(m.error){const er=document.createElement('div');er.className='meta';er.innerHTML=`<span class="err">Error: ${esc(m.error).slice(0,600)}</span>`; bub.appendChild(er);}
    if(m.role==='assistant' && !m.thinking){
      const acts=document.createElement('div');acts.className='actions';
      const cp=document.createElement('button');cp.className='btn';cp.textContent='Copy';cp.setAttribute('aria-label','Copy response');cp.onclick=()=>{navigator.clipboard.writeText(m.text);cp.textContent='Copied';setTimeout(()=>cp.textContent='Copy',1200)};
      acts.appendChild(cp);
      if(m.error){const rt=document.createElement('button');rt.className='btn';rt.textContent='Retry';rt.setAttribute('aria-label','Retry');rt.onclick=()=>{promptEl.value=history[i-1]?.text||'';autoSize();}; acts.appendChild(rt);}
      bub.appendChild(acts);
    }
    row.appendChild(bub); chatEl.appendChild(row);
  });
  window.scrollTo(0,document.body.scrollHeight);
  syncLayout();
}
function save(){ saveHistory(); localStorage.setItem('agy_web_model',modelEl.value); localStorage.setItem('agy_web_effort',effortEl.value); }
function isEffortModel(id){const l=(id||'').toLowerCase(); return l.includes('-high')||l.includes('-low')||l.includes('-medium');}
function syncEffortUI(){
  const has=isEffortModel(modelEl.value);
  effortEl.disabled=has;
  effortEl.title=has?'This model already includes effort (high/medium/low) — effort is ignored':'Choose reasoning effort';
  if(has) effortEl.value='';
}
async function loadModels(){
  try{
    const r=await fetch('/api/models');const j=await r.json(); modelCache=j.models||[]; modelEl.innerHTML='';
    modelCache.forEach(m=>{const o=document.createElement('option');o.value=m.id;o.textContent=m.label||m.id;modelEl.appendChild(o);});
    const saved=localStorage.getItem('agy_web_model'); if(saved) modelEl.value=saved;
    const savedEff=localStorage.getItem('agy_web_effort'); if(savedEff && !isEffortModel(modelEl.value)) effortEl.value=savedEff;
    syncEffortUI();
    modelHint.textContent=(modelEl.options[modelEl.selectedIndex]?.textContent||modelEl.value||'auto');
  }catch(e){modelHint.textContent='model: auto'}
}
modelEl.addEventListener('change',()=>{syncEffortUI();save();modelHint.textContent=(modelEl.options[modelEl.selectedIndex]?.textContent||modelEl.value||'auto')});
effortEl.addEventListener('change',()=>{save();});
loadModels();
fetch('/api/health').then(r=>r.json()).then(j=>{
  const v=j.version||''; if(verBadge) verBadge.textContent=v?`v${v}`:''; if(!v) verBadge.style.display='none';
}).catch(()=>{ if(verBadge) verBadge.style.display='none'; });
let quotaCache=null;
function renderQuota(groups){
  if(!groups||!groups.length){ quotaBadge.textContent='quota —'; quotaBadge.title='no quota data'; return; }
  const parts=[];
  for(const g of groups){
    for(const b of g.buckets){
      const name=b.name.replace(' Limit Remaining','');
      parts.push(`${g.name.split(' ')[0]} ${name}: ${b.used_pct}% used | ${b.avail_pct}% avail`);
    }
  }
  let tight=null;
  for(const g of groups) for(const b of g.buckets) if(!tight||b.avail_pct < tight.avail_pct) tight=b, tight.group=g.name;
  if(tight) quotaBadge.innerHTML=`<b>${tight.group.split(' ')[0]}</b> ${tight.used_pct}% used | ${tight.avail_pct}% avail`;
  quotaBadge.title = parts.join('  •  ') + ' • click to refresh';
  quotaBadge.dataset.ts=String(Date.now());
}
async function loadQuota(){
  try{
    const r=await fetch('/api/quota'); const j=await r.json(); quotaCache=j.groups||[];
    renderQuota(quotaCache);
  }catch(e){ quotaBadge.textContent='quota —'; }
}
loadQuota();
quotaBadge.onclick=loadQuota;
setInterval(loadQuota, 45000);
document.addEventListener('visibilitychange', ()=>{ if(!document.hidden) loadQuota(); });
let slashCommands=[];
async function loadSlash(){
  try{ const r=await fetch('/api/commands'); const j=await r.json(); slashCommands=j.commands||[]; }catch(e){}
}
loadSlash();
let slashActive=-1;
function showSlash(filter){
  if(!slashCommands.length||filter===''){ slashMenu.classList.remove('on'); return; }
  const q=filter.toLowerCase();
  const matched=slashCommands.filter(c=>c.name.toLowerCase().includes(q)).slice(0,12);
  if(!matched.length){ slashMenu.classList.remove('on'); return; }
  slashMenu.innerHTML='';
  matched.forEach((c,i)=>{
    const d=document.createElement('div'); d.className='slash-item'+(i===slashActive?' active':'');
    d.setAttribute('role','option'); d.setAttribute('aria-selected', i===slashActive?'true':'false');
    d.innerHTML=`<b>/${esc(c.name)}</b><span>${esc(c.description||'')}</span>`;
    d.onclick=()=>{ promptEl.value='/'+c.name+' '; autoSize(); slashMenu.classList.remove('on'); promptEl.focus(); slashActive=-1; };
    slashMenu.appendChild(d);
  });
  slashMenu.classList.add('on');
  slashMenu.setAttribute('aria-expanded','true');
}
promptEl.addEventListener('keydown', e=>{
  if(slashMenu.classList.contains('on')){
    if(e.key==='ArrowDown'){ e.preventDefault(); slashActive=Math.min(slashActive+1, slashMenu.children.length-1); [...slashMenu.children].forEach((el,i)=>el.classList.toggle('active',i===slashActive)); }
    else if(e.key==='ArrowUp'){ e.preventDefault(); slashActive=Math.max(slashActive-1,0); [...slashMenu.children].forEach((el,i)=>el.classList.toggle('active',i===slashActive)); }
    else if(e.key==='Enter' && slashActive>=0){ e.preventDefault(); slashMenu.children[slashActive].click(); }
    else if(e.key==='Escape'){ slashMenu.classList.remove('on'); slashActive=-1; slashMenu.setAttribute('aria-expanded','false'); }
  }
});
promptEl.addEventListener('input', ()=>{
  const v=promptEl.value;
  if(v.startsWith('/')){
    const m=v.slice(1).split(/\s/)[0];
    showSlash(m);
    slashActive=-1;
  } else slashMenu.classList.remove('on');
});
document.addEventListener('click', e=>{ if(!slashMenu.contains(e.target) && e.target!==promptEl) slashMenu.classList.remove('on'); });

// sessions overlay
const sessionOverlay=document.getElementById('sessionOverlay'), sessionList=document.getElementById('sessionList');
let shouldShowOverlayOnLoad=false;
function timeAgo(s){ try{ const d=new Date(s); const diff=(Date.now()-d)/1000; if(diff<60) return 'just now'; if(diff<3600) return Math.floor(diff/60)+'m ago'; if(diff<86400) return Math.floor(diff/3600)+'h ago'; if(diff<86400*7) return Math.floor(diff/86400)+'d ago'; return d.toLocaleDateString(); }catch(e){ return s; } }
function escAttr(s){ return String(s).replaceAll('"','&quot;'); }
async function loadSessions(){
  sessionList.innerHTML='<div class="session-empty"><div class="skeleton w80"></div><div class="skeleton w60" style="margin:8px auto;width:220px"></div></div>';
  try{
    const r=await fetch('/api/sessions'); const j=await r.json(); sessionCache=j.sessions||[];
    if(!sessionCache.length){ sessionList.innerHTML='<div class="session-empty"><b>No sessions yet</b><br>Start a new session to begin.</div>'; return; }
    sessionList.innerHTML='';
    for(const s of sessionCache){
      const isActive = s.id===currentConversation;
      const card=document.createElement('button'); card.className='session-card'+(isActive?' active':''); card.setAttribute('aria-label', `Resume ${s.title}`); card.dataset.id=s.id;
      const icon=document.createElement('div'); icon.className='session-icon'; icon.textContent=isActive?'●':'◷';
      const main=document.createElement('div'); main.className='session-main';
      main.innerHTML=`<b>${esc(s.title||s.preview||s.id.slice(0,8))}</b><span>${esc(s.preview||'')}</span><div class="session-meta"><i>${esc(String(s.steps))} steps</i><i>${esc(timeAgo(s.updated))}</i>${s.workspace?`<i>${esc(s.workspace)}</i>`:''}</div>`;
      card.appendChild(icon); card.appendChild(main);
      card.onclick=()=>resumeSession(s.id);
      sessionList.appendChild(card);
    }
  }catch(e){ sessionList.innerHTML=`<div class="session-empty"><span class="err">Failed to load sessions: ${esc(String(e))}</span></div>`; }
}
function showSessions(){ sessionOverlay.classList.add('on'); sessionOverlay.setAttribute('aria-hidden','false'); loadSessions(); }
function hideSessions(){ sessionOverlay.classList.remove('on'); sessionOverlay.setAttribute('aria-hidden','true'); }
async function resumeSession(id){
  currentConversation=id;
  localStorage.setItem('agy_web_last_cid', id);
  // try load messages from server (extracted), fallback to local history
  try{
    const r=await fetch(`/api/session/${encodeURIComponent(id)}/messages`); const j=await r.json();
    if(j.messages && j.messages.length){ history=j.messages.map(m=>({role:m.role, text:m.text})); saveHistory(); hideSessions(); render(); return; }
  }catch(e){}
  history=loadHistory(); hideSessions(); render();
}
function newSession(){
  currentConversation=null; localStorage.removeItem('agy_web_last_cid'); history=[]; saveHistory(); hideSessions(); render();
}
document.getElementById('sessionsBtn2')?.addEventListener('click', showSessions);
document.getElementById('sessionsBtn')?.addEventListener('click', showSessions); // legacy header (removed) compat
document.getElementById('newSessionBtn')?.addEventListener('click', newSession);
document.getElementById('closeSessionsBtn')?.addEventListener('click', hideSessions);
document.getElementById('clearBtn')?.addEventListener('click', ()=>{ if(confirm('Start new chat? History will be cleared.')){ history=[]; saveHistory(); render(); }});
sessionOverlay?.addEventListener('click', e=>{ if(e.target===sessionOverlay) hideSessions(); });
 // init conversation from storage
(function initConversation(){
  const last=localStorage.getItem('agy_web_last_cid');
  if(last) currentConversation=last;
  history=loadHistory();
  // if no local history but last id exists, try server
  if(!history.length && last){ fetch(`/api/session/${encodeURIComponent(last)}/messages`).then(r=>r.json()).then(j=>{ if(j.messages&&j.messages.length){ history=j.messages.map(m=>({role:m.role,text:m.text})); render(); } }).catch(()=>{}); }
  // decide overlay on first load
  const hasAny = history.length>0;
  shouldShowOverlayOnLoad = !hasAny;
  // we defer showing until sessions loaded? Show immediately if no history
})();

function setPreview(){
  previewEl.innerHTML='';
  if(!pendingImage){ syncLayout(); return; }
  const card=document.createElement('div');card.className='preview-card';
  const img=document.createElement('img');img.src=pendingImage.dataUrl;card.appendChild(img);
  const meta=document.createElement('div');meta.className='preview-meta';
  const kb=Math.round((pendingImage.size||0)/1024);
  meta.innerHTML=`<b>${esc(pendingImage.name||'image')}</b><br>${esc(pendingImage.mime||'')} • ${kb} KB`;
  card.appendChild(meta);
  const rm=document.createElement('button');rm.className='btn';rm.textContent='Remove';rm.setAttribute('aria-label','Remove image');rm.onclick=()=>{pendingImage=null;setPreview();};
  card.appendChild(rm);
  previewEl.appendChild(card);
  syncLayout();
}
function handleFile(f){
  if(!f) return;
  if(!f.type.startsWith('image/')){alert('Only jpg/png/webp images');return}
  if(f.size>10*1024*1024){alert('Max 10MB');return}
  const fr=new FileReader(); fr.onload=()=>{pendingImage={dataUrl:fr.result, base64:fr.result.split(',')[1], mime:f.type||'image/jpeg', name:f.name, size:f.size}; setPreview(); promptEl.focus();}; fr.readAsDataURL(f);
}
attachBtn.onclick=()=>fileEl.click();
fileEl.onchange=()=>{const f=fileEl.files[0]; handleFile(f); fileEl.value='';};
window.addEventListener('paste',e=>{
  const items=e.clipboardData?.items; if(!items) return;
  for(const it of items){ if(it.type.startsWith('image/')){ const f=it.getAsFile(); if(!f) continue; const fr=new FileReader(); fr.onload=()=>{pendingImage={dataUrl:fr.result, base64:fr.result.split(',')[1], mime:it.type, name:'paste.'+(it.type.split('/')[1]||'png'), size:f.size}; setPreview();}; fr.readAsDataURL(f); e.preventDefault(); break; }}
});
let dragDepth=0;
window.addEventListener('dragenter',e=>{e.preventDefault();dragDepth++;dropOverlay.classList.add('show')});
window.addEventListener('dragover',e=>{e.preventDefault()});
window.addEventListener('dragleave',e=>{e.preventDefault();dragDepth=Math.max(0,dragDepth-1);if(dragDepth===0)dropOverlay.classList.remove('show')});
window.addEventListener('drop',e=>{e.preventDefault();dragDepth=0;dropOverlay.classList.remove('show');const f=e.dataTransfer?.files?.[0]; if(f) handleFile(f);});
dropOverlay.addEventListener('click',()=>dropOverlay.classList.remove('show'));
function setStreaming(on){
  if(on){ sendBtn.textContent='Stop'; sendBtn.classList.remove('primary'); sendBtn.classList.add('danger'); sendBtn.dataset.mode='stop'; sendBtn.setAttribute('aria-label','Stop generation'); promptEl.disabled=true; attachBtn.disabled=true; }
  else{ sendBtn.textContent='Send'; sendBtn.classList.add('primary'); sendBtn.classList.remove('danger'); delete sendBtn.dataset.mode; sendBtn.setAttribute('aria-label','Send prompt'); promptEl.disabled=false; attachBtn.disabled=false; promptEl.focus(); }
}
async function send(){
  if(sendBtn.dataset.mode==='stop' && currentAbort){ currentAbort.abort(); return; }
  const text=promptEl.value.trim(); if(!text && !pendingImage) return;
  const userMsg={role:'user', text: text||'(photo)', image: pendingImage?pendingImage.dataUrl:null};
  history.push(userMsg); render(); save();
  promptEl.value=''; autoSize(); const imgToSend=pendingImage; pendingImage=null; setPreview();
  const th={role:'assistant', text:'', thinking:true}; history.push(th); render();
  setStreaming(true);
  const eff = effortEl.disabled ? '' : effortEl.value;
  const body={prompt:text, model:modelEl.value, effort:eff, conversation_id: currentConversation||''};
  if(imgToSend) body.image={data:imgToSend.base64, mime:imgToSend.mime, name:imgToSend.name};
  const t0=performance.now();
  currentAbort=new AbortController();
  let fullText=''; let usage=null; let duration=null; let gotFirst=false;
  let textEl=null; let bubbleEl=null;
  let toolLog=[];
  try{
    const lastRow=chatEl.lastElementChild;
    if(lastRow){ bubbleEl=lastRow.querySelector('.bubble'); textEl=bubbleEl.querySelector('div'); }
    const r=await fetch('/api/chat_stream',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),signal:currentAbort.signal});
    if(!r.ok){ const txt=await r.text(); throw new Error(txt.slice(0,600)||r.statusText); }
    const reader=r.body.getReader(); const dec=new TextDecoder(); let buf='';
    function renderThinking(){
      if(!textEl) return;
      const items=toolLog.slice(-4).map(to=>`<div style="display:flex;gap:6px;align-items:center;font-size:11px;color:var(--sub);margin:3px 0"><span style="width:6px;height:6px;border-radius:999px;background:${to.state==='DONE'?'#22c55e':'var(--muted)'};display:inline-block;flex:0 0 6px"></span><span style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:260px">${esc(to.name)}${to.summary?' · '+esc(to.summary.slice(0,55)):''}</span></div>`).join('');
      const dot='<span class="dot"></span> Thinking…';
      textEl.innerHTML = toolLog.length ? `<div style="display:flex;align-items:center;gap:8px">${dot}</div><div style="margin-top:6px;border-left:2px solid var(--line);padding-left:8px">${items}</div><div style="margin-top:8px"><div class="skeleton w70"></div></div>` : `${dot}<div style="flex:1;margin-left:8px;display:grid;gap:6px"><div class="skeleton w80"></div><div class="skeleton w60"></div><div class="skeleton w40"></div></div>`;
      textEl.className='thinking';
    }
    while(true){
      const {value,done}=await reader.read(); if(done) break;
      buf+=dec.decode(value,{stream:true});
      const lines=buf.split('\n'); buf=lines.pop();
      for(const line of lines){
        if(!line.trim()) continue;
        let j; try{j=JSON.parse(line)}catch(e){continue}
        if(j.t==='tool'){
          toolLog.push({name:j.name, summary:j.summary||'', state:j.state});
          if(toolLog.length>12) toolLog.shift();
          if(!gotFirst) renderThinking();
        } else if(j.t==='tool_out'){
          if(toolLog.length) toolLog[toolLog.length-1].summary = (toolLog[toolLog.length-1].summary + ' → ' + String(j.output).slice(0,45)).slice(0,85);
          if(!gotFirst) renderThinking();
        } else if(j.t==='delta'){
          if(!gotFirst){ gotFirst=true; if(textEl){textEl.className=''; textEl.innerHTML='';} }
          fullText+=j.d;
          history[history.length-1].text=fullText;
          history[history.length-1].thinking=false;
          if(textEl){ textEl.innerHTML=md(fullText); }
          window.scrollTo(0,document.body.scrollHeight);
        } else if(j.t==='done'){
          fullText=j.response||fullText;
          usage=j.usage; duration=j.duration||((performance.now()-t0)/1000);
          if(j.conversation_id && !currentConversation){ currentConversation=j.conversation_id; localStorage.setItem('agy_web_last_cid', currentConversation); }
          history[history.length-1].text=fullText; history[history.length-1].usage=usage; history[history.length-1].duration=duration;
          history[history.length-1].thinking=false;
          if(j.status==='ERROR') history[history.length-1].error=j.error||'agy error';
          if(textEl) textEl.innerHTML=md(fullText);
        } else if(j.t==='cmd'){
        } else if(j.t==='error'){
          history[history.length-1].error=j.error;
        }
      }
    }
    if(!gotFirst && fullText){ if(textEl) textEl.innerHTML=md(fullText); }
    // fallback if no done
    if(!usage && fullText) duration=((performance.now()-t0)/1000);
    history[history.length-1].duration=history[history.length-1].duration||duration;
    history[history.length-1].thinking=false;
    render(); save(); loadQuota();
  }catch(e){
    history.pop();
    if(e.name==='AbortError'){ history.push({role:'assistant', text:fullText||'(stopped)', error:'stopped by user', duration:((performance.now()-t0)/1000)}); }
    else{ history.push({role:'assistant', text:fullText||'Request failed', error:String(e).slice(0,600)}); }
    render(); save();
  }finally{
    setStreaming(false); currentAbort=null; autoSize(); syncLayout();
  }
}
sendBtn.onclick=send;
promptEl.addEventListener('keydown',e=>{ if(e.key==='Enter' && !e.shiftKey){ e.preventDefault(); send(); }});
// clear handled above via sessions-aware handler
document.getElementById('aboutLink').onclick=(e)=>{e.preventDefault();alert('Antigravity Web — local browser UI for agy CLI.\n\n• Streaming via stream-json, slash commands, markdown\n• Stop to abort generation\n• Runs on localhost, images as @/tmp/...\n• History in localStorage')};
chatEl.addEventListener('click', e=>{ const b=e.target.closest('.copy-code'); if(b){ const code=b.previousElementSibling.textContent; navigator.clipboard.writeText(code); b.textContent='Copied'; setTimeout(()=>b.textContent='Copy',1200); }});
render(); autoSize(); syncLayout();
if(shouldShowOverlayOnLoad){ setTimeout(()=>{ fetch('/api/sessions').then(r=>r.json()).then(j=>{ if(j.sessions && j.sessions.length) showSessions(); }).catch(()=>{}); }, 300); }
</script>
</html>
"""
