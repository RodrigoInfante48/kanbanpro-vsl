# Arquitectura de Prompts — VSL Landing Page
**Uso:** Copia y pega cada prompt en una sesión nueva de Claude Code.
**Regla de oro:** Siempre abre el repo `RodrigoInfante48/kanbanpro-vsl` antes de pegar el prompt.
**Branch de trabajo:** `claude/upgrade-vsl-landing-page-yF8WE`

---

## Mapa de sesiones

| Sesión | Objetivo | Tokens estimados | Output |
|--------|----------|-----------------|--------|
| S1 | Diseño, plan, docs | ~40k | Aprobado ✅ |
| S2 | HEAD + Hero + VSL + Problema + Solución | ~35k | index.html parcial |
| S3 | Bonos + Comparativa + Garantía + Testimonios + FAQ + CTA Final + JS | ~40k | index.html completo |
| S4 | QA mobile + fixes + push final | ~20k | Rama lista para merge |

**Total estimado:** ~135k tokens · ~4 días (1 sesión/día)

---

## SESIÓN 2 — Build: HEAD + Hero + Secciones 3 y 4

> **Cuándo usarlo:** Primera sesión de construcción.
> **Prerequisito:** Sesión 1 completada, rama creada.
> **Output esperado:** index.html con las primeras 4 secciones funcionales, commiteado al branch.

```
Contexto del proyecto: Estoy rediseñando la VSL landing page de KanbanPro en el repo
RodrigoInfante48/kanbanpro-vsl. El branch de trabajo es claude/upgrade-vsl-landing-page-yF8WE.
Lee el archivo docs/GTM-ROADMAP.md para entender el proyecto completo antes de empezar.

Tu tarea en esta sesión: Escribe el nuevo index.html desde cero con las primeras 4 secciones.
IMPORTANTE: Reemplaza el index.html existente completamente.

Especificaciones técnicas:
- HTML + Tailwind CDN (sin build step)
- Font: Plus Jakarta Sans (300/400/600/700/800) — reemplaza Inter
- Tailwind config con paleta exacta del ROADMAP
- Solo español — eliminar todo el sistema i18n y el objeto translations
- Conservar: Google Tag Manager G-M08G3EFVMM, URL de Hotmart, WhatsApp, YouTube ID Ek2lHQ7K7Nk
- Mobile-first obligatorio

Secciones a construir en esta sesión:
1. HEAD: meta tags, GA, Tailwind CDN + config completo con todos los colores, fonts, CSS custom
2. HERO: eyebrow badge (120+ · 4.8★), H1 hook, subtítulo, phone mockup con imagen assets/image_1.png,
   botón CTA verde-teal, microcopy de urgencia (28 accesos/mes)
3. VSL VIDEO: sección con thumbnail clickeable que abre modal YouTube (ID: Ek2lHQ7K7Nk)
   con botón play pulsante — el modal ya existe en el código actual, reutilizarlo
4. PROBLEMA: H2 "Todo está en tu cabeza. Nada está en un sistema.",
   3 pain points en cards con iconos SVG (no Material Icons, no emojis)

Copy exacto está en docs/GTM-ROADMAP.md sección "Copy aprobado por sección".
Paleta exacta está en docs/GTM-ROADMAP.md sección "Design system aprobado".

Al terminar: commitea al branch claude/upgrade-vsl-landing-page-yF8WE con mensaje
"feat: S2 — HEAD + Hero + VSL + Problema sections"
```

---

## SESIÓN 3 — Build: Secciones 5 a 10 + JS + Footer

> **Cuándo usarlo:** Día siguiente de Sesión 2.
> **Prerequisito:** Sesión 2 commiteada, index.html tiene las primeras 4 secciones.
> **Output esperado:** index.html completo, funcional, listo para QA.

```
Contexto del proyecto: Continúo construyendo la VSL landing page de KanbanPro.
Branch: claude/upgrade-vsl-landing-page-yF8WE
Lee docs/GTM-ROADMAP.md para contexto completo.

El index.html ya tiene las primeras 4 secciones (HEAD, Hero, VSL, Problema).
Tu tarea: Agrega las secciones 5 a 10 + todos los scripts al mismo archivo.

Secciones a construir:
5. SOLUCIÓN: H2 + descripción de Visual Board, features visuales con iconos SVG,
   link a https://kanbanpro.notion.site/Visual-Board-2ff4f515cfb080c095d1ed72b2442c6f?pvs=74
   Mini-CTA inline "Ver Visual Board →"

6. BONOS: Dos cards con valor monetario explícito.
   Bono 1 KanbanPro ($22 valor), Bono 2 Notion Blueprint ($22 valor).
   Badge "GRATIS" en gold. Cierre "Total valor: $66. Tú pagas: $22."

7. COMPARATIVA: Tabla responsive (en mobile: cards, en desktop: tabla)
   vs Monday Pro $124.90, Asana Pro $149.00, Minitab $250+
   Visual Board en columna destacada con color teal.
   Ancla de precio: "$22 único vs $124.90/mes".

8. GARANTÍA: Badge verde con escudo SVG, texto garantía 8 días,
   "Sin formularios. Sin preguntas." Fondo surface #16213e.

9. PRUEBA SOCIAL: 4 testimonios en grid (1 col mobile, 2 col tablet, 4 col desktop).
   Stats animados: contador 120+ usuarios, 4.8★, $22, 8 días garantía.
   Imagen assets/image_2.png con animated gradient border.

10. FAQ: Accordion con 5 preguntas (JS puro, sin librería).
    Animación suave al abrir/cerrar. Iconos + / − SVG.

CTA FINAL: Countdown timer (1800s → redirige a Hotmart), progress bar 22/28 slots,
precio $22 gold enorme, botón CTA grande full-width, garantía microcopy debajo.
Marquee de métodos de pago (Efecty, Nequi, PSE, PayPal, Tarjetas).

FOOTER: Logo DailyDuty, links (Linktree, Hotmart, WhatsApp, FAQ), copyright.

STICKY BAR: Aparece tras 300px de scroll. "Visual Board · $22 único" + botón CTA.

SCRIPTS a incluir (todos inline, sin librerías externas):
- VSL Modal (YouTube embed dinámico, ya existe — conservar y adaptar)
- Countdown timer (1800s, redirige al expirar)
- IntersectionObserver fade-in para todas las secciones (class "fade-in" → "visible")
- FAQ accordion
- Sticky bar show/hide on scroll
- Stat counters animados (requestAnimationFrame)

CSS adicional en <style>:
- @keyframes fade-in-up para animaciones de scroll
- .fade-in { opacity: 0; transform: translateY(20px); transition: all 0.6s ease; }
- .fade-in.visible { opacity: 1; transform: translateY(0); }
- @media (prefers-reduced-motion: reduce) { .fade-in { opacity: 1; transform: none; transition: none; } }

Al terminar: commitea con mensaje "feat: S3 — complete page build, all sections + JS"
```

---

## SESIÓN 4 — QA, Fixes y Push Final

> **Cuándo usarlo:** Después de revisar visualmente el resultado de Sesión 3.
> **Prerequisito:** index.html completo en el branch.
> **Output esperado:** Rama lista para merge a main y deploy a GitHub Pages.

```
Contexto: VSL Landing Page de KanbanPro lista para QA.
Branch: claude/upgrade-vsl-landing-page-yF8WE
Lee docs/GTM-ROADMAP.md para contexto completo.

Ejecuta el checklist completo de ui-ux-pro-max (está en docs/GTM-ROADMAP.md
sección "Checklist pre-entrega") sobre el index.html actual.

Auditoría específica — revisa y corrige cada uno:

MOBILE (375px):
- ¿Hay scroll horizontal? → corregir overflow
- ¿Todos los botones tienen min-h-[44px]? → agregar si falta
- ¿El H1 del hero cabe sin overflow? → ajustar text-size
- ¿La tabla comparativa es legible? → convertir a cards si no

ACCESIBILIDAD:
- ¿Todos los botones icon-only tienen aria-label? → agregar
- ¿Las imágenes tienen alt descriptivo? → agregar
- ¿Los inputs (si hay) tienen label? → verificar
- ¿El contraste teal #00e6c7 sobre navy #1a1a2e cumple 4.5:1? → verificar

PERFORMANCE:
- ¿Las imágenes below-the-fold tienen loading="lazy"? → agregar
- ¿Las fonts usan display=swap? → verificar
- ¿Hay CSS bloqueante innecesario? → mover si aplica

INTERACCIÓN:
- ¿Todos los links/cards tienen cursor-pointer? → agregar
- ¿Los hover states tienen transition-colors duration-200? → verificar
- ¿El modal cierra con Escape y click en backdrop? → verificar JS

LINKS:
- ¿El link de Hotmart es exactamente https://pay.hotmart.com/I97237386O ? → verificar
- ¿El WhatsApp link es correcto? → verificar
- ¿El YouTube ID es Ek2lHQ7K7Nk? → verificar

Después de todos los fixes:
1. Commitea con mensaje "fix: S4 — QA mobile, a11y, performance audit"
2. Push al branch: git push -u origin claude/upgrade-vsl-landing-page-yF8WE
3. Reporta: lista de fixes aplicados + confirmación de push exitoso
```

---

## Prompt de emergencia — Sección específica

> Usa este prompt si una sección específica necesita ser reescrita sin tocar el resto.

```
Contexto: VSL Landing Page KanbanPro.
Branch: claude/upgrade-vsl-landing-page-yF8WE
Lee docs/GTM-ROADMAP.md para contexto completo.

Necesito que reescribas SOLO la sección [NOMBRE DE SECCIÓN] del index.html.

Problema: [describe qué está mal]
Criterio de éxito: [describe cómo debe quedar]

Conserva el resto del archivo exactamente igual.
Commitea con mensaje "fix: rewrite [nombre-sección] section"
```

---

## Prompt de deploy

> Usa este prompt para deployar a GitHub Pages una vez el branch esté aprobado.

```
El branch claude/upgrade-vsl-landing-page-yF8WE del repo RodrigoInfante48/kanbanpro-vsl
está listo para merge a main.

1. Verifica que no haya conflictos con main
2. Hace merge del branch al main
3. Confirma que el index.html en main tiene la versión nueva
4. Reporta la URL de GitHub Pages cuando esté live
```

---

## Notas de token management

- **Sesión 2 y 3** son las más pesadas — hacerlas con el repo fresco (sin mucho contexto previo)
- **No acumules conversación** antes de los prompts S2 y S3 — ábrelos en sesión limpia
- Si Claude se queda a mitad de un archivo grande, usa: `"Continúa desde donde quedaste, 
  escribe desde la sección [X], el archivo ya tiene hasta [Y]"`
- El prompt de emergencia es para arreglos quirúrgicos sin gastar tokens en reescribir todo
