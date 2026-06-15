# AnkiTabs
# Auto-generated AnkiTabs cloze add-on

from aqt import mw, gui_hooks

NOTE_TYPE_NAME = "AnkiTabs"

FRONT_TEMPLATE = """<div style="display:none">
  {{cloze:Definition}}{{cloze:Classification}}{{cloze:Histology}}{{cloze:Etiology}}{{cloze:Pathophysiology}}{{cloze:Epidemiology}}{{cloze:Risk Factors}}{{cloze:Symptoms}}{{cloze:Clinical Findings}}{{cloze:Investigation}}
  {{cloze:Diagnosis}}{{cloze:Management}}{{cloze:Admission}}{{cloze:Treatment}}{{cloze:Surgery}}{{cloze:Follow-up}}{{cloze:Prognosis}}
</div>

<div class="title">{{Disease}}</div>

<div class="tabs">
  <div class="tab-buttons">
    {{#Definition}}<div class="tab-btn" data-tab="bak">Definition</div>{{/Definition}}
		{{#Classification}}<div class="tab-btn" data-tab="klass">Classification</div>{{/Classification}}
		{{#Histology}}<div class="tab-btn" data-tab="his">Histology</div>{{/Histology}}
    {{#Etiology}}<div class="tab-btn" data-tab="eti">Etiology</div>{{/Etiology}}
    {{#Pathophysiology}}<div class="tab-btn" data-tab="pat">Pathophysiology</div>{{/Pathophysiology}}
    {{#Epidemiology}}<div class="tab-btn" data-tab="epi">Epidemiology</div>{{/Epidemiology}}
    {{#Risk Factors}}<div class="tab-btn" data-tab="risk">Risk Factors</div>{{/Risk Factors}}
    {{#Symptoms}}<div class="tab-btn" data-tab="sym">Symptoms</div>{{/Symptoms}}
    {{#Clinical Findings}}<div class="tab-btn" data-tab="klin">Clinical Findings</div>{{/Clinical Findings}}
    {{#Investigation}}<div class="tab-btn" data-tab="utr">Investigation</div>{{/Investigation}}
    {{#Diagnosis}}<div class="tab-btn" data-tab="diag">Diagnosis</div>{{/Diagnosis}}
    {{#Management}}<div class="tab-btn" data-tab="hand">Management</div>{{/Management}}
    {{#Admission}}<div class="tab-btn" data-tab="inläg">Admission</div>{{/Admission}}
    {{#Treatment}}<div class="tab-btn" data-tab="beh">Treatment</div>{{/Treatment}}
    {{#Surgery}}<div class="tab-btn" data-tab="op">Surgery</div>{{/Surgery}}
    {{#Follow-up}}<div class="tab-btn" data-tab="uppf">Follow-up</div>{{/Follow-up}}
   {{#Prognosis}}<div class="tab-btn" data-tab="prog">Prognosis</div>{{/Prognosis}}
  </div>

  {{#Definition}}
  <div id="tab-bak" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Definition}}</div>
    <div class="content-raw" style="display:none">{{Definition}}</div>
  </div></div>
  {{/Definition}}

  {{#Classification}}
  <div id="tab-klass" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Classification}}</div>
    <div class="content-raw" style="display:none">{{Classification}}</div>
  </div></div>
  {{/Classification}}

  {{#Histology}}
  <div id="tab-his" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Histology}}</div>
    <div class="content-raw" style="display:none">{{Histology}}</div>
  </div></div>
  {{/Histology}}


  {{#Etiology}}
  <div id="tab-eti" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Etiology}}</div>
    <div class="content-raw" style="display:none">{{Etiology}}</div>
  </div></div>
  {{/Etiology}}

  {{#Pathophysiology}}
  <div id="tab-pat" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Pathophysiology}}</div>
    <div class="content-raw" style="display:none">{{Pathophysiology}}</div>
  </div></div>
  {{/Pathophysiology}}

  {{#Epidemiology}}
  <div id="tab-epi" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Epidemiology}}</div>
    <div class="content-raw" style="display:none">{{Epidemiology}}</div>
  </div></div>
  {{/Epidemiology}}

  {{#Risk Factors}}
  <div id="tab-risk" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Risk Factors}}</div>
    <div class="content-raw" style="display:none">{{Risk Factors}}</div>
  </div></div>
  {{/Risk Factors}}

  {{#Symptoms}}
  <div id="tab-sym" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Symptoms}}</div>
    <div class="content-raw" style="display:none">{{Symptoms}}</div>
  </div></div>
  {{/Symptoms}}

  {{#Clinical Findings}}
  <div id="tab-klin" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Clinical Findings}}</div>
    <div class="content-raw" style="display:none">{{Clinical Findings}}</div>
  </div></div>
  {{/Clinical Findings}}

  {{#Investigation}}
  <div id="tab-utr" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Investigation}}</div>
    <div class="content-raw" style="display:none">{{Investigation}}</div>
  </div></div>
  {{/Investigation}}

  {{#Diagnosis}}
  <div id="tab-diag" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Diagnosis}}</div>
    <div class="content-raw" style="display:none">{{Diagnosis}}</div>
  </div></div>
  {{/Diagnosis}}

  {{#Management}}
  <div id="tab-hand" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Management}}</div>
    <div class="content-raw" style="display:none">{{Management}}</div>
  </div></div>
  {{/Management}}

  {{#Admission}}
  <div id="tab-inläg" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Admission}}</div>
    <div class="content-raw" style="display:none">{{Admission}}</div>
  </div></div>
  {{/Admission}}

  {{#Treatment}}
  <div id="tab-beh" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Treatment}}</div>
    <div class="content-raw" style="display:none">{{Treatment}}</div>
  </div></div>
  {{/Treatment}}

  {{#Surgery}}
  <div id="tab-op" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Surgery}}</div>
    <div class="content-raw" style="display:none">{{Surgery}}</div>
  </div></div>
  {{/Surgery}}

  {{#Follow-up}}
  <div id="tab-uppf" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Follow-up}}</div>
    <div class="content-raw" style="display:none">{{Follow-up}}</div>
  </div></div>
  {{/Follow-up}}

  {{#Prognosis}}
  <div id="tab-prog" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Prognosis}}</div>
    <div class="content-raw" style="display:none">{{Prognosis}}</div>
  </div></div>
  {{/Prognosis}}

</div>

<script>
(function () {
  const $  = s => document.querySelector(s);
  const $$ = s => Array.from(document.querySelectorAll(s));

  const OPEN  = String.fromCharCode(123,123);
  const CLOSE = String.fromCharCode(125,125);
  const reCloze = new RegExp(OPEN + 'c\\\\d+::' + '([\\\\s\\\\S]*?)' + '(?:::[^}]+)?' + CLOSE, 'g');

  function stripClozeFromHTML(html) {
    if (!html) return '';
    return html.replace(reCloze, '$1');
  }

  function renderPanel(panelEl, mode) {
    const cont    = panelEl.querySelector('.panel-content');
    const clozeEl = cont.querySelector('.content-cloze');
    const rawEl   = cont.querySelector('.content-raw');
    if (!clozeEl || !rawEl) return;

    const clozeHTML = (clozeEl.innerHTML || '').trim();
    const rawHTML   = rawEl.innerHTML || '';

    if (mode === 'question') {
      cont.innerHTML = clozeHTML ? clozeHTML : stripClozeFromHTML(rawHTML);
    } else {
      cont.innerHTML = stripClozeFromHTML(rawHTML);
    }
  }

  // --- Autoscroll helpers ---
  const isMobile = () => window.matchMedia('(max-width: 640px)').matches;

  function ensureActiveTabVisible(smooth) {
    if (!isMobile()) return; // bara på mobil
    const container = document.querySelector('.tab-buttons');
    if (!container) return;
    const active = container.querySelector('.tab-btn.active') || container.querySelector('.tab-btn');
    if (!active) return;

    const cRect = container.getBoundingClientRect();
    const aRect = active.getBoundingClientRect();

    let delta = 0;
    if (aRect.left < cRect.left) {
      delta = aRect.left - cRect.left;       // skrolla vänster
    } else if (aRect.right > cRect.right) {
      delta = aRect.right - cRect.right;     // skrolla höger
    }
    if (delta !== 0) {
      container.scrollTo({
        left: container.scrollLeft + delta,
        behavior: smooth ? 'smooth' : 'auto'
      });
    }
  }

  // Kör efter layouten “satt sig” (dubbla rAF motverkar timing-problem i Anki)
  function queueEnsure(smooth) {
    requestAnimationFrame(() => {
      requestAnimationFrame(() => ensureActiveTabVisible(smooth));
    });
  }

  // --- Init + rendering ---
  const panels = $$('.tab-panel').map(el => ({ id: el.id.replace('tab-',''), el }));
  const btns   = $$('.tab-btn');

  // öppna den första panelen som faktiskt har cloze-innehåll, annars första
  let activeId = panels.length ? panels[0].id : '';
  for (const p of panels) {
    const c = p.el.querySelector('.content-cloze');
    if (c && (c.innerHTML || '').trim()) { activeId = p.id; break; }
  }

  function rerenderAll() {
    panels.forEach(p => {
      renderPanel(p.el, p.id === activeId ? 'question' : 'plain');
      p.el.classList.toggle('active', p.id === activeId);
    });
    btns.forEach(b => b.classList.toggle('active', b.dataset.tab === activeId));
    queueEnsure(false); // se till att aktiv flik syns efter varje render
  }

  rerenderAll();

  // klick för att byta aktiv flik
  btns.forEach(b => b.addEventListener('click', () => {
    activeId = b.dataset.tab;
    rerenderAll();
    queueEnsure(true);
  }));

  // Space / Enter → visa svaret på framsidan
  document.addEventListener('keydown', function(e){
    const k   = e.key || e.code;
    const tag = (document.activeElement && document.activeElement.tagName) || '';
    const isSpace = k === ' ' || k === 'Spacebar' || k === 'Space';
    const isEnter = k === 'Enter';
    const onBack  = !!document.getElementById('answer');
    if (!onBack && (isSpace || isEnter) &&
        !/^(INPUT|TEXTAREA|SELECT)$/.test(tag) &&
        typeof pycmd === 'function') {
      e.preventDefault();
      pycmd('ans');
    }
  }, {passive:false});

  // --- Håll autoscrollen vid liv i Anki ---
  // 1) Kör även direkt (för fall där DOMContentLoaded inte triggas i återanvänd webview)
  queueEnsure(false);

  // 2) Reagera på storleksändring/rotation
  window.addEventListener('resize', () => queueEnsure(false));

  // 3) När kortet blir synligt igen (t.ex. efter nästa/prev), säkra att rätt flik syns
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') queueEnsure(false);
  });

  // 4) MutationObserver: om Anki ändrar DOM (klass på knappar/paneler), scrolla igen
  const container = document.querySelector('.tab-buttons');
  if (container && 'MutationObserver' in window) {
    const mo = new MutationObserver(() => queueEnsure(false));
    mo.observe(container, {subtree: true, childList: true, attributes: true, attributeFilter: ['class']});
  }
})();
</script>
"""

BACK_TEMPLATE = """<div style="display:none">
  {{cloze:Definition}}{{cloze:Classification}}{{cloze:Histology}}{{cloze:Etiology}}{{cloze:Pathophysiology}}{{cloze:Epidemiology}}{{cloze:Risk Factors}}{{cloze:Symptoms}}{{cloze:Clinical Findings}}{{cloze:Investigation}}
  {{cloze:Diagnosis}}{{cloze:Management}}{{cloze:Admission}}{{cloze:Treatment}}{{cloze:Surgery}}{{cloze:Follow-up}}{{cloze:Prognosis}}
</div>

<div class="title">{{Disease}}</div>

<div class="tabs">
  <div class="tab-buttons">
    {{#Definition}}<div class="tab-btn" data-tab="bak">Definition</div>{{/Definition}}
		{{#Classification}}<div class="tab-btn" data-tab="klass">Classification</div>{{/Classification}}
		{{#Histology}}<div class="tab-btn" data-tab="his">Histology</div>{{/Histology}}
    {{#Etiology}}<div class="tab-btn" data-tab="eti">Etiology</div>{{/Etiology}}
    {{#Pathophysiology}}<div class="tab-btn" data-tab="pat">Pathophysiology</div>{{/Pathophysiology}}
    {{#Epidemiology}}<div class="tab-btn" data-tab="epi">Epidemiology</div>{{/Epidemiology}}
    {{#Risk Factors}}<div class="tab-btn" data-tab="risk">Risk Factors</div>{{/Risk Factors}}
    {{#Symptoms}}<div class="tab-btn" data-tab="sym">Symptoms</div>{{/Symptoms}}
    {{#Clinical Findings}}<div class="tab-btn" data-tab="klin">Clinical Findings</div>{{/Clinical Findings}}
    {{#Investigation}}<div class="tab-btn" data-tab="utr">Investigation</div>{{/Investigation}}
    {{#Diagnosis}}<div class="tab-btn" data-tab="diag">Diagnosis</div>{{/Diagnosis}}
    {{#Management}}<div class="tab-btn" data-tab="hand">Management</div>{{/Management}}
    {{#Admission}}<div class="tab-btn" data-tab="inläg">Admission</div>{{/Admission}}
    {{#Treatment}}<div class="tab-btn" data-tab="beh">Treatment</div>{{/Treatment}}
    {{#Surgery}}<div class="tab-btn" data-tab="op">Surgery</div>{{/Surgery}}
    {{#Follow-up}}<div class="tab-btn" data-tab="uppf">Follow-up</div>{{/Follow-up}}
   {{#Prognosis}}<div class="tab-btn" data-tab="prog">Prognosis</div>{{/Prognosis}}
  </div>

  {{#Definition}}
  <div id="tab-bak" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Definition}}</div>
    <div class="content-raw" style="display:none">{{Definition}}</div>
  </div></div>
  {{/Definition}}

  {{#Classification}}
  <div id="tab-klass" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Classification}}</div>
    <div class="content-raw" style="display:none">{{Classification}}</div>
  </div></div>
  {{/Classification}}

  {{#Histology}}
  <div id="tab-his" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Histology}}</div>
    <div class="content-raw" style="display:none">{{Histology}}</div>
  </div></div>
  {{/Histology}}


  {{#Etiology}}
  <div id="tab-eti" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Etiology}}</div>
    <div class="content-raw" style="display:none">{{Etiology}}</div>
  </div></div>
  {{/Etiology}}

  {{#Pathophysiology}}
  <div id="tab-pat" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Pathophysiology}}</div>
    <div class="content-raw" style="display:none">{{Pathophysiology}}</div>
  </div></div>
  {{/Pathophysiology}}

  {{#Epidemiology}}
  <div id="tab-epi" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Epidemiology}}</div>
    <div class="content-raw" style="display:none">{{Epidemiology}}</div>
  </div></div>
  {{/Epidemiology}}

  {{#Risk Factors}}
  <div id="tab-risk" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Risk Factors}}</div>
    <div class="content-raw" style="display:none">{{Risk Factors}}</div>
  </div></div>
  {{/Risk Factors}}

  {{#Symptoms}}
  <div id="tab-sym" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Symptoms}}</div>
    <div class="content-raw" style="display:none">{{Symptoms}}</div>
  </div></div>
  {{/Symptoms}}

  {{#Clinical Findings}}
  <div id="tab-klin" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Clinical Findings}}</div>
    <div class="content-raw" style="display:none">{{Clinical Findings}}</div>
  </div></div>
  {{/Clinical Findings}}

  {{#Investigation}}
  <div id="tab-utr" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Investigation}}</div>
    <div class="content-raw" style="display:none">{{Investigation}}</div>
  </div></div>
  {{/Investigation}}

  {{#Diagnosis}}
  <div id="tab-diag" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Diagnosis}}</div>
    <div class="content-raw" style="display:none">{{Diagnosis}}</div>
  </div></div>
  {{/Diagnosis}}

  {{#Management}}
  <div id="tab-hand" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Management}}</div>
    <div class="content-raw" style="display:none">{{Management}}</div>
  </div></div>
  {{/Management}}

  {{#Admission}}
  <div id="tab-inläg" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Admission}}</div>
    <div class="content-raw" style="display:none">{{Admission}}</div>
  </div></div>
  {{/Admission}}

  {{#Treatment}}
  <div id="tab-beh" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Treatment}}</div>
    <div class="content-raw" style="display:none">{{Treatment}}</div>
  </div></div>
  {{/Treatment}}

  {{#Surgery}}
  <div id="tab-op" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Surgery}}</div>
    <div class="content-raw" style="display:none">{{Surgery}}</div>
  </div></div>
  {{/Surgery}}

  {{#Follow-up}}
  <div id="tab-uppf" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Follow-up}}</div>
    <div class="content-raw" style="display:none">{{Follow-up}}</div>
  </div></div>
  {{/Follow-up}}

  {{#Prognosis}}
  <div id="tab-prog" class="tab-panel"><div class="panel-content">
    <div class="content-cloze">{{cloze:Prognosis}}</div>
    <div class="content-raw" style="display:none">{{Prognosis}}</div>
  </div></div>
  {{/Prognosis}}

</div>

<div class="panel-extra">{{Extra}}</div>

<script>
(function () {
  const $  = s => document.querySelector(s);
  const $$ = s => Array.from(document.querySelectorAll(s));

  // Bygg regex via charCodes för att inte trigga Ankis parser
  const OPEN  = String.fromCharCode(123,123);
  const CLOSE = String.fromCharCode(125,125);
  const reCloze = new RegExp(OPEN + 'c\\\\d+::' + '([\\\\s\\\\S]*?)' + '(?:::[^}]+)?' + CLOSE, 'g');

  function stripClozeFromHTML(html) {
    if (!html) return '';
    return html.replace(reCloze, '$1');
  }

  // Läs in (en gång) och cacha cloze+ren text på varje panel-content
  function primePanel(panelEl){
    const cont    = panelEl.querySelector('.panel-content');
    if (!cont || cont.dataset._primed === '1') return;

    const clozeEl = cont.querySelector('.content-cloze');
    const rawEl   = cont.querySelector('.content-raw');

    const clozeHTML = (clozeEl && clozeEl.innerHTML ? clozeEl.innerHTML.trim() : '');
    const rawHTML   = (rawEl && rawEl.innerHTML ? rawEl.innerHTML : '');

    cont.dataset.cloze = clozeHTML;                 // kan vara tom sträng
    cont.dataset.raw   = stripClozeFromHTML(rawHTML);
    cont.dataset._primed = '1';
  }

  function setPanelMode(panelEl, isActive){
    const cont = panelEl.querySelector('.panel-content');
    if (!cont) return;
    const cloze = cont.dataset.cloze || '';
    const raw   = cont.dataset.raw   || '';
    // Aktiv flik: visa cloze om den finns, annars ren text
    // Övriga flikar: visa ren text
    cont.innerHTML = (isActive && cloze) ? cloze : raw;
  }

  // Hjälp för att hitta första panel som verkligen har .cloze
  function detectFirstClozePanelId(panels){
    for (const p of panels) {
      if (p.el.querySelector('.content-cloze .cloze') || p.el.querySelector('.panel-content .cloze')) {
        return p.id; // t.ex. 'bak'
      }
    }
    return panels.length ? panels[0].id : '';
  }

  // Autoscroll så aktiv knapp alltid är helt synlig på mobil
  const isMobile = () => window.matchMedia('(max-width: 640px)').matches;

  function ensureActiveTabVisible(smooth) {
    if (!isMobile()) return;
    const container = $('.tab-buttons');
    if (!container) return;
    const active = container.querySelector('.tab-btn.active') || container.querySelector('.tab-btn');
    if (!active) return;

    const cRect = container.getBoundingClientRect();
    const aRect = active.getBoundingClientRect();

    let delta = 0;
    if (aRect.left < cRect.left) {
      delta = aRect.left - cRect.left; // scrolla vänster
    } else if (aRect.right > cRect.right) {
      delta = aRect.right - cRect.right; // scrolla höger
    }
    if (delta) {
      container.scrollTo({
        left: container.scrollLeft + delta,
        behavior: smooth ? 'smooth' : 'auto'
      });
    }
  }

  function queueEnsure(smooth){
    // dubbla rAF → efter layout/styling/Ankis DOM-uppdateringar
    requestAnimationFrame(() => {
      requestAnimationFrame(() => ensureActiveTabVisible(smooth));
    });
  }

  // -------- Init --------
  const panelEls = $$('.tab-panel');
  panelEls.forEach(primePanel);

  const panels = panelEls.map(el => ({ id: el.id.replace('tab-',''), el }));
  const btns   = $$('.tab-btn');

  let activeId = detectFirstClozePanelId(panels);

  function rerender(){
    panels.forEach(p => {
      const isActive = (p.id === activeId);
      p.el.classList.toggle('active', isActive);
      setPanelMode(p.el, isActive);
    });
    btns.forEach(b => b.classList.toggle('active', b.dataset.tab === activeId));
    queueEnsure(false);
  }

  rerender();

  // Byt flik på klick
  btns.forEach(b => b.addEventListener('click', () => {
    activeId = b.dataset.tab;
    rerender();
    queueEnsure(true);
  }));

  // Space/Enter på framsidan → vänd kortet
  document.addEventListener('keydown', function(e){
    const k = e.key || e.code;
    const isSpace = k === ' ' || k === 'Spacebar' || k === 'Space';
    const isEnter = k === 'Enter';
    const onBack  = !!document.getElementById('answer');
    const tag     = (document.activeElement && document.activeElement.tagName) || '';
    if (!onBack && (isSpace || isEnter) &&
        !/^(INPUT|TEXTAREA|SELECT)$/.test(tag) &&
        typeof pycmd === 'function') {
      e.preventDefault();
      pycmd('ans');
    }
  }, {passive:false});

  // Håll autoscroll robust i Ankis webview-livscykel
  queueEnsure(false);
  window.addEventListener('resize', () => queueEnsure(false));
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') queueEnsure(false);
  });

  // Om något (t.ex. klass) förändras i knappraden → säkra synlighet
  const container = $('.tab-buttons');
  if (container && 'MutationObserver' in window) {
    const mo = new MutationObserver(() => queueEnsure(false));
    mo.observe(container, {subtree: true, childList: true, attributes: true, attributeFilter: ['class']});
  }
})();
</script>

<br><br>
<div id="bildkälla" style="font-size: 7px; color: gray;">
    
</div>



"""

CSS = """.card { 
  font-family: -apple-system, Inter, Segoe UI, Roboto, sans-serif; 
  font-size: 18px; 
  line-height: 1.45; 
  max-width: 55rem; 
  margin: 0 auto; 
  background: #ffffff;
  color: var(--fg);
}

/* Titel */
.title {
  font-size: 24px;
  font-weight: 700;
  text-align: center;
  margin: 20px 0;
  color: var(--fg);
}

/* Flikcontainer */
.tabs { 
  border: 1px solid #a8a8a8;        /* mörkare grå kant */
  border-radius: 10px;
  overflow: hidden;
  background: #dcdcdc;              /* mörkare ljusgrå */
}

/* Flikknappar + scrollbar */
.tab-buttons { 
  display: flex;
  border-bottom: 1px solid #a8a8a8; 
  background: #cccccc;              /* något mörkare tabbar */
  overflow-x: auto;
  overflow-y: hidden;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin;
}

.tab-buttons::-webkit-scrollbar { height: 6px; }
.tab-buttons::-webkit-scrollbar-thumb { 
  background: rgba(0,0,0,0.15); 
  border-radius: 4px; 
}
.tab-buttons::-webkit-scrollbar-track { background: transparent; }

/* Tabbar */
.tab-btn { 
  flex: 1;
  padding: 6px 8px;            
  font-size: 14px;             
  font-weight: 500;            
  border: 0; 
  background: transparent; 
  color: #444;                  /* lite mörkare text */
  cursor: pointer; 
  transition: background .15s ease, color .15s ease; 
  user-select: none; 
}

/* Mobil */
@media (max-width: 640px) {
  .tab-buttons {
    width: 100%;
  }
  .tab-btn {
    flex: 1 0 auto;
    padding: 6px 12px;
    font-size: 11px;
    scroll-snap-align: start;
  }
}

/* Hover */
.tab-btn:hover  { 
  background: #bdbdbd; 
  color: #222; 
}

/* Aktiv flik */
.tab-btn.active { 
  background: #b0b0b0; 
  color: #111; 
}

/* Paneler */
.tab-panel { 
  display: none; 
  padding: 10px 12px; 
  background: #e6e6e6;            /* lite mörkare panelbakgrund */
  color: #000;                  
  font-size: 16px;
  line-height: 1.45;
}

.tab-panel.active { display: block; }

/* Panelinnehåll */
.panel-content { 
  white-space: pre-wrap; 
  word-wrap: break-word; 
}

/* Cloze-text – Mörkblå (original Anki) */
.cloze { 
  font-weight: bold; 
  text-decoration: none !important;
  color: #0B3FD4 !important;
}

/* Cloze på baksidan */
#answer ~ .tabs .cloze {
  font-weight: bold;
  text-decoration: none !important;
  color: #0B3FD4 !important;
}

/* Extra-fält */
.panel-extra {
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  font-style: italic;
  color: #888;
  text-align: center;
  display: block;
  width: 100%;
  line-height: 1.2;
}

/* Hint */
.hint { 
  font-size: 7px; 
  color: gray !important; 
  text-align: center;
  display: block;
  margin-top: 0.3em;
}

/* Hint inline */
.hint[style*="display: inline;"] { 
  color: black !important;
  display: inline;
  text-align: left;
}"""

FIELDS = ["Disease", "Definition", "Classification", "Histology", "Etiology", "Pathophysiology", "Epidemiology", "Risk Factors", "Symptoms", "Clinical Findings", "Investigation", "Diagnosis", "Management", "Admission", "Treatment", "Surgery", "Follow-up", "Prognosis", "Extra"]


def create_note_type():
    col = mw.col
    existing = col.models.by_name(NOTE_TYPE_NAME)
    if existing:
        return

    m = col.models.new(NOTE_TYPE_NAME)
    m["type"] = 1  # cloze type

    for field_name in FIELDS:
        fld = col.models.new_field(field_name)
        col.models.add_field(m, fld)

    t = col.models.new_template("AnkiTabs Card")
    t["qfmt"] = FRONT_TEMPLATE
    t["afmt"] = BACK_TEMPLATE
    col.models.add_template(m, t)

    m["css"] = CSS
    col.models.add(m)
    col.models.save(m)


def on_profile_loaded():
    create_note_type()


gui_hooks.profile_did_open.append(on_profile_loaded)
