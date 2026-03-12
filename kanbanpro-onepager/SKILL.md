---
name: kanbanpro-onepager
description: >
  Genera one-pagers PDF de KanbanPro listos para enviar por WhatsApp, ajustados
  al sector o tipo de negocio que se indique. Usa este skill siempre que Rodrigo
  pida crear, generar o actualizar un one-pager, PDF de propuesta, o documento de
  ventas para cualquier industria — gyms, veterinarias, restaurantes, estéticas,
  academias, talleres mecánicos, o cualquier otro sector que mencione. También
  úsalo cuando quiera agregar una industria nueva a la librería de one-pagers, o
  cuando diga "regenera todos los PDFs". El output es un archivo PDF de ~4 KB
  optimizado para WhatsApp, con el branding KanbanPro (teal/gold/navy).
---

# KanbanPro One-Pager Skill

Genera un PDF profesional de una sola página para cualquier tipo de negocio,
usando el motor en `generate_onepager.py`. El PDF tiene branding KanbanPro
consistente — solo cambia el contenido por industria.

## Ruta del motor

```
C:\Users\rodri\OneDrive\Documents\DD\stitch_kanbanpro_vsl_landing_page\generate_onepager.py
```

## Industrias disponibles (listas para usar)

| Clave        | Sector                                    |
|--------------|-------------------------------------------|
| `gym`        | Gyms, CrossFit, centros de fitness        |
| `vet`        | Clínicas veterinarias                     |
| `estetica`   | Estéticas, spas, salones de belleza       |
| `restaurante`| Restaurantes, cafés, negocios de comida   |
| `academia`   | Academias de idiomas, baile, tutorías     |

## Flujo de trabajo

### Caso 1 — Industria ya existe en la librería

```bash
cd "C:\Users\rodri\OneDrive\Documents\DD\stitch_kanbanpro_vsl_landing_page"
python generate_onepager.py [clave]
# Ejemplo: python generate_onepager.py gym
```

El PDF se guarda en la misma carpeta como `kanbanpro-[clave]-onepager.pdf`.

### Caso 2 — Industria nueva (no está en la lista)

1. Leer `generate_onepager.py` y encontrar el dict `INDUSTRIES`
2. Agregar una nueva entrada siguiendo exactamente la estructura de las existentes:

```python
'clave_nueva': {
    'filename':     'kanbanpro-[clave]-onepager.pdf',
    'meta_title':   'KanbanPro — Sistema de Gestion para Tu [Negocio]',
    'tagline':      'Gestion visual para tu [negocio] — [beneficio clave]',
    'sub_tags':     'Area1  ·  Area2  ·  Area3  ·  Area4',
    'pain_title':   'El [problema/caos] real de tu [negocio] hoy:',
    'pain_lines':   [
        'Primera línea del dolor — situación concreta,',        # line 1: situación
        'segunda línea — consecuencia directa.',                 # line 2: consecuencia
        'Tercera línea más reflexiva — carga que lleva el dueño.',  # line 3: impacto emocional
    ],
    'benefits': [
        ('Beneficio 1 concreto y directo',      'Descripción de cómo lo resuelve KanbanPro'),
        ('Beneficio 2 concreto y directo',      'Descripción de cómo lo resuelve KanbanPro'),
        ('Beneficio 3 concreto y directo',      'Descripción de cómo lo resuelve KanbanPro'),
        ('Beneficio 4 concreto y directo',      'Descripción de cómo lo resuelve KanbanPro'),
    ],
    'footer_micro': 'KanbanPro — Sistema Kanban para [sector] y negocios que crecen con orden.',
},
```

**Criterios de calidad para el contenido:**
- `tagline`: máx ~55 caracteres, cabe en una línea del header
- `sub_tags`: exactamente 4 áreas clave del negocio separadas por ` · `
- `pain_title`: nombra el sector explícitamente ("de tu taller", "de tu clínica")
- `pain_lines[0-1]`: problema concreto y operativo, no genérico
- `pain_lines[2]`: tono más reflexivo — lo que el dueño carga mentalmente
- `benefits`: cada label máx ~45 chars, cada desc máx ~65 chars; deben ser específicos al sector, no genéricos
- Los textos con guiones largos (—) deben usar `\u2014` y los puntos medios (·) deben usar `\u00b7`

3. Guardar el archivo y ejecutar:
```bash
python generate_onepager.py [clave_nueva]
```

### Caso 3 — Regenerar todos

```bash
python generate_onepager.py all
```

## Después de generar

- Confirmar con la ruta del archivo y el tamaño en KB
- El PDF está listo para adjuntar en WhatsApp
- Hacer commit y push a GitHub con el PDF nuevo y el script actualizado:

```bash
cd "C:\Users\rodri\OneDrive\Documents\DD\stitch_kanbanpro_vsl_landing_page"
git add generate_onepager.py kanbanpro-[clave]-onepager.pdf
git commit -m "Add [sector] one-pager to KanbanPro library"
git push origin main
```
