/**
 * KanbanPro — Pitch Deck para Gyms (9 slides)
 * Target: Propietarios de gym en Chapinero / Usaquen, Bogota
 * Brand: Teal #00e6c7 | Gold #FFB800 | Dark Navy #1a1a2e
 * Full dark theme — premium, tech, confianza
 */

const pptxgen = require("pptxgenjs");

// ─────────────────────────────────────────────
// BRAND TOKENS
// ─────────────────────────────────────────────
const C = {
  navy:      "1a1a2e",   // fondo principal
  surface:   "16213e",   // fondo cards / superficie
  card:      "0f3460",   // cards secundarios
  teal:      "00e6c7",   // primario — títulos, íconos
  tealDim:   "00b8a0",   // teal bajado
  gold:      "FFB800",   // precios, urgencia, CTA
  goldDim:   "cc9400",   // gold bajado
  white:     "ffffff",
  gray:      "9ca3af",
  grayLight: "d1d5db",
  red:       "ef4444",
  green:     "22c55e",
  greenDim:  "166534",
};

const F = {
  title: "Arial Black",
  head:  "Arial",
  body:  "Calibri",
};

const OUTPUT = "kanbanpro-gym-deck.pptx";

// ─────────────────────────────────────────────
// HELPERS
// ─────────────────────────────────────────────
const makeShadow = () => ({
  type: "outer", blur: 8, offset: 3, angle: 135, color: "000000", opacity: 0.3
});

function addBg(slide, color) {
  slide.background = { color };
}

function addRect(slide, x, y, w, h, color, opts = {}) {
  slide.addShape(slide.pres ? slide.pres.shapes.RECTANGLE : "rect", {
    x, y, w, h,
    fill: { color },
    line: { color, width: 0 },
    ...opts,
  });
}

// ─────────────────────────────────────────────
// PRESENTATION
// ─────────────────────────────────────────────
const pres = new pptxgen();
pres.layout   = "LAYOUT_16x9";  // 10" × 5.625"
pres.author   = "KanbanPro";
pres.title    = "KanbanPro — Sistema de Gestion para Tu Gym";
pres.subject  = "Pitch Deck Comercial — Gyms Bogota";

// ═══════════════════════════════════════════════════════
// SLIDE 1 — PORTADA
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  // Barra lateral teal (left accent)
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 0.18, h: 5.625,
    fill: { color: C.teal }, line: { color: C.teal, width: 0 },
  });

  // Barra inferior gold
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 5.2, w: 10, h: 0.425,
    fill: { color: C.gold }, line: { color: C.gold, width: 0 },
  });

  // Wordmark
  s.addText("KanbanPro", {
    x: 0.5, y: 0.5, w: 9, h: 0.8,
    fontSize: 18, fontFace: F.head, color: C.teal,
    bold: true, align: "left", margin: 0,
  });

  // Headline
  s.addText("¿Tu gym sigue\ncorriendo por WhatsApp?", {
    x: 0.5, y: 1.3, w: 6.2, h: 2.0,
    fontSize: 42, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });

  // Subhead
  s.addText("Hay una forma más inteligente de gestionar\nhorarios, instructores y miembros.", {
    x: 0.5, y: 3.45, w: 6.2, h: 1.0,
    fontSize: 15, fontFace: F.body, color: C.grayLight,
    align: "left", margin: 0,
  });

  // Badge gold right side
  s.addShape(pres.shapes.RECTANGLE, {
    x: 7.2, y: 1.6, w: 2.5, h: 2.4,
    fill: { color: C.surface }, line: { color: C.teal, width: 2 },
    shadow: makeShadow(),
  });
  s.addText("USD 22", {
    x: 7.2, y: 1.75, w: 2.5, h: 0.9,
    fontSize: 36, fontFace: F.title, color: C.gold,
    bold: true, align: "center", margin: 0,
  });
  s.addText("Pago único\nde por vida", {
    x: 7.2, y: 2.65, w: 2.5, h: 0.7,
    fontSize: 13, fontFace: F.body, color: C.grayLight,
    align: "center", margin: 0,
  });
  s.addText("Sin mensualidades", {
    x: 7.2, y: 3.4, w: 2.5, h: 0.4,
    fontSize: 10, fontFace: F.body, color: C.teal,
    bold: true, align: "center", margin: 0,
  });

  // Footer text gold bar
  s.addText("Rodrigo Infante  ·  +57 320 997 4750  ·  Bogotá, Colombia", {
    x: 0.5, y: 5.22, w: 9, h: 0.3,
    fontSize: 11, fontFace: F.body, color: C.navy,
    bold: true, align: "left", margin: 0,
  });
}

// ═══════════════════════════════════════════════════════
// SLIDE 2 — EL PROBLEMA
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  // Header strip
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 1.05,
    fill: { color: C.surface }, line: { color: C.surface, width: 0 },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 1.02, w: 10, h: 0.06,
    fill: { color: C.gold }, line: { color: C.gold, width: 0 },
  });

  s.addText("El problema real de tu gym", {
    x: 0.5, y: 0.18, w: 9, h: 0.7,
    fontSize: 30, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });

  // 3 problem cards
  const problems = [
    {
      emoji: "📱",
      title: "WhatsApp como sistema",
      desc: "Horarios, cambios, avisos, quejas — todo mezclado en el mismo chat. Sin historial, sin orden.",
    },
    {
      emoji: "👤",
      title: "Instructores sin claridad",
      desc: "Cada uno maneja su agenda de forma distinta. Los conflictos de horario se resuelven el mismo día.",
    },
    {
      emoji: "📉",
      title: "Miembros que se van sin avisar",
      desc: "No tienes visibilidad de quién está activo, quién faltó, quién está por cancelar.",
    },
  ];

  problems.forEach((p, i) => {
    const x = 0.35 + i * 3.15;
    s.addShape(pres.shapes.RECTANGLE, {
      x, y: 1.3, w: 2.9, h: 3.8,
      fill: { color: C.surface }, line: { color: C.card, width: 1 },
      shadow: makeShadow(),
    });
    // Gold top accent
    s.addShape(pres.shapes.RECTANGLE, {
      x, y: 1.3, w: 2.9, h: 0.07,
      fill: { color: C.gold }, line: { color: C.gold, width: 0 },
    });
    s.addText(p.emoji, {
      x, y: 1.5, w: 2.9, h: 0.65,
      fontSize: 32, align: "center", margin: 0,
    });
    s.addText(p.title, {
      x: x + 0.15, y: 2.22, w: 2.6, h: 0.65,
      fontSize: 15, fontFace: F.head, color: C.gold,
      bold: true, align: "center", margin: 0,
    });
    s.addText(p.desc, {
      x: x + 0.15, y: 2.92, w: 2.6, h: 1.9,
      fontSize: 12, fontFace: F.body, color: C.grayLight,
      align: "left", margin: 0,
    });
  });

  // Bottom note
  s.addText("¿Te suena familiar? Estás dejando dinero y miembros sobre la mesa.", {
    x: 0.5, y: 5.15, w: 9, h: 0.35,
    fontSize: 12, fontFace: F.body, color: C.teal,
    italic: true, align: "center", margin: 0,
  });
}

// ═══════════════════════════════════════════════════════
// SLIDE 3 — LA SOLUCIÓN
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  // Left panel (text)
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 4.6, h: 5.625,
    fill: { color: C.surface }, line: { color: C.surface, width: 0 },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 4.57, y: 0, w: 0.06, h: 5.625,
    fill: { color: C.teal }, line: { color: C.teal, width: 0 },
  });

  s.addText("La solución", {
    x: 0.4, y: 0.4, w: 3.8, h: 0.5,
    fontSize: 14, fontFace: F.body, color: C.teal,
    bold: true, align: "left", margin: 0,
  });
  s.addText("Un tablero Kanban\npara tu gym", {
    x: 0.4, y: 0.9, w: 3.8, h: 1.3,
    fontSize: 30, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });
  s.addText("KanbanPro convierte el caos operativo\nde tu gym en un tablero visual claro.", {
    x: 0.4, y: 2.3, w: 3.8, h: 0.8,
    fontSize: 13, fontFace: F.body, color: C.grayLight,
    align: "left", margin: 0,
  });

  const leftPoints = [
    "Clases y horarios del día en tiempo real",
    "Cada instructor sabe exactamente qué hace",
    "Miembros activos vs. inactivos de un vistazo",
    "Acceso desde cualquier celular o computador",
  ];
  leftPoints.forEach((pt, i) => {
    s.addShape(pres.shapes.OVAL, {
      x: 0.4, y: 3.2 + i * 0.47, w: 0.18, h: 0.18,
      fill: { color: C.teal }, line: { color: C.teal, width: 0 },
    });
    s.addText(pt, {
      x: 0.65, y: 3.17 + i * 0.47, w: 3.6, h: 0.24,
      fontSize: 12, fontFace: F.body, color: C.grayLight,
      align: "left", margin: 0,
    });
  });

  // Right panel — Kanban board mockup
  // Board container
  s.addShape(pres.shapes.RECTANGLE, {
    x: 4.85, y: 0.35, w: 4.9, h: 4.9,
    fill: { color: C.card }, line: { color: C.tealDim, width: 1 },
    shadow: makeShadow(),
  });

  // Board title bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: 4.85, y: 0.35, w: 4.9, h: 0.45,
    fill: { color: C.teal }, line: { color: C.teal, width: 0 },
  });
  s.addText("🏋️ Gym Kanban — Hoy", {
    x: 4.85, y: 0.37, w: 4.9, h: 0.38,
    fontSize: 13, fontFace: F.head, color: C.navy,
    bold: true, align: "center", margin: 0,
  });

  // 3 columns
  const cols = ["📋 Por Hacer", "⚡ En Curso", "✅ Listo"];
  const colColors = [C.surface, "1a3a5c", "0d2b1a"];
  cols.forEach((col, ci) => {
    const cx = 4.95 + ci * 1.6;
    s.addShape(pres.shapes.RECTANGLE, {
      x: cx, y: 0.88, w: 1.5, h: 4.25,
      fill: { color: colColors[ci] }, line: { color: C.navy, width: 1 },
    });
    s.addText(col, {
      x: cx, y: 0.9, w: 1.5, h: 0.32,
      fontSize: 9, fontFace: F.head, color: C.teal,
      bold: true, align: "center", margin: 0,
    });
    // Sample cards
    const cards = ci === 0
      ? ["Clase Yoga 7am", "Turno Limpieza"]
      : ci === 1
      ? ["Spinning 9am", "Renovar Memb."]
      : ["Pesas Tarde", "Check Equipos"];
    cards.forEach((card, ki) => {
      s.addShape(pres.shapes.RECTANGLE, {
        x: cx + 0.07, y: 1.3 + ki * 0.82, w: 1.36, h: 0.68,
        fill: { color: C.surface }, line: { color: C.tealDim, width: 1 },
        shadow: makeShadow(),
      });
      s.addText(card, {
        x: cx + 0.1, y: 1.35 + ki * 0.82, w: 1.3, h: 0.58,
        fontSize: 9, fontFace: F.body, color: C.white,
        align: "left", valign: "middle", margin: 0,
      });
    });
  });
}

// ═══════════════════════════════════════════════════════
// SLIDE 4 — CÓMO FUNCIONA (3 pasos)
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.95,
    fill: { color: C.surface }, line: { color: C.surface, width: 0 },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0.92, w: 10, h: 0.05,
    fill: { color: C.teal }, line: { color: C.teal, width: 0 },
  });
  s.addText("¿Cómo funciona?  —  3 pasos y tu gym está corriendo", {
    x: 0.5, y: 0.15, w: 9, h: 0.65,
    fontSize: 26, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });

  const steps = [
    {
      num: "1",
      title: "Compra y accede",
      desc: "Pago único de USD 22 en Hotmart. Acceso inmediato desde tu celular o computador. Sin instalación complicada.",
      color: C.teal,
    },
    {
      num: "2",
      title: "Configura tu gym",
      desc: "Agrega tus instructores, clases y horarios en menos de 30 minutos. Nosotros te acompañamos paso a paso.",
      color: C.gold,
    },
    {
      num: "3",
      title: "Opera en modo Kanban",
      desc: "Desde mañana, cada turno, instructor y miembro tiene su lugar en el tablero. Sin más WhatsApp caótico.",
      color: C.green,
    },
  ];

  steps.forEach((st, i) => {
    const x = 0.5 + i * 3.1;

    // Card
    s.addShape(pres.shapes.RECTANGLE, {
      x, y: 1.2, w: 2.85, h: 3.9,
      fill: { color: C.surface }, line: { color: C.card, width: 1 },
      shadow: makeShadow(),
    });
    // Top accent bar
    s.addShape(pres.shapes.RECTANGLE, {
      x, y: 1.2, w: 2.85, h: 0.07,
      fill: { color: st.color }, line: { color: st.color, width: 0 },
    });
    // Big number
    s.addShape(pres.shapes.OVAL, {
      x: x + 0.95, y: 1.35, w: 0.95, h: 0.95,
      fill: { color: st.color }, line: { color: st.color, width: 0 },
    });
    s.addText(st.num, {
      x: x + 0.95, y: 1.38, w: 0.95, h: 0.89,
      fontSize: 28, fontFace: F.title, color: C.navy,
      bold: true, align: "center", valign: "middle", margin: 0,
    });
    // Title
    s.addText(st.title, {
      x: x + 0.15, y: 2.42, w: 2.55, h: 0.55,
      fontSize: 16, fontFace: F.head, color: C.white,
      bold: true, align: "center", margin: 0,
    });
    // Desc
    s.addText(st.desc, {
      x: x + 0.15, y: 3.05, w: 2.55, h: 1.85,
      fontSize: 12, fontFace: F.body, color: C.grayLight,
      align: "left", margin: 0,
    });
  });

  // Arrow connectors between cards
  [1, 2].forEach(i => {
    const ax = 0.5 + i * 3.1 - 0.22;
    s.addShape(pres.shapes.LINE, {
      x: ax, y: 2.7, w: 0.22, h: 0,
      line: { color: C.tealDim, width: 2, dashType: "dash" },
    });
  });

  s.addText("Soporte incluido · Sin contrato · Cancelable cuando quieras", {
    x: 0.5, y: 5.2, w: 9, h: 0.3,
    fontSize: 11, fontFace: F.body, color: C.teal,
    italic: true, align: "center", margin: 0,
  });
}

// ═══════════════════════════════════════════════════════
// SLIDE 5 — BENEFICIOS CLAVE (2×2 grid)
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  // Left panel header
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 3.2, h: 5.625,
    fill: { color: C.teal }, line: { color: C.teal, width: 0 },
  });

  s.addText("Beneficios\nclave", {
    x: 0.2, y: 0.9, w: 2.8, h: 1.5,
    fontSize: 36, fontFace: F.title, color: C.navy,
    bold: true, align: "left", margin: 0,
  });
  s.addText("Lo que cambia en tu gym\ndesde el primer día.", {
    x: 0.2, y: 2.55, w: 2.8, h: 0.9,
    fontSize: 13, fontFace: F.body, color: C.surface,
    align: "left", margin: 0,
  });

  // USD 22 badge on teal
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.3, y: 3.7, w: 2.5, h: 1.2,
    fill: { color: C.navy }, line: { color: C.gold, width: 2 },
  });
  s.addText("USD 22", {
    x: 0.3, y: 3.78, w: 2.5, h: 0.6,
    fontSize: 28, fontFace: F.title, color: C.gold,
    bold: true, align: "center", margin: 0,
  });
  s.addText("Pago único de por vida", {
    x: 0.3, y: 4.38, w: 2.5, h: 0.38,
    fontSize: 10, fontFace: F.body, color: C.grayLight,
    align: "center", margin: 0,
  });

  // 2x2 benefit cards (right side)
  const benefits = [
    { icon: "🗂️", title: "Tablero en tiempo real", desc: "Todos los turnos del día visibles desde cualquier pantalla." },
    { icon: "👥", title: "Control de instructores", desc: "Agenda clara por persona. Sin mensajes de ida y vuelta." },
    { icon: "📊", title: "Seguimiento de miembros", desc: "Activos, inactivos, en riesgo de irse — de un vistazo." },
    { icon: "🔧", title: "Equipos y mantenimiento", desc: "Máquinas, zonas y limpieza organizados en el mismo tablero." },
  ];

  const positions = [
    { x: 3.45, y: 0.22 },
    { x: 6.72, y: 0.22 },
    { x: 3.45, y: 2.98 },
    { x: 6.72, y: 2.98 },
  ];

  benefits.forEach((b, i) => {
    const { x, y } = positions[i];
    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w: 3.0, h: 2.55,
      fill: { color: C.surface }, line: { color: C.card, width: 1 },
      shadow: makeShadow(),
    });
    // Teal top accent
    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w: 3.0, h: 0.06,
      fill: { color: C.teal }, line: { color: C.teal, width: 0 },
    });
    s.addText(b.icon, {
      x: x + 0.1, y: y + 0.14, w: 0.6, h: 0.55,
      fontSize: 26, align: "center", margin: 0,
    });
    s.addText(b.title, {
      x: x + 0.78, y: y + 0.14, w: 2.12, h: 0.55,
      fontSize: 14, fontFace: F.head, color: C.teal,
      bold: true, align: "left", margin: 0,
    });
    s.addText(b.desc, {
      x: x + 0.15, y: y + 0.78, w: 2.7, h: 1.6,
      fontSize: 12, fontFace: F.body, color: C.grayLight,
      align: "left", margin: 0,
    });
  });
}

// ═══════════════════════════════════════════════════════
// SLIDE 6 — COMPARATIVA
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.95,
    fill: { color: C.surface }, line: { color: C.surface, width: 0 },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0.92, w: 10, h: 0.05,
    fill: { color: C.teal }, line: { color: C.teal, width: 0 },
  });
  s.addText("KanbanPro vs. cómo gestionas hoy", {
    x: 0.5, y: 0.15, w: 9, h: 0.65,
    fontSize: 28, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });

  // Column headers
  const headers = ["", "WhatsApp + Excel", "Software genérico", "KanbanPro"];
  const colW = [2.8, 2.0, 2.0, 2.0];
  const startX = 0.3;

  headers.forEach((h, i) => {
    const x = startX + colW.slice(0, i).reduce((a, b) => a + b, 0);
    const isKanban = i === 3;
    if (i > 0) {
      s.addShape(pres.shapes.RECTANGLE, {
        x, y: 1.1, w: colW[i], h: 0.55,
        fill: { color: isKanban ? C.teal : C.surface },
        line: { color: isKanban ? C.teal : C.card, width: 1 },
      });
    }
    s.addText(h, {
      x: x + (i === 0 ? 0 : 0.05), y: 1.15, w: colW[i] - 0.1, h: 0.45,
      fontSize: isKanban ? 14 : 12, fontFace: F.head,
      color: isKanban ? C.navy : C.teal,
      bold: true, align: "center", margin: 0,
    });
  });

  const rows = [
    ["Tablero visual por actividad", "❌", "🟡 Parcial", "✅"],
    ["Control por instructor",       "❌", "🟡 Parcial", "✅"],
    ["Seguimiento de miembros",      "❌", "✅",         "✅"],
    ["Precio mensual",               "$0 (caos)", "$50-$150 USD/mes", "USD 22 único"],
    ["Sin contrato / cancelable",    "✅",         "❌",               "✅"],
    ["Soporte personalizado",        "❌",         "❌",               "✅"],
  ];

  rows.forEach((row, ri) => {
    const isEven = ri % 2 === 0;
    row.forEach((cell, ci) => {
      const x = startX + colW.slice(0, ci).reduce((a, b) => a + b, 0);
      const isKanban = ci === 3;
      const rowBg = isKanban ? (isEven ? "0d2b1a" : "0a2316") : (isEven ? C.surface : C.card);
      s.addShape(pres.shapes.RECTANGLE, {
        x, y: 1.72 + ri * 0.58, w: colW[ci], h: 0.58,
        fill: { color: rowBg }, line: { color: C.navy, width: 1 },
      });
      s.addText(cell, {
        x: x + 0.05, y: 1.76 + ri * 0.58, w: colW[ci] - 0.1, h: 0.48,
        fontSize: ci === 0 ? 12 : 13, fontFace: ci === 0 ? F.body : F.head,
        color: isKanban ? C.green : (ci === 0 ? C.grayLight : C.white),
        bold: isKanban, align: ci === 0 ? "left" : "center", margin: 0,
      });
    });
  });

  // Bottom note
  s.addText("KanbanPro no es el más barato — es el que más sentido tiene para tu operación.", {
    x: 0.5, y: 5.22, w: 9, h: 0.3,
    fontSize: 11, fontFace: F.body, color: C.teal,
    italic: true, align: "center", margin: 0,
  });
}

// ═══════════════════════════════════════════════════════
// SLIDE 7 — PRECIO
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  // Left dark panel
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 4.8, h: 5.625,
    fill: { color: C.surface }, line: { color: C.surface, width: 0 },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 4.78, y: 0, w: 0.04, h: 5.625,
    fill: { color: C.teal }, line: { color: C.teal, width: 0 },
  });

  // Left — price big display
  s.addText("Precio", {
    x: 0.4, y: 0.45, w: 4.0, h: 0.5,
    fontSize: 14, fontFace: F.body, color: C.teal,
    bold: true, align: "left", margin: 0,
  });
  s.addText("Una inversión.\nNo una suscripción.", {
    x: 0.4, y: 0.97, w: 4.0, h: 1.1,
    fontSize: 28, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });

  // Competitors strikethrough block
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.4, y: 2.25, w: 3.8, h: 0.55,
    fill: { color: C.card }, line: { color: C.red, width: 1 },
  });
  s.addText("Competidores: USD 50 – 150 / mes", {
    x: 0.4, y: 2.3, w: 3.8, h: 0.42,
    fontSize: 13, fontFace: F.body, color: C.gray,
    align: "center", margin: 0,
  });
  s.addShape(pres.shapes.LINE, {
    x: 0.5, y: 2.52, w: 3.6, h: 0,
    line: { color: C.red, width: 2 },
  });

  // Big price
  s.addText("USD 22", {
    x: 0.4, y: 2.95, w: 4.0, h: 1.1,
    fontSize: 68, fontFace: F.title, color: C.gold,
    bold: true, align: "center", margin: 0,
  });
  s.addText("Pago único · Acceso de por vida", {
    x: 0.4, y: 4.1, w: 4.0, h: 0.38,
    fontSize: 13, fontFace: F.body, color: C.grayLight,
    align: "center", margin: 0,
  });

  // Right — what's included
  s.addText("¿Qué incluye?", {
    x: 5.1, y: 0.45, w: 4.6, h: 0.55,
    fontSize: 22, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });

  const includes = [
    { icon: "✅", text: "Acceso completo a KanbanPro" },
    { icon: "✅", text: "Tableros ilimitados para tu gym" },
    { icon: "✅", text: "Usuarios ilimitados (instructores, admin)" },
    { icon: "✅", text: "Soporte personalizado vía WhatsApp" },
    { icon: "✅", text: "Actualizaciones incluidas de por vida" },
    { icon: "✅", text: "Onboarding guiado paso a paso" },
  ];
  includes.forEach((item, i) => {
    s.addText(`${item.icon}  ${item.text}`, {
      x: 5.1, y: 1.15 + i * 0.62, w: 4.6, h: 0.5,
      fontSize: 13, fontFace: F.body, color: C.grayLight,
      align: "left", margin: 0,
    });
  });

  // Guarantee badge
  s.addShape(pres.shapes.RECTANGLE, {
    x: 5.1, y: 4.9, w: 4.6, h: 0.55,
    fill: { color: C.greenDim }, line: { color: C.green, width: 1 },
  });
  s.addText("🛡️  Sin contrato · Sin mensualidades · Cancelable cuando quieras", {
    x: 5.1, y: 4.93, w: 4.6, h: 0.4,
    fontSize: 10.5, fontFace: F.body, color: C.green,
    bold: true, align: "center", margin: 0,
  });
}

// ═══════════════════════════════════════════════════════
// SLIDE 8 — TESTIMONIOS / CREDIBILIDAD
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.95,
    fill: { color: C.surface }, line: { color: C.surface, width: 0 },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0.92, w: 10, h: 0.05,
    fill: { color: C.gold }, line: { color: C.gold, width: 0 },
  });
  s.addText("¿Por qué confiar en KanbanPro?", {
    x: 0.5, y: 0.15, w: 9, h: 0.65,
    fontSize: 28, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });

  // Left — stats
  const stats = [
    { val: "Six Sigma", label: "Metodología base del sistema" },
    { val: "100%",      label: "Web — sin app que descargar" },
    { val: "< 30 min",  label: "Tiempo de configuración inicial" },
  ];
  stats.forEach((st, i) => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: 0.4 + i * 3.1, y: 1.15, w: 2.8, h: 1.7,
      fill: { color: C.surface }, line: { color: C.teal, width: 1 },
      shadow: makeShadow(),
    });
    s.addShape(pres.shapes.RECTANGLE, {
      x: 0.4 + i * 3.1, y: 1.15, w: 2.8, h: 0.06,
      fill: { color: C.teal }, line: { color: C.teal, width: 0 },
    });
    s.addText(st.val, {
      x: 0.4 + i * 3.1, y: 1.28, w: 2.8, h: 0.75,
      fontSize: 24, fontFace: F.title, color: C.gold,
      bold: true, align: "center", margin: 0,
    });
    s.addText(st.label, {
      x: 0.55 + i * 3.1, y: 2.06, w: 2.5, h: 0.65,
      fontSize: 12, fontFace: F.body, color: C.grayLight,
      align: "center", margin: 0,
    });
  });

  // Sobre el fundador
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.4, y: 3.05, w: 9.2, h: 2.35,
    fill: { color: C.surface }, line: { color: C.card, width: 1 },
    shadow: makeShadow(),
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.4, y: 3.05, w: 0.07, h: 2.35,
    fill: { color: C.teal }, line: { color: C.teal, width: 0 },
  });

  s.addText("Sobre el fundador", {
    x: 0.65, y: 3.15, w: 8.7, h: 0.4,
    fontSize: 14, fontFace: F.head, color: C.teal,
    bold: true, align: "left", margin: 0,
  });
  s.addText(
    "Rodrigo Infante — Ingeniero de datos y especialista en metodología Six Sigma. " +
    "Diseñé KanbanPro porque vi de primera mano cómo los gyms, clínicas y negocios pierden dinero " +
    "gestionando sus operaciones en chats y hojas de cálculo. " +
    "KanbanPro es la herramienta que yo hubiera querido tener — y que hoy pongo en tus manos a un precio justo.",
    {
      x: 0.65, y: 3.62, w: 8.7, h: 1.65,
      fontSize: 13, fontFace: F.body, color: C.grayLight,
      align: "left", margin: 0,
    }
  );
}

// ═══════════════════════════════════════════════════════
// SLIDE 9 — CTA CIERRE
// ═══════════════════════════════════════════════════════
{
  const s = pres.addSlide();
  s.background = { color: C.teal };

  // Dark overlay panel (left)
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 5.8, h: 5.625,
    fill: { color: C.navy }, line: { color: C.navy, width: 0 },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 5.78, y: 0, w: 0.04, h: 5.625,
    fill: { color: C.gold }, line: { color: C.gold, width: 0 },
  });

  s.addText("KanbanPro", {
    x: 0.5, y: 0.55, w: 5.0, h: 0.5,
    fontSize: 16, fontFace: F.head, color: C.teal,
    bold: true, align: "left", margin: 0,
  });
  s.addText("Tu gym merece\nun sistema real.", {
    x: 0.5, y: 1.1, w: 5.0, h: 1.5,
    fontSize: 38, fontFace: F.title, color: C.white,
    bold: true, align: "left", margin: 0,
  });
  s.addText("Deja de gestionar en WhatsApp.\nEmpieza a operar con claridad — hoy.", {
    x: 0.5, y: 2.72, w: 5.0, h: 0.85,
    fontSize: 15, fontFace: F.body, color: C.grayLight,
    align: "left", margin: 0,
  });

  // Precio en panel oscuro
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: 3.72, w: 4.5, h: 1.5,
    fill: { color: C.surface }, line: { color: C.gold, width: 2 },
    shadow: makeShadow(),
  });
  s.addText("USD 22  —  Pago único de por vida", {
    x: 0.5, y: 3.85, w: 4.5, h: 0.6,
    fontSize: 20, fontFace: F.title, color: C.gold,
    bold: true, align: "center", margin: 0,
  });
  s.addText("hotmart.com / kanbanpro.co", {
    x: 0.5, y: 4.48, w: 4.5, h: 0.45,
    fontSize: 13, fontFace: F.body, color: C.teal,
    align: "center", margin: 0,
  });

  // Right panel — contacto
  s.addText("¿Listo para empezar?", {
    x: 6.1, y: 0.8, w: 3.6, h: 0.65,
    fontSize: 22, fontFace: F.title, color: C.navy,
    bold: true, align: "center", margin: 0,
  });

  const contacts = [
    { icon: "💬", label: "WhatsApp", val: "+57 320 997 4750" },
    { icon: "🌐", label: "Web",      val: "kanbanpro.co" },
    { icon: "📧", label: "Hotmart",  val: "hotmart.com/kanbanpro" },
  ];
  contacts.forEach((ct, i) => {
    s.addShape(pres.shapes.RECTANGLE, {
      x: 6.1, y: 1.65 + i * 1.1, w: 3.6, h: 0.88,
      fill: { color: C.navy }, line: { color: C.navy, width: 1 },
    });
    s.addText(ct.icon, {
      x: 6.15, y: 1.68 + i * 1.1, w: 0.6, h: 0.75,
      fontSize: 24, align: "center", margin: 0,
    });
    s.addText(ct.label, {
      x: 6.82, y: 1.68 + i * 1.1, w: 2.85, h: 0.32,
      fontSize: 10, fontFace: F.body, color: C.navy,
      bold: true, align: "left", margin: 0,
    });
    s.addText(ct.val, {
      x: 6.82, y: 2.0 + i * 1.1, w: 2.85, h: 0.35,
      fontSize: 13, fontFace: F.head, color: C.navy,
      bold: true, align: "left", margin: 0,
    });
  });

  s.addText("Escríbeme hoy — respondo en menos de 1 hora.", {
    x: 6.0, y: 5.07, w: 3.8, h: 0.38,
    fontSize: 10, fontFace: F.body, color: C.navy,
    italic: true, align: "center", margin: 0,
  });
}

// ─────────────────────────────────────────────
// GUARDAR
// ─────────────────────────────────────────────
pres.writeFile({ fileName: OUTPUT })
  .then(() => console.log(`[OK] Deck generado: ${OUTPUT}`))
  .catch(err => console.error("[ERROR]", err));
