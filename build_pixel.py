from pathlib import Path

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
<title>VirtualCompany - Pixel Office</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Courier New', monospace;
    background: #0b0f14;
    color: #c9d1d9;
    min-height: 100vh;
    padding-bottom: 40px;
  }
  header {
    padding: 18px;
    background: #0d1117;
    border-bottom: 1px solid #1f2937;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 10;
  }
  .brand {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 4px;
    color: #5af78e;
    text-shadow: 0 0 6px rgba(90,247,142,0.35);
    text-transform: uppercase;
  }
  .sub { font-size: 11px; color: #8b949e; letter-spacing: 2px; margin-top: 4px; }
  main { padding: 16px; }

  .office {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    max-width: 960px;
    margin: 0 auto 24px;
  }
  .desk {
    background: #0d1117;
    border: 2px solid #1f2937;
    border-radius: 8px;
    padding: 12px;
    position: relative;
    transition: transform 120ms ease, border-color 120ms ease, box-shadow 120ms ease;
    image-rendering: pixelated;
  }
  .desk:hover {
    transform: translateY(-3px);
    border-color: #5af78e;
    box-shadow: 0 12px 30px rgba(90,247,142,0.18);
    z-index: 2;
  }
  .pixel-char {
    width: 56px;
    height: 56px;
    margin: 0 auto 8px;
    background: #161b22;
    border-radius: 6px;
    image-rendering: pixelated;
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-template-rows: repeat(8, 1fr);
    padding: 3px;
    gap: 1px;
  }
  .px { width: 100%; height: 100%; border-radius: 1px; }
  .px.on { background: currentColor; }
  .px.off { background: transparent; }

  .name { font-size: 12px; font-weight: 700; color: #f0f6fc; text-align: center; }
  .role { font-size: 10px; color: #8b949e; text-align: center; margin-top: 2px; }

  .desk::after {
    content: attr(data-tip);
    position: absolute;
    bottom: 98%;
    left: 50%;
    transform: translateX(-50%) scale(0.88);
    background: #010409;
    color: #c9d1d9;
    border: 1px solid #30363d;
    padding: 10px 12px;
    border-radius: 10px;
    font-size: 12px;
    line-height: 1.45;
    width: 220px;
    pointer-events: none;
    opacity: 0;
    transition: all 120ms ease;
    z-index: 5;
    box-shadow: 0 8px 18px rgba(0,0,0,0.45);
  }
  .desk:hover::after { opacity: 1; transform: translateX(-50%) scale(1); }

  .terminal {
    background: #010409;
    border: 1px solid #1f2937;
    border-radius: 12px;
    padding: 14px;
    max-width: 960px;
    margin: 0 auto;
    min-height: 280px;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.03);
  }
  .terminal-head { display: flex; gap: 6px; margin-bottom: 12px; }
  .dot { width: 10px; height: 10px; border-radius: 50%; }
  .dot.red { background:#ff5f57; } .dot.yel { background:#febc2e; } .dot.grn { background:#28c840; }
  .log { font-size: 12px; line-height: 1.75; margin-bottom: 6px; word-break: break-word; }
  .ts { color: #6e7681; margin-right: 8px; }
  .sys { color: #58a6ff; }
  .own { color: #f0f6fc; }
  .bot { color: #d2a8ff; }

  .controls { display:flex; gap:10px; max-width:960px; margin:14px auto 0; }
  .controls input {
    flex: 1;
    background:#0d1117;
    color:#c9d1d9;
    border:1px solid #1f2937;
    border-radius:8px;
    padding:10px 12px;
    font-family: inherit;
    outline:none;
  }
  .controls button {
    background:#5af78e;
    color:#010409;
    border:none;
    border-radius:8px;
    padding:10px 14px;
    font-weight:800;
    cursor:pointer;
    letter-spacing:1px;
  }
</style>
</head>
<body>
<header>
  <div class="brand">🏢 VirtualCompany</div>
  <div class="sub">PIXEL OFFICE // AUTONOMOUS WORKFORCE</div>
</header>
<main>
  <div class="office" id="office"></div>
  <div class="terminal">
    <div class="terminal-head">
      <div class="dot red"></div><div class="dot yel"></div><div class="dot grn"></div>
    </div>
    <div id="term">
      <div class="log sys"><span class="ts">SYS</span>Welcome. Hover over pixel staff to see what they are doing or thinking. Click a desk to open terminal.</div>
    </div>
    <div class="controls">
      <input type="text" id="inp" placeholder="> send message to selected agent">
      <button onclick="send()">SEND</button>
    </div>
  </div>
</main>
<script>
const AGENTS = {
  "CEO-01": {"name":"CEO-01","title":"Chief Strategist","color":"#5af78e","status":"planning","thought":"Focus: Q3 expansion","work_log":["Reviewed Q3 financials","Delegated expansion plan","Analyzed market data","Updated CEO KPI dashboard"]},
  "MGR-SALES": {"name":"MGR-SALES","title":"Sales Manager","color":"#ffd166","status":"leading","thought":"Pipeline looks strong today","work_log":["Closed 2 enterprise deals","Reviewed team pipeline","Mentored S-01 on negotiation","Updated CRM reports"]},
  "MGR-OPS": {"name":"MGR-OPS","title":"Operations Manager","color":"#4cc9f0","status":"optimizing","thought":"Need to cut delivery lag","work_log":["Reduced delivery SLA by 12%","Resolved vendor dispute","Audited warehouse costs","Pushed SOP v3.2"]},
  "MGR-TECH": {"name":"MGR-TECH","title":"Technology Manager","color":"#c084fc","status":"shipping","thought":"Bandwidth is stable online","work_log":["Deployed hotfix to prod","Reviewed T-01 PRs","Updated infra cost report","Shipped v2.17.4"]},
  "S-01": {"name":"S-01","title":"Sales Executive","color":"#ff7b72","status":"calling","thought":"36% hit rate in this hour","work_log":["Called 32 prospects","Sent follow-up emails","Prepared demo for LeadX","Submitted monthly forecast"]},
  "S-02": {"name":"S-02","title":"Sales Executive","color":"#ff9e64","status":"follow_up","thought":"3 proposals pending review","work_log":["Followed up 18 leads","Booked 4 meetings","Updated CRM data","Shared proposal template"]},
  "O-01": {"name":"O-01","title":"Operations Executive","color":"#7dd3fc","status":"logistics","thought":"Route B is tracking fast","work_log":["Processed 24 orders","Updated shipment tracking","Resolved delivery exception","Compiled daily ops report"]},
  "T-01": {"name":"T-01","title":"Tech Executive","color":"#d8b4fe","status":"coding","thought":"Refactor DB layer offline","work_log":["Fixed login timeout bug","Reduced API latency by 18%","Wrote unit tests","Pushed commit to staging"]}
};

const PIXEL_MAP = {
  CEO: [1,1,1,1,1,1,1,1,
        1,0,0,0,0,0,0,1,
        1,0,0,0,0,0,0,1,
        1,0,0,1,1,0,0,1,
        1,0,0,1,1,0,0,1,
        1,0,0,0,0,0,0,1,
        1,0,0,0,0,0,0,1,
        1,1,1,1,1,1,1,1],
  MGR: [1,1,1,1,1,1,1,1,
        1,0,0,0,0,0,0,1,
        1,0,1,1,1,1,0,1,
        1,0,1,0,0,1,0,1,
        1,0,1,0,0,1,0,1,
        1,0,1,1,1,1,0,1,
        1,0,0,0,0,0,0,1,
        0,0,0,0,0,0,0,0],
  EXEC: [0,0,0,1,1,0,0,0,
         0,0,1,1,1,1,0,0,
         0,1,1,0,0,1,1,0,
         0,1,0,0,0,0,1,0,
         0,1,0,0,0,0,1,0,
         0,1,1,0,0,1,1,0,
         0,0,1,1,1,1,0,0,
         0,0,0,1,1,0,0,0]
};

function resolveRole(title) {
  if (title.includes('Chief')) return 'CEO';
  if (title.includes('Manager')) return 'MGR';
  return 'EXEC';
}

function buildPixels(color, title) {
  const map = PIXEL_MAP[resolveRole(title)];
  const out = [];
  for (let i = 0; i < 64; i++) {
    const state = map[i] === 1 ? 'on' : 'off';
    out.push('<div class="px ' + state + '" style="color:' + color + '"></div>');
  }
  return out.join('');
}

function office() {
  const g = document.getElementById('office');
  g.innerHTML = '';
  for (const [k,a] of Object.entries(AGENTS)) {
    const el = document.createElement('div');
    el.className = 'desk';
    el.onclick = () => select(k);
    const tip = '<b>' + a.name + '</b><br>' + a.title + '<br>• Status: ' + a.status + '<br>• Thought: ' + a.thought;
    el.setAttribute('data-tip', tip);
    el.innerHTML = '<div class="pixel-char" style="color:' + a.color + '">' + buildPixels(a.color, a.title) + '</div><div class="name">' + a.name + '</div><div class="role">' + a.title + '</div>';
    g.appendChild(el);
  }
}

let current = null;
function select(k) {
  current = k;
  const a = AGENTS[k];
  document.getElementById('term').innerHTML = '';
  append('sys', 'Connected to ' + k + ' (' + a.title + ')');
  append('sys', '--- WORK LOG ---');
  a.work_log.slice(0,4).forEach(w => append('bot', w));
}

function append(cls, text) {
  const t = document.getElementById('term');
  const row = document.createElement('div');
  row.className = 'log ' + (cls || '');
  const ts = new Date().toLocaleTimeString('en-IN', {hour12:false});
  row.innerHTML = '<span class="ts">' + ts + '</span>' + text;
  t.appendChild(row);
  t.scrollTop = t.scrollHeight;
}

function send() {
  const inp = document.getElementById('inp');
  const msg = inp.value.trim();
  if (!msg) return;
  if (!current) { append('sys', 'Select a pixel staff member first by clicking their desk'); return; }
  append('own', '> ' + msg);
  inp.value = '';
  setTimeout(() => {
    const a = AGENTS[current];
    const reply = 'Ack: command `' + msg + '` processed by ' + current;
    append('bot', '<' + current + '> ' + reply);
  }, 400);
}

office();
</script>
</body>
</html>
'''

out = Path('/c/Users/Gatade/Desktop/VirtualCompany/virtual_company.html')
out.write_text(html, encoding='utf-8')
print('written', out.exists(), out.stat().st_size)
