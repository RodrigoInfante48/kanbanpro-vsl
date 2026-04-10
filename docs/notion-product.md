# KanbanPro — Estructura Completa del Producto en Notion

> Este archivo es el contexto completo del producto para cualquier IA que trabaje en el repo.
> Extraído directamente de Notion el 2026-04-09.

---

## Arquitectura del Bundle ($22 USD único)

El bundle KanbanPro consta de 3 componentes entregados como plantillas de Notion:

### 1. 🧠 Visual Board (Producto Principal)

**Descripción:** Gestor multidimensional personal. Un dashboard central que conecta ideas → objetivos → proyectos → tareas → notas en un solo lugar.

**Estructura del Visual Board:**

```
Visual Board/
├── Quick Capture (5 botones de captura rápida)
├── Control Panel/
│   ├── General Data
│   └── Notes Panel
├── Productivity/
│   ├── Inbox
│   ├── Tasks
│   ├── Projects
│   ├── Objectives
│   ├── Areas
│   └── Events
├── Knowledge/
│   ├── Notes
│   ├── Destacados
│   ├── Referencias
│   ├── Temas
│   ├── Libros
│   ├── Archivo
│   ├── Bases de datos
│   └── Migración
├── Databases visibles en columna derecha:
│   ├── View of Tareas (inline)
│   ├── View of Proyectos (inline)
│   ├── View of Objetivos (inline)
│   ├── View of Areas (inline)
│   ├── Notes (inline)
│   └── Habit Tracker (inline)
```

**Propuesta de valor:** "Ve tus ideas, objetivos, proyectos y tareas en un solo lugar — y trabaja desde tu celular."

---

### 2. 🧩 KanbanPro (Bono 1 — valor $22)

**Descripción:** Sistema de gestión de proyectos B2B con metodología Six Sigma DMAIC + Kanban + Kaizen.

**Base de datos KanbanPro — Schema:**

```
Tabla: Kanbanpro
├── Subproceso (título — nombre del paso/tarea)
├── Status: Sin empezar | En curso | Listo
├── Tags (multi-select): 
│   ├── Project Charter
│   ├── Definir
│   ├── Medir
│   ├── CTQ
│   ├── Analizar
│   ├── Mejorar
│   └── Controlar
├── Fecha inicio (date)
├── Fecha fin (date)
├── Owner (person)
└── Notebook Copilot (url)
```

**Vistas disponibles (Board/Gallery):**
1. **DMAIC** — Vista galería con todos los subprocesos
2. **Definir** — Board filtrado por tag "Definir", agrupado por Status
3. **Medir** — Board filtrado por tag "Medir", agrupado por Status
4. **Analizar** — Board filtrado por tag "Analizar", agrupado por Status
5. **Mejorar** — Board filtrado por tag "Mejorar", agrupado por Status
6. **Controlar** — Board filtrado por tag "Controlar", agrupado por Status

**Diferenciador clave:** La fase Medir incluye un stack ETL gratuito (PostgreSQL + Python + Power BI local) eliminando costos de licenciamiento vs Minitab ($3,000+/año).

---

### 3. 📓 Notion Blueprint (Bono 2 — valor $22)

**Descripción:** Guía organizacional completa para monetizar habilidades con sistemas Notion. Funciona como el "pegamento operativo" que sincroniza datos entre móvil y desktop.

**Contiene:** Base de datos "Notion Blueprint" con recursos y guías paso a paso.

---

## Copias del Producto en Notion

Existen 3 copias del producto para diferentes propósitos:

| Copia | Propósito |
|-------|-----------|
| **Free Trial** | Versión de prueba para activación vía WhatsApp (8 días) |
| **Published** | Versión final entregada al comprador vía Hotmart |
| **Phone Gadget** | Versión optimizada para demo en móvil |

---

## Productos Complementarios (Bots)

### VetBot
- Pipeline: Tally form → Gemini AI → Notion
- Genera recursos personalizados para clínicas veterinarias
- URL Tally: https://tally.so/r/aQ0oLB

### DentBot
- Mismo patrón que VetBot adaptado para consultorios dentales

---

## FAQ Oficial del Producto

### ¿Qué es KanbanPro?
KanbanPro es un potente gestor de proyectos que utiliza una filosofía Kaizen, un sistema Kanban y una metodología DMAIC, todo en uno.

### ¿Es esta herramienta adecuada para mi?
Es para ti si:
- Estás luchando con la baja productividad
- Quieres aumentar tu tiempo pero no sabes por dónde empezar
- Eres un creador empresarial o individual que busca apoyo
- Trabajas en un equipo ágil y en constante evolución
- Estás intentando delegar funciones a otras personas

### ¿Qué habilidades necesitas?
Dirigida a ejecutivos de todo el espectro, desde estudiantes jr hasta empresas.

### ¿Qué herramientas necesito?
Solo un teléfono inteligente y una computadora (por comodidad).

### ¿Cuánto tiempo tarda la curva de aprendizaje?
Diseño UX/UI en patrón F:
- Progresivo: 1 semana (1-2 lecciones/día)
- Intensivo: 2 días

### Garantía de satisfacción
- 7 días desde la fecha de compra
- Reembolso parcial en cuotas mensuales durante 6 meses
- Solicitar vía WhatsApp: +57 320 997 4750

---

## Funnel de Ventas

```
Redes sociales (IG/TikTok/LinkedIn)
    ↓
Linktree (linktr.ee/DailyDuty)
    ↓
Landing VSL (rodrigoinfante48.github.io/kanbanpro-vsl)
    ↓
Hotmart checkout ($22 USD) — https://pay.hotmart.com/I97237386O
    ↓
Entrega automática (Notion template link)
```

**Activación alternativa:** WhatsApp → Free Trial 8 días → Conversión

---

## Links Críticos

| Recurso | URL |
|---------|-----|
| Checkout Hotmart | https://pay.hotmart.com/I97237386O |
| WhatsApp | https://api.whatsapp.com/send/?phone=573209974750&text=Kanbanpro |
| Linktree | https://linktr.ee/DailyDuty |
| Landing VSL | https://rodrigoinfante48.github.io/kanbanpro-vsl/ |
| Visual Board (público) | https://kanbanpro.notion.site/Visual-Board-2ff4f515cfb080c095d1ed72b2442c6f |
| Google Analytics | G-M08G3EFVMM |
| YouTube VSL | Ek2lHQ7K7Nk |
| Telegram Bot | https://t.me/Dailyduty48_bot?start=info |
| VetBot Tally | https://tally.so/r/aQ0oLB |

---

## Brand Identity

| Token | Valor |
|-------|-------|
| Marca principal | DailyDuty / Instituto para el Desarrollo Diario |
| Producto | KanbanPro |
| Primary color (teal) | #00e6c7 |
| Gold | #FFB800 |
| Dark Navy | #1a1a2e |
| Surface | #16213e |
| Font | Plus Jakarta Sans |
| Precio | $22 USD único |
| Garantía | 7-8 días |
| Métodos de pago | Tarjeta, Efecty, Nequi, PSE, PayPal |
| Idioma principal | Español (tuteo) |
