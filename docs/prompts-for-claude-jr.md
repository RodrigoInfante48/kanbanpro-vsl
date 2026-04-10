# Prompts para Claude Code Jr (ollama launch claude)

> Copia y pega estos prompts en `ollama launch claude` (qwen3.5:cloud).
> Prerequisito: tener el repo clonado y estar en la carpeta del proyecto.
> Cada prompt es independiente — no necesitan conversación previa.

---

## PROMPT 0 — Clonar el repo (solo la primera vez)

```
git clone https://github.com/RodrigoInfante48/kanbanpro-vsl.git
cd kanbanpro-vsl
git checkout claude/upgrade-vsl-landing-page-yF8WE
```

---

## PROMPT 1 — Subir los archivos de contexto al repo

> Usa este prompt después de copiar manualmente el archivo `docs/notion-product.md` al repo.

```
Estoy en el repo RodrigoInfante48/kanbanpro-vsl, branch claude/upgrade-vsl-landing-page-yF8WE.

Lee estos archivos para entender el proyecto completo:
1. docs/GTM-ROADMAP.md — el plan de la landing page
2. docs/PROMPTS.md — la arquitectura de prompts por sesión
3. docs/PROGRESS.md — el estado actual del proyecto
4. docs/notion-product.md — la estructura completa del producto en Notion

Confirma que entendiste: qué es el producto, cuánto cuesta, quién lo compra, 
y qué secciones faltan por construir en el index.html.
```

---

## PROMPT 2 — Construir secciones 1-4 del index.html

> Este es el prompt de la Sesión 2 del ROADMAP. El más importante.

```
Contexto: Estoy rediseñando la VSL landing page de KanbanPro.
Branch: claude/upgrade-vsl-landing-page-yF8WE
Lee docs/GTM-ROADMAP.md COMPLETO antes de escribir una sola línea de código.
Lee docs/notion-product.md para entender qué es el producto.

Tu tarea: Reescribe el index.html desde cero con las primeras 4 secciones.
IMPORTANTE: Reemplaza el index.html existente completamente.

Especificaciones técnicas:
- HTML + Tailwind CDN (sin build step, sin frameworks)
- Font: Plus Jakarta Sans (300/400/600/700/800)
- Tailwind config inline con esta paleta exacta:
  primary: '#00e6c7', gold: '#FFB800', navy: '#1a1a2e', 
  surface: '#16213e', gray-dim: '#9ca3af', red-dim: '#ff6b6b', green-ok: '#4ade80'
- Solo español — eliminar todo el sistema i18n
- Mobile-first obligatorio
- Conservar Google Analytics G-M08G3EFVMM
- Conservar Meta Pixel 916718191120650

Secciones a construir:
1. HEAD: meta tags, GA, Meta Pixel, Tailwind CDN + config, fonts, CSS custom
2. HERO: eyebrow "120+ personas ya lo usan · 4.8★", 
   H1 "Tienes 100 ideas, 20 proyectos a medias y 0 sistemas.",
   subtítulo, phone mockup con assets/image_1.png, 
   CTA "Quiero el acceso por $22 →" link a https://pay.hotmart.com/I97237386O,
   microcopy "Solo 28 accesos disponibles este mes"
3. VSL VIDEO: thumbnail YouTube clickeable que abre modal 
   (YouTube ID: Ek2lHQ7K7Nk), botón play pulsante
4. PROBLEMA: H2 "Todo está en tu cabeza. Nada está en un sistema.",
   3 cards con iconos SVG inline (NO emojis, NO Material Icons):
   - "Abres Notion y no sabes por dónde empezar."
   - "Tienes 3 apps distintas para proyectos, tareas e ideas."
   - "Al final del día sientes que trabajaste mucho pero avanzaste poco."

Reglas de UI:
- cursor-pointer en todo lo clickeable
- transitions 150-300ms
- hover states en todos los elementos interactivos
- focus-visible:ring-2 en botones/links
- prefers-reduced-motion respetado
- touch targets mínimo 44x44px
- contraste texto mínimo 4.5:1

Al terminar: git add . && git commit -m "feat: S2 — HEAD + Hero + VSL + Problema"
```

---

## PROMPT 3 — Construir secciones 5-10 + JS

> Sesión 3 del ROADMAP. Completa toda la página.

```
Contexto: VSL Landing Page KanbanPro.
Branch: claude/upgrade-vsl-landing-page-yF8WE
Lee docs/GTM-ROADMAP.md para el copy exacto de cada sección.
Lee docs/notion-product.md para datos del producto.

El index.html ya tiene las secciones 1-4 (HEAD, Hero, VSL, Problema).
Tu tarea: Agrega las secciones 5-10 + scripts al MISMO archivo.

Secciones:
5. SOLUCIÓN: Visual Board como producto principal. Features con iconos SVG.
   Descripción: "El gestor multidimensional que te permite ver tus ideas, 
   objetivos, proyectos y tareas en un solo lugar — desde tu celular."
   Mini-CTA "Ver Visual Board →"

6. BONOS: Dos cards.
   Bono 1 — KanbanPro (valor $22): "gestiona cada proyecto con metodología real"
   Bono 2 — Notion Blueprint (valor $22): "pegamento operativo"
   Badge "GRATIS" en gold. Cierre: "Total valor: $66. Tú pagas: $22."

7. COMPARATIVA: Tabla responsive (cards en mobile, tabla en desktop).
   Visual Board $22 único vs Monday $124.90/mes vs Asana $149/mes vs Minitab $250+
   Columna Visual Board destacada en teal.

8. GARANTÍA: Badge con escudo SVG, "8 días para probarlo sin riesgo."
   "Sin formularios. Sin preguntas." Fondo surface.

9. PRUEBA SOCIAL: 4 testimonios en grid responsive.
   Stats animados: 120+ usuarios, 4.8★, $22, 8 días garantía.
   Imagen assets/image_2.png.

10. FAQ: Accordion JS puro, 5 preguntas:
    - ¿Necesito saber usar Notion? → No, viene listo para duplicar.
    - ¿Funciona en iOS y Android? → Sí, 100% mobile-first.
    - ¿Qué pasa si Notion sube de precio? → La plantilla siempre es tuya.
    - ¿Es para empresas o personas? → Para solopreneurs y freelancers.
    - ¿Cuánto tarda la entrega? → Acceso inmediato al pagar en Hotmart.

CTA FINAL: Countdown timer 30min, progress bar 22/28 slots,
precio $22 gold enorme, botón CTA full-width, 
link: https://pay.hotmart.com/I97237386O

STICKY BAR: Aparece tras 300px scroll. "Visual Board · $22 único" + CTA.
FOOTER: Logo DailyDuty, links, copyright 2026.

Scripts inline (sin librerías):
- VSL Modal YouTube (autoplay, cierre con Escape y backdrop)
- Countdown timer (1800s)
- IntersectionObserver scroll reveal
- FAQ accordion
- Sticky bar show/hide
- Stat counters animados

Al terminar: git add . && git commit -m "feat: S3 — complete page build"
```

---

## PROMPT 4 — QA y Push

```
Contexto: VSL Landing Page KanbanPro completa.
Branch: claude/upgrade-vsl-landing-page-yF8WE

Ejecuta este checklist sobre el index.html:

MOBILE (375px):
- ¿Scroll horizontal? → corregir overflow
- ¿Botones min-h-[44px]? → agregar
- ¿H1 cabe sin overflow? → ajustar
- ¿Tabla comparativa legible? → cards si no

ACCESIBILIDAD:
- ¿Botones icon-only con aria-label?
- ¿Imágenes con alt descriptivo?
- ¿Contraste teal #00e6c7 sobre navy #1a1a2e ≥ 4.5:1?

PERFORMANCE:
- ¿loading="lazy" en imágenes below-fold?
- ¿Fonts con display=swap?

INTERACCIÓN:
- ¿cursor-pointer en todo clickeable?
- ¿hover con transition-colors duration-200?
- ¿Modal cierra con Escape y backdrop?

LINKS:
- Hotmart: https://pay.hotmart.com/I97237386O
- WhatsApp: https://api.whatsapp.com/send/?phone=573209974750&text=Kanbanpro
- YouTube: Ek2lHQ7K7Nk

Corrige todo lo que encuentres.
git add . && git commit -m "fix: S4 — QA audit"
git push -u origin claude/upgrade-vsl-landing-page-yF8WE
```

---

## PROMPT DE EMERGENCIA — Fix de sección específica

```
Branch: claude/upgrade-vsl-landing-page-yF8WE
Lee docs/GTM-ROADMAP.md para contexto.

Reescribe SOLO la sección [NOMBRE] del index.html.
Problema: [describe qué está mal]
Cómo debe quedar: [describe el resultado esperado]
No toques el resto del archivo.

git add . && git commit -m "fix: rewrite [nombre] section"
```
