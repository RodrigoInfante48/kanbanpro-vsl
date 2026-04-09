# GTM Roadmap — Visual Board VSL Landing Page
**Proyecto:** KanbanPro VSL — Upgrade completo
**Repo:** RodrigoInfante48/kanbanpro-vsl
**Branch activo:** `claude/upgrade-vsl-landing-page-yF8WE`
**Meta:** Landing page que convierte tráfico frío de Instagram/TikTok a $22 USD/venta

---

## Resumen ejecutivo

Estamos rediseñando la VSL landing page de KanbanPro de cero. El cambio no es cosmético — es un cambio de ángulo de venta completo: de "herramienta Six Sigma técnica" a "sistema de ejecución personal desde tu celular". El producto principal pasa a ser **Visual Board** ($22 USD único) con KanbanPro y Notion Blueprint como bonos de valor.

---

## Estado actual del proyecto

| Item | Estado |
|------|--------|
| Rama de desarrollo creada | ✅ `claude/upgrade-vsl-landing-page-yF8WE` |
| Design system generado (ui-ux-pro-max) | ✅ |
| Plan aprobado por Rod | ✅ |
| Estructura de prompts documentada | ✅ |
| index.html nuevo — sección HEAD + Hero | ⬜ Pendiente Sesión 2 |
| index.html nuevo — secciones 3 a 6 | ⬜ Pendiente Sesión 3 |
| index.html nuevo — secciones 7 a 10 + JS | ⬜ Pendiente Sesión 4 |
| QA mobile + accesibilidad + push final | ⬜ Pendiente Sesión 5 |

---

## Arquitectura de la página (10 secciones)

```
1.  HERO           Hook de dolor + CTA primario + phone mockup
2.  VSL VIDEO      Embed YouTube con thumbnail clickeable
3.  PROBLEMA       Agitación del dolor (3 puntos)
4.  SOLUCIÓN       Visual Board como producto principal
5.  BONOS          KanbanPro + Notion Blueprint valorados
6.  COMPARATIVA    Tabla vs Monday / Asana / Minitab
7.  GARANTÍA       8 días, sin preguntas, badge visual
8.  PRUEBA SOCIAL  4 testimonios + stats (120+ · 4.8★)
9.  FAQ            5 preguntas que eliminan objeciones
10. CTA FINAL      Urgencia + countdown + precio + botón grande
    + Sticky bar, Footer, Modal VSL, JS
```

---

## Design system aprobado

### Paleta
| Token | Hex | Uso |
|-------|-----|-----|
| Primary (teal) | `#00e6c7` | CTAs, acentos, iconos |
| Gold | `#FFB800` | Precio, urgencia, estrellas |
| Dark Navy | `#1a1a2e` | Fondo principal |
| Surface | `#16213e` | Cards, secciones alternas |
| White | `#ffffff` | Texto principal |
| Gray | `#9ca3af` | Texto secundario |
| Red Dim | `#ff6b6b` | Precios tachados competidores |
| Green | `#4ade80` | Garantía, badges confianza |

### Tipografía
- **Plus Jakarta Sans** 300/400/600/700/800
- Google Fonts: `https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&display=swap`

### Pattern de conversión
**Scroll-Triggered Storytelling** — narrativa en capítulos, cada sección con temperatura visual propia, mini-CTAs al final de cada capítulo, CTA climático al final.

### Stack técnico
- HTML + Tailwind CDN (sin build step, sin frameworks)
- Solo español (se elimina el sistema i18n)
- Animaciones con `IntersectionObserver` puro (sin GSAP)
- `prefers-reduced-motion` respetado

---

## Links críticos (conservar exactos)

```
Checkout:   https://pay.hotmart.com/I97237386O
WhatsApp:   https://api.whatsapp.com/send/?phone=573209974750&text=Kanbanpro&type=phone_number&app_absent=0
Linktree:   https://linktr.ee/DailyDuty
GA Tag:     G-M08G3EFVMM
YT Video:   Ek2lHQ7K7Nk
```

---

## Copy aprobado por sección

### HERO
```
Eyebrow: "120+ personas ya lo usan · 4.8★"
H1:      Tienes 100 ideas, 20 proyectos a medias y 0 sistemas.
Sub:     3 herramientas en Notion para pasar del caos a la ejecución
         — desde tu celular.
CTA:     Quiero el acceso por $22 →
Micro:   Solo 28 accesos disponibles este mes
```

### PROBLEMA
```
H2:  Todo está en tu cabeza. Nada está en un sistema.
P1:  Abres Notion y no sabes por dónde empezar.
P2:  Tienes 3 apps distintas para proyectos, tareas e ideas.
P3:  Al final del día sientes que trabajaste mucho pero avanzaste poco.
```

### SOLUCIÓN (Visual Board)
```
H2:  Visual Board — tu sistema de ejecución personal
Sub: El gestor multidimensional que te permite ver tus ideas, objetivos,
     proyectos y tareas en un solo lugar — y trabajar desde tu celular.
```

### BONOS
```
Bono 1 — KanbanPro (valor $22):
"Ya tienes tus objetivos claros. Ahora gestiona cada proyecto con
metodología real."

Bono 2 — Notion Blueprint (valor $22):
"El pegamento operativo para que todo funcione sin fricción entre
tu celular y tu laptop."

Cierre: Total de valor: $66. Tú pagas: $22.
```

### COMPARATIVA
```
                   Visual Board   Monday Pro   Asana Pro   Minitab
Precio mensual          —          $124.90      $149.00     $250+
Pago único           $22 ✓           ✗             ✗          ✗
Mobile-first           ✓          Parcial       Parcial       ✗
Sin código             ✓             ✗             ✗           ✗
Bonos incluidos        3             0             0           0
```

### GARANTÍA
```
8 días para probarlo sin riesgo.
Si no es para ti, te devuelvo cada centavo.
Sin formularios. Sin preguntas.
```

### FAQ (5 preguntas)
```
1. ¿Necesito saber usar Notion? → No, viene listo para duplicar.
2. ¿Funciona en iOS y Android? → Sí, 100% mobile-first.
3. ¿Qué pasa si Notion sube de precio? → La plantilla siempre es tuya.
4. ¿Es para empresas o personas? → Para solopreneurs y freelancers.
5. ¿Cuánto tarda la entrega? → Acceso inmediato al pagar en Hotmart.
```

---

## Checklist pre-entrega (ui-ux-pro-max)

- [ ] Sin emojis como iconos — usar SVG (Heroicons/Lucide)
- [ ] `cursor-pointer` en todos los elementos clickeables
- [ ] Hover states con transición 150-300ms
- [ ] Contraste de texto ≥ 4.5:1
- [ ] Focus states visibles (teclado)
- [ ] `prefers-reduced-motion` respetado
- [ ] Touch targets mínimo 44x44px
- [ ] Sin scroll horizontal en mobile
- [ ] Responsive: 375px · 768px · 1024px · 1440px
- [ ] Todas las imágenes con `alt` descriptivo
- [ ] `loading="lazy"` en imágenes below-the-fold

---

*Última actualización: Sesión 1 — Diseño y arquitectura aprobados*
