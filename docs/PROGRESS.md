# Progress Tracker — VSL Landing Page

## Resumen de estado

```
S1 ✅ → S2 ⬜ → S3 ⬜ → S4 ⬜ → LIVE 🚀
```

---

## Sesión 1 — Diseño y Arquitectura ✅

**Fecha:** 2026-04-09
**Branch:** `claude/upgrade-vsl-landing-page-yF8WE`

### Completado
- [x] Exploración del repo existente (index.html 1207 líneas, analizado)
- [x] Design system generado con ui-ux-pro-max skill
  - Pattern: Scroll-Triggered Storytelling
  - Font: Plus Jakarta Sans
  - Paleta: Teal #00e6c7 · Gold #FFB800 · Navy #1a1a2e · Surface #16213e
- [x] Plan de 10 secciones aprobado por Rod
- [x] Copy por sección definido (español, tuteo, sin frases prohibidas)
- [x] Arquitectura de prompts documentada (docs/PROMPTS.md)
- [x] GTM Roadmap documentado (docs/GTM-ROADMAP.md)
- [x] Rama de desarrollo creada

### Decisiones tomadas
- Eliminar sistema i18n (solo español)
- Reemplazar Inter por Plus Jakarta Sans
- Fondo: #1a1a2e (más oscuro que el actual #0f2320 — mejor contraste)
- Producto principal: Visual Board (no KanbanPro como en la versión anterior)
- Sin librerías JS externas (IntersectionObserver puro)

### Archivos modificados
- `docs/GTM-ROADMAP.md` — creado
- `docs/PROMPTS.md` — creado
- `docs/PROGRESS.md` — creado

---

## Sesión 2 — Build: HEAD + Hero + VSL + Problema ⬜

**Fecha:** —
**Prompt a usar:** Ver `docs/PROMPTS.md` → SESIÓN 2

### Tareas
- [ ] HEAD completo (meta, GA, Tailwind config, fonts, CSS custom)
- [ ] Hero section (eyebrow, H1, subtítulo, phone mockup, CTA, urgency)
- [ ] VSL modal funcional (YouTube Ek2lHQ7K7Nk, autoplay, cierre con Escape)
- [ ] Sección Problema (H2 + 3 pain points + iconos SVG)
- [ ] Commit al branch

### Criterio de éxito
El hero debe comunicar el hook en los primeros 3 segundos de lectura.
El modal del video debe abrirse y cerrarse correctamente en mobile.

---

## Sesión 3 — Build: Secciones 5-10 + JS + Footer ⬜

**Fecha:** —
**Prompt a usar:** Ver `docs/PROMPTS.md` → SESIÓN 3

### Tareas
- [ ] Sección Solución (Visual Board)
- [ ] Sección Bonos (KanbanPro + Notion Blueprint)
- [ ] Tabla Comparativa (responsive — cards en mobile)
- [ ] Sección Garantía (8 días)
- [ ] Prueba Social (4 testimonios + stats animados)
- [ ] FAQ accordion (5 preguntas)
- [ ] CTA Final (countdown + progress bar + botón grande)
- [ ] Marquee métodos de pago
- [ ] Footer
- [ ] Sticky bar (scroll-triggered)
- [ ] Todos los scripts JS inline
- [ ] Commit al branch

### Criterio de éxito
La página completa se puede scrollear de arriba a abajo sin errores visuales.
El countdown timer funciona. El FAQ accordion abre/cierra. El sticky bar aparece.

---

## Sesión 4 — QA + Push Final ⬜

**Fecha:** —
**Prompt a usar:** Ver `docs/PROMPTS.md` → SESIÓN 4

### Tareas
- [ ] Audit mobile 375px
- [ ] Audit accesibilidad (aria-labels, alt, contraste)
- [ ] Audit performance (lazy loading, fonts swap)
- [ ] Audit interacción (cursor-pointer, hover states, transitions)
- [ ] Verificar todos los links críticos
- [ ] Fix de todos los issues encontrados
- [ ] Push a remote
- [ ] Confirmar live en GitHub Pages

### Criterio de éxito
Checklist completo de ui-ux-pro-max en verde.
La página carga en < 3s en conexión 3G (estimado).
Push exitoso, GitHub Pages updated.

---

## Métricas de éxito del proyecto

| KPI | Baseline actual | Meta |
|-----|----------------|------|
| Conversión landing | Desconocida | ≥ 3% |
| Tiempo en página | Desconocido | ≥ 90s |
| Ventas/mes | — | 2,000 |
| Ticket promedio | $22 | $22 + order bump |

---

## Log de cambios

| Fecha | Sesión | Descripción | Commit |
|-------|--------|-------------|--------|
| 2026-04-09 | S1 | Diseño, plan, docs creados | — |

---

*Actualizar este archivo al final de cada sesión.*
