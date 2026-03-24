#!/usr/bin/env python3
"""
KanbanPro — One-Pager Clinica Veterinaria
DMAIC + Kanban + Kaizen aplicados a veterinarias
Target: Propietarios de clinica veterinaria en Chapinero / Usaquen, Bogota
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

# ─────────────────────────────────────────────
# BRAND — KanbanPro
# ─────────────────────────────────────────────
DARK_NAVY  = HexColor('#1a1a2e')
DARK_SURF  = HexColor('#16213e')
TEAL       = HexColor('#00e6c7')
GOLD       = HexColor('#FFB800')
WHITE      = HexColor('#ffffff')
GRAY       = HexColor('#9ca3af')
RED_DIM    = HexColor('#ff6b6b')
TEAL_DIM   = HexColor('#00b8a0')

# Colores metodologias
COLOR_KANBAN  = HexColor('#00e6c7')   # Teal — Kanban visual
COLOR_6SIGMA  = HexColor('#818cf8')   # Indigo — 6 Sigma
COLOR_KAIZEN  = HexColor('#34d399')   # Esmeralda — Kaizen mejora continua
COLOR_DMAIC   = HexColor('#FFB800')   # Gold — DMAIC control

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'kanbanpro-vet-onepager.pdf')
W, H = A4   # 595 x 842 pt

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def bg(cv, x, y, w, h, color):
    cv.setFillColor(color)
    cv.rect(x, y, w, h, fill=1, stroke=0)

def txt(cv, t, x, y, font='Helvetica', size=10, color=WHITE, align='left'):
    cv.setFillColor(color)
    cv.setFont(font, size)
    if align == 'center':
        cv.drawCentredString(x, y, t)
    elif align == 'right':
        cv.drawRightString(x, y, t)
    else:
        cv.drawString(x, y, t)

def checkmark(cv, cx, cy, sz, color):
    cv.setStrokeColor(color)
    cv.setLineWidth(sz * 0.22)
    cv.setLineCap(1)
    path = cv.beginPath()
    path.moveTo(cx - sz * 0.45, cy)
    path.lineTo(cx - sz * 0.05, cy - sz * 0.42)
    path.lineTo(cx + sz * 0.52, cy + sz * 0.38)
    cv.drawPath(path, stroke=1, fill=0)

def method_badge(cv, x, y, label, color):
    """Dibuja un badge de metodologia (ej: KANBAN, 6 SIGMA, KAIZEN, DMAIC)."""
    badge_w = 56
    badge_h = 13
    cv.setFillColor(color)
    cv.roundRect(x, y, badge_w, badge_h, 3, fill=1, stroke=0)
    cv.setFillColor(DARK_NAVY)
    cv.setFont('Helvetica-Bold', 6.5)
    cv.drawCentredString(x + badge_w / 2, y + 3.5, label)

def benefit_row(cv, y, label, desc, idx, method_tag=None, method_color=None):
    row_color = DARK_NAVY if idx % 2 == 0 else DARK_SURF
    bg(cv, 0, y - 14, W, 50, row_color)
    cv.setFillColor(TEAL)
    cv.circle(46, y + 16, 11, fill=1, stroke=0)
    checkmark(cv, 46, y + 16, 10, DARK_NAVY)
    label_y = y + 13 if not desc else y + 20
    txt(cv, label, 68, label_y, 'Helvetica-Bold', 10.5, WHITE)
    if desc:
        txt(cv, desc, 68, y + 6, 'Helvetica', 8.5, GRAY)
    if method_tag and method_color:
        method_badge(cv, W - 74, y + 12, method_tag, method_color)


# ─────────────────────────────────────────────
# CANVAS
# ─────────────────────────────────────────────
cv = canvas.Canvas(OUTPUT, pagesize=A4)
cv.setTitle('KanbanPro — Sistema de Gestion para Tu Clinica Veterinaria')
cv.setAuthor('KanbanPro')
cv.setSubject('One-Pager Propuesta Comercial Veterinaria | DMAIC + Kanban + Kaizen')

# ════════════════════════════════════════════════
# 1. FONDO GENERAL
# ════════════════════════════════════════════════
bg(cv, 0, 0, W, H, DARK_NAVY)

# ════════════════════════════════════════════════
# 2. HEADER  (sin drivers de categoria)
# ════════════════════════════════════════════════
HEADER_H = 128
bg(cv, 0, H - HEADER_H, W, HEADER_H, TEAL)
bg(cv, 0, H - 8, W, 8, TEAL_DIM)

txt(cv, 'KanbanPro', W/2, H - 52, 'Helvetica-Bold', 40, DARK_NAVY, 'center')

cv.setStrokeColor(DARK_NAVY)
cv.setLineWidth(0.8)
cv.setDash(4, 4)
cv.line(60, H - 72, W - 60, H - 72)
cv.setDash()

txt(cv, 'Gestion visual para tu veterinaria — Sin caos operativo',
    W/2, H - 92, 'Helvetica-Bold', 11.5, DARK_SURF, 'center')

badge_x = W/2 - 60
cv.setFillColor(GOLD)
cv.roundRect(badge_x, H - 118, 120, 18, 6, fill=1, stroke=0)
txt(cv, 'USD 22  |  Pago unico de por vida', W/2, H - 113,
    'Helvetica-Bold', 8.5, DARK_NAVY, 'center')

# ════════════════════════════════════════════════
# 3. BLOQUE PROBLEMA  (icono 6S + referencias metodologicas)
# ════════════════════════════════════════════════
PAIN_TOP = H - HEADER_H
PAIN_H   = 112
bg(cv, 0, PAIN_TOP - PAIN_H, W, PAIN_H, DARK_SURF)

# Circulo con icono de advertencia
cv.setFillColor(GOLD)
cv.circle(50, PAIN_TOP - PAIN_H/2, 18, fill=1, stroke=0)
txt(cv, '!', 50, PAIN_TOP - PAIN_H/2 - 7, 'Helvetica-Bold', 22, DARK_NAVY, 'center')

txt(cv, 'El caos real de tu veterinaria hoy:',
    80, PAIN_TOP - 24, 'Helvetica-Bold', 11.5, GOLD)
txt(cv, 'Tu clinica funciona, pero tu cabeza carga con todo el sistema.',
    80, PAIN_TOP - 46, 'Helvetica', 10, WHITE)

# Linea divisora metodologias
cv.setStrokeColor(HexColor('#2a3a4a'))
cv.setLineWidth(0.5)
cv.line(80, PAIN_TOP - 82, W - 40, PAIN_TOP - 82)

# Badges metodologias combinadas
method_badge(cv, 82,  PAIN_TOP - 100, 'DMAIC', COLOR_DMAIC)
method_badge(cv, 146, PAIN_TOP - 100, 'KANBAN', COLOR_KANBAN)
method_badge(cv, 210, PAIN_TOP - 100, 'KAIZEN', COLOR_KAIZEN)
txt(cv, '— 3 metodologias. 1 sistema. Para tu veterinaria.',
    276, PAIN_TOP - 93, 'Helvetica', 7.5, GRAY)

# ════════════════════════════════════════════════
# 4. BENEFICIOS — 4 filas con etiqueta de metodologia
# ════════════════════════════════════════════════
BENEFITS_TOP = PAIN_TOP - PAIN_H - 10

benefits = [
    ('Tablero Kanban de citas y cirugias en tiempo real',
     '',
     'KANBAN', COLOR_KANBAN),
    ('Medicion 6 Sigma: sin errores, todo es visible.',
     '',
     '6 SIGMA', COLOR_6SIGMA),
    ('Kaizen: Coordinacion mobile first, mejora continua dia a dia.',
     '',
     'KAIZEN', COLOR_KAIZEN),
    ('DMAIC: estandariza tus tareas clinicas diarias',
     'Define, mide y controla: esterilizacion, limpieza y seguimientos',
     'DMAIC', COLOR_DMAIC),
]

for i, (label, desc, tag, tag_color) in enumerate(benefits):
    row_y = BENEFITS_TOP - (i * 52)
    benefit_row(cv, row_y, label, desc, i, tag, tag_color)

# ════════════════════════════════════════════════
# 5. BLOQUE PRECIO
# ════════════════════════════════════════════════
CTA_H     = 108
PRICE_TOP = BENEFITS_TOP - (len(benefits) * 52) - 18
PRICE_H   = PRICE_TOP - CTA_H
bg(cv, 0, CTA_H, W, PRICE_H, DARK_SURF)

cv.setStrokeColor(TEAL)
cv.setLineWidth(2)
cv.line(40, PRICE_TOP, W - 40, PRICE_TOP)

mid = CTA_H + PRICE_H / 2

txt(cv, 'Compara antes de decidir:', W/2, mid + 82,
    'Helvetica-Bold', 12, WHITE, 'center')

comp_str = 'Competidores: USD 124.90 / mes (o mas)'
cv.setFont('Helvetica', 10.5)
cv.setFillColor(GRAY)
str_w  = cv.stringWidth(comp_str, 'Helvetica', 10.5)
comp_x = W/2 - str_w/2
cv.drawString(comp_x, mid + 56, comp_str)
cv.setStrokeColor(RED_DIM)
cv.setLineWidth(1.5)
cv.line(comp_x, mid + 60, comp_x + str_w, mid + 60)

cv.setStrokeColor(TEAL_DIM)
cv.setLineWidth(0.5)
cv.setDash(3, 6)
cv.line(W/2 - 80, mid + 40, W/2 + 80, mid + 40)
cv.setDash()

txt(cv, 'USD 22', W/2, mid - 12,
    'Helvetica-Bold', 52, GOLD, 'center')
txt(cv, 'Pago unico  ·  Sin mensualidades  ·  Acceso de por vida',
    W/2, mid - 32, 'Helvetica', 9, GRAY, 'center')

cv.setFillColor(HexColor('#1f3a2e'))
cv.roundRect(W/2 - 120, mid - 62, 240, 22, 6, fill=1, stroke=0)
txt(cv, 'Soporte incluido  ·  Sin contrato  ·  Cancelable cuando quieras',
    W/2, mid - 55, 'Helvetica', 7.5, HexColor('#4ade80'), 'center')

# ════════════════════════════════════════════════
# 6. CTA FOOTER
# ════════════════════════════════════════════════
bg(cv, 0, 0, W, CTA_H, TEAL)

cv.setStrokeColor(GOLD)
cv.setLineWidth(2.5)
cv.line(0, CTA_H, W, CTA_H)

txt(cv, 'Escribeme — Te explico en 2 minutos como implementarlo',
    W/2, CTA_H - 26, 'Helvetica-Bold', 12, DARK_NAVY, 'center')

cv.setFillColor(DARK_NAVY)
cv.roundRect(W/2 - 150, CTA_H - 66, 300, 30, 9, fill=1, stroke=0)
txt(cv, 'WhatsApp: +57 320 997 4750',
    W/2, CTA_H - 56, 'Helvetica-Bold', 13, TEAL, 'center')

txt(cv, 'Disponible en hotmart.com  ·  kanbanpro.co',
    W/2, CTA_H - 82, 'Helvetica', 9, DARK_SURF, 'center')

txt(cv, 'KanbanPro — DMAIC + Kanban + Kaizen para veterinarias, gyms y negocios que crecen con orden.',
    W/2, 10, 'Helvetica', 6.5, DARK_SURF, 'center')

# ─────────────────────────────────────────────
# GUARDAR
# ─────────────────────────────────────────────
cv.save()
print(f'[OK] PDF generado: {OUTPUT}')
