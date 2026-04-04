#!/usr/bin/env python3
"""
KanbanPro — One-Pager Gym
WhatsApp-optimized PDF | KanbanPro Brand
Target: Propietarios de gym en Chapinero / Usaquen, Bogota
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
import os

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

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kanbanpro-gym-onepager.pdf')
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
    """Dibuja un check mark limpio con lineas."""
    cv.setStrokeColor(color)
    cv.setLineWidth(sz * 0.22)
    cv.setLineCap(1)
    path = cv.beginPath()
    path.moveTo(cx - sz * 0.45, cy)
    path.lineTo(cx - sz * 0.05, cy - sz * 0.42)
    path.lineTo(cx + sz * 0.52, cy + sz * 0.38)
    cv.drawPath(path, stroke=1, fill=0)

def benefit_row(cv, y, label, desc, idx):
    """Fila de beneficio con fondo alternado y checkmark."""
    row_color = DARK_NAVY if idx % 2 == 0 else DARK_SURF
    bg(cv, 0, y - 14, W, 50, row_color)

    # Circulo fondo del check
    cv.setFillColor(TEAL)
    cv.circle(46, y + 16, 11, fill=1, stroke=0)
    checkmark(cv, 46, y + 16, 10, DARK_NAVY)

    # Label
    txt(cv, label, 68, y + 20, 'Helvetica-Bold', 10.5, WHITE)
    # Desc
    txt(cv, desc, 68, y + 6, 'Helvetica', 8.5, GRAY)


# ─────────────────────────────────────────────
# CANVAS
# ─────────────────────────────────────────────
cv = canvas.Canvas(OUTPUT, pagesize=A4)
cv.setTitle('KanbanPro — Sistema de Gestion para Tu Gym')
cv.setAuthor('KanbanPro')
cv.setSubject('One-Pager Propuesta Comercial Gym')

# ════════════════════════════════════════════════
# 1. FONDO GENERAL
# ════════════════════════════════════════════════
bg(cv, 0, 0, W, H, DARK_NAVY)

# ════════════════════════════════════════════════
# 2. HEADER — Teal strip (H - 140 → H)
# ════════════════════════════════════════════════
HEADER_H = 142
bg(cv, 0, H - HEADER_H, W, HEADER_H, TEAL)

# Acento superior sutil
bg(cv, 0, H - 8, W, 8, TEAL_DIM)

# Wordmark
txt(cv, 'KanbanPro', W/2, H - 54, 'Helvetica-Bold', 40, DARK_NAVY, 'center')

# Separador
cv.setStrokeColor(DARK_NAVY)
cv.setLineWidth(0.8)
cv.setDash(4, 4)
cv.line(60, H - 74, W - 60, H - 74)
cv.setDash()

# Tagline gym
txt(cv, 'Gestion visual para tu gym — Control total desde hoy', W/2, H - 95,
    'Helvetica-Bold', 11.5, DARK_SURF, 'center')

# Sub-tags
txt(cv, 'Horarios  ·  Instructores  ·  Miembros  ·  Equipos',
    W/2, H - 118, 'Helvetica', 9, DARK_SURF, 'center')

# Badge "Pago unico"
badge_x = W/2 - 55
cv.setFillColor(GOLD)
cv.roundRect(badge_x, H - 136, 110, 18, 6, fill=1, stroke=0)
txt(cv, 'USD 22  |  Pago unico de por vida', W/2, H - 131,
    'Helvetica-Bold', 8.5, DARK_NAVY, 'center')

# ════════════════════════════════════════════════
# 3. BLOQUE PROBLEMA (dark surface)
# ════════════════════════════════════════════════
PAIN_TOP = H - HEADER_H
PAIN_H = 100
bg(cv, 0, PAIN_TOP - PAIN_H, W, PAIN_H, DARK_SURF)

# Icono advertencia
cv.setFillColor(GOLD)
cv.circle(50, PAIN_TOP - PAIN_H/2, 18, fill=1, stroke=0)
txt(cv, '!', 50, PAIN_TOP - PAIN_H/2 - 7, 'Helvetica-Bold', 22, DARK_NAVY, 'center')

# Texto problema
txt(cv, 'El problema real de tu gym:', 80, PAIN_TOP - 22,
    'Helvetica-Bold', 11.5, GOLD)
txt(cv, 'Horarios por WhatsApp, instructores sin claridad,',
    80, PAIN_TOP - 40, 'Helvetica', 10, WHITE)
txt(cv, 'miembros que se van y no sabes por que.',
    80, PAIN_TOP - 56, 'Helvetica', 10, WHITE)
txt(cv, 'Todo en tu cabeza. Nada en un sistema que lo soporte.',
    80, PAIN_TOP - 74, 'Helvetica', 9.5, GRAY)

# ════════════════════════════════════════════════
# 4. BENEFICIOS — 4 filas
# ════════════════════════════════════════════════
BENEFITS_TOP = PAIN_TOP - PAIN_H - 10

benefits = [
    ('Tablero de clases en tiempo real',
     'Ve todos los turnos del dia de un vistazo — desde tu celular'),
    ('Control de instructores sin WhatsApp caotico',
     'Cada instructor tiene su agenda clara, sin mensajes de ida y vuelta'),
    ('Seguimiento de miembros activos e inactivos',
     'Detecta quien esta por cancelar antes de que lo haga'),
    ('Gestion de equipos y zonas del gym',
     'Maquinas, limpieza y mantenimiento en un solo tablero'),
]

for i, (label, desc) in enumerate(benefits):
    row_y = BENEFITS_TOP - (i * 52)
    benefit_row(cv, row_y, label, desc, i)

# ════════════════════════════════════════════════
# 5. BLOQUE PRECIO — ocupa todo el espacio hasta CTA
# ════════════════════════════════════════════════
CTA_H = 108                          # definido aqui para el calculo dinamico
PRICE_TOP = BENEFITS_TOP - (len(benefits) * 52) - 18
PRICE_H = PRICE_TOP - CTA_H          # llena el gap exacto
bg(cv, 0, CTA_H, W, PRICE_H, DARK_SURF)

# Separador teal superior
cv.setStrokeColor(TEAL)
cv.setLineWidth(2)
cv.line(40, PRICE_TOP, W - 40, PRICE_TOP)

# Centrado vertical dentro del bloque precio
mid = CTA_H + PRICE_H / 2           # centro del bloque

txt(cv, 'Compara antes de decidir:', W/2, mid + 82,
    'Helvetica-Bold', 12, WHITE, 'center')

# Precio competidores (tachado)
comp_str = 'Competidores: USD 124.90 / mes (o mas)'
cv.setFont('Helvetica', 10.5)
cv.setFillColor(GRAY)
str_w = cv.stringWidth(comp_str, 'Helvetica', 10.5)
comp_x = W/2 - str_w/2
cv.drawString(comp_x, mid + 56, comp_str)
cv.setStrokeColor(RED_DIM)
cv.setLineWidth(1.5)
cv.line(comp_x, mid + 60, comp_x + str_w, mid + 60)

# Divider sutil
cv.setStrokeColor(TEAL_DIM)
cv.setLineWidth(0.5)
cv.setDash(3, 6)
cv.line(W/2 - 80, mid + 40, W/2 + 80, mid + 40)
cv.setDash()

# Precio KanbanPro — sin label redundante, solo el numero grande
txt(cv, 'USD 22', W/2, mid - 12,
    'Helvetica-Bold', 52, GOLD, 'center')
txt(cv, 'Pago unico  ·  Sin mensualidades  ·  Acceso de por vida',
    W/2, mid - 32, 'Helvetica', 9, GRAY, 'center')

# Garantia
cv.setFillColor(HexColor('#1f3a2e'))
cv.roundRect(W/2 - 120, mid - 62, 240, 22, 6, fill=1, stroke=0)
txt(cv, 'Soporte incluido  ·  Sin contrato  ·  Cancelable cuando quieras',
    W/2, mid - 55, 'Helvetica', 7.5, HexColor('#4ade80'), 'center')

# ════════════════════════════════════════════════
# 6. CTA FOOTER — Teal
# ════════════════════════════════════════════════
bg(cv, 0, 0, W, CTA_H, TEAL)

# Linea separadora dorada
cv.setStrokeColor(GOLD)
cv.setLineWidth(2.5)
cv.line(0, CTA_H, W, CTA_H)

txt(cv, 'Escríbeme — Te explico en 2 minutos como implementarlo',
    W/2, CTA_H - 26, 'Helvetica-Bold', 12, DARK_NAVY, 'center')

# Boton WhatsApp
cv.setFillColor(DARK_NAVY)
cv.roundRect(W/2 - 150, CTA_H - 66, 300, 30, 9, fill=1, stroke=0)
txt(cv, 'WhatsApp: +57 320 997 4750',
    W/2, CTA_H - 56, 'Helvetica-Bold', 13, TEAL, 'center')

# URL
txt(cv, 'Disponible en hotmart.com  ·  kanbanpro.co',
    W/2, CTA_H - 82, 'Helvetica', 9, DARK_SURF, 'center')

# Micro footer
txt(cv, 'KanbanPro — Sistema Kanban para gyms, clinicas y negocios que crecen con orden.',
    W/2, 10, 'Helvetica', 6.5, DARK_SURF, 'center')

# ─────────────────────────────────────────────
# GUARDAR
# ─────────────────────────────────────────────
cv.save()
print(f'[OK] PDF generado: {OUTPUT}')
