# KanbanPro — Plan de Skills Claude (Battle Plan)

> Generado: 2026-03-10
> Contexto: Análisis de 17 skills de Claude contra los objetivos de negocio de KanbanPro
> Propósito: Roadmap priorizado de qué herramientas usar, cuándo y para qué — sin relleno

---

## Resumen ejecutivo

KanbanPro opera con un funnel de 3 pasos: **Google Maps → WhatsApp outreach → Hotmart ($22 USD)**. El cuello de botella no es el producto — es la fricción entre el primer contacto y la decisión de compra. Los skills de Claude se usan para eliminar esa fricción con assets profesionales, repetibles y medibles.

---

## TIER 1 — Impacto directo en ingresos (ejecutar esta semana)

### 1. `theme-factory` — KanbanPro brand una sola vez
**Ejecutar primero.** Define el tema visual de KanbanPro una vez y se aplica a todo lo demás.

- **Colores:** Teal `#00e6c7` / Gold `#FFB800` / Dark `#1a1a2e`
- **Tipografía:** Inter o Poppins para títulos, sistema para body
- **Output:** Tema reutilizable para pptx, pdf, docx sin rehacer diseño

**Por qué primero:** Todos los assets que vienen después heredan este tema. Hacerlo al revés significa rediseñar cada asset por separado.

---

### 2. `pdf` — One-pager para WhatsApp
**Asset de mayor ROI por unidad de tiempo invertido.**

- 1 página, optimizada para móvil (lectura en pantalla de 6 pulgadas)
- Secciones: problema → solución Kanban → precio anclado → QR a Hotmart
- Número directo: +57 320 997 4750
- Se genera una vez, se ajusta en 5 min por industria (restaurante / clínica / gym)
- Peso < 500KB para envío sin fricciones por WhatsApp

**Iteración:** Una versión por tipo de negocio (4 versiones = cubre el 80% de prospectos en Chapinero/Usaquén)

---

### 3. `pptx` — Pitch deck B2B en español
**Para cuando el prospecto pide "más información".**

- 8-10 slides, colores KanbanPro, sin texto denso
- Estructura: Problema → DMAIC/Kanban → Demo visual → Precio → CTA
- Pain point específico por industria en slide 2
- Slide final: precio $22 USD vs competidores ($124.90+/mes)
- Se envía como adjunto en WhatsApp o como link de Drive

**Iteración:** Mismo deck, solo cambia slide 2 (problema) y slide 3 (caso de uso) por industria.

---

### 4. `xlsx` — Tracker de 28 prospectos/semana
**Sin datos no hay decisiones. Sin decisiones no hay escala.**

Columnas clave:
| Campo | Uso |
|---|---|
| Nombre negocio | Identificación |
| Tipo (restaurant/gym/clínica) | Segmentación |
| Barrio | Concentración geográfica |
| Fecha primer contacto | Cadencia follow-up |
| Material enviado (one-pager / deck / nada) | A/B de assets |
| Estado (frío / tibio / caliente / compró) | Funnel |
| Próximo follow-up | Automatización de agenda |
| Canal de entrada | Google Maps / referido / orgánico |

Fórmulas incluidas:
- Tasa de conversión por barrio
- Tasa de conversión por tipo de negocio
- Días promedio de cierre
- Ingresos proyectados (contactos × tasa × $22)

**Revisión:** Solo leer columna "Estado" y "Próximo follow-up" el viernes. 10 minutos.

---

## TIER 2 — Posicionamiento y autoridad (semanas 2-4)

### 5. `frontend-design` — Mejoras incrementales al landing VSL
No reconstruir. Iterar secciones específicas:

- [ ] Sección de caso de uso real ("Así lo usa una clínica en Chapinero")
- [ ] Bloque de testimonios con foto + nombre + ciudad + tipo de negocio
- [ ] Modal exit-intent en español con urgencia ("Oferta por tiempo limitado")
- [ ] Optimización mobile del VSL player (above the fold)

**Cómo usar el skill:** Un task a la vez. Un cambio = un commit. Nunca reconstruir todo junto.

---

### 6. `canvas-design` — Assets para LinkedIn/Redes
Construir autoridad como "data guru + Six Sigma":

- Infografía: "DMAIC explicado en 5 pasos para dueños de negocio"
- Comparativa: "PostgreSQL gratis vs Minitab $3,000/año"
- Serie: "Semana 1 con Kanban: qué cambia en tu equipo"
- Formato: vertical para LinkedIn (1200x1500), cuadrado para Instagram (1080x1080)

**Cadencia:** 2 posts/semana = 8 assets/mes. Batch de producción mensual con `canvas-design`.

---

## TIER 3 — Automatización (cuando llegues a 10+ ventas/mes)

### 7. `claude-api` — Generador de mensajes personalizados
Script que toma: `{tipo_negocio}` + `{barrio}` → genera mensaje de WhatsApp con dolor específico.

```
Input:  tipo="restaurante", barrio="Chapinero"
Output: "Rodrigo, ¿cuántos pedidos se pierden entre cocina y salón
         en hora pico? KanbanPro te da un tablero en tiempo real..."
```

Mismo producto, dolor específico. Escala sin bajar calidad del mensaje.

---

### 8. `skill-creator` — Skill propio de KanbanPro Outreach
Encapsular el mensaje que convierte (con datos del xlsx) como skill reutilizable.

- Input: tipo de negocio + barrio + stage del funnel
- Output: mensaje WhatsApp / seguimiento / cierre
- Sin variación de calidad en 100 mensajes/semana

---

## Skills descartados (y por qué)

| Skill | Razón |
|---|---|
| `algorithmic-art` | Arte generativo, cero aplicación en ventas B2B |
| `internal-comms` | Para equipos. Operación es unipersonal. |
| `slack-gif-creator` | No está en el stack tecnológico actual |
| `mcp-builder` | Alta complejidad de setup, bajo retorno inmediato |
| `webapp-testing` | Solo si hay desarrollo activo de features en el landing |
| `doc-coauthoring` | Para escritura colaborativa, no aplica |

---

## Flujo compuesto — El sistema completo

```
[1] theme-factory
      ↓ (tema KanbanPro definido)
[2] pdf (one-pager por industria)  +  [3] pptx (deck B2B)  +  [4] xlsx (tracker)
      ↓
WhatsApp outreach (28 contactos/semana)
      ↓
Hotmart → $22 USD
      ↓ (con datos de conversión del xlsx)
[7] claude-api → mensajes personalizados → escala sin fricción
```

---

## Orden de ejecución

```
Semana 1:  theme-factory → pdf (one-pager) → xlsx (tracker)
Semana 2:  pptx (pitch deck) → outreach activo con materiales
Semana 3:  frontend-design (mejora landing) + canvas-design (primer batch LinkedIn)
Semana 4+: medir conversión con xlsx → iterar assets que no convierten
Mes 2+:    claude-api si el volumen lo justifica
```

---

## KPIs para saber si está funcionando

| Métrica | Objetivo semana 4 | Dónde medirla |
|---|---|---|
| Tasa respuesta WhatsApp | > 40% | xlsx |
| Tasa conversión a venta | > 5% de contactados | xlsx |
| Ventas/semana | ≥ 2 | Hotmart dashboard |
| Barrio con mejor conversión | Identificado | xlsx (fórmula) |
| Tipo negocio con mejor conversión | Identificado | xlsx (fórmula) |

---

*Documento vivo — actualizar al final de cada semana con aprendizajes del tracker.*
