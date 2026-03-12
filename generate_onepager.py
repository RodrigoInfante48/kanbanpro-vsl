#!/usr/bin/env python3
"""
KanbanPro — Motor de One-Pagers por Industria
Uso: python generate_onepager.py [industria]
     python generate_onepager.py gym
     python generate_onepager.py vet
     python generate_onepager.py estetica
     python generate_onepager.py restaurante
     python generate_onepager.py academia
     python generate_onepager.py all        ← genera todos

Para industrias nuevas: agregar entrada al dict INDUSTRIES abajo.
"""

import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

# ─────────────────────────────────────────────
# BRAND — KanbanPro (no tocar)
# ─────────────────────────────────────────────
DARK_NAVY = HexColor('#1a1a2e')
DARK_SURF = HexColor('#16213e')
TEAL      = HexColor('#00e6c7')
GOLD      = HexColor('#FFB800')
WHITE     = HexColor('#ffffff')
GRAY      = HexColor('#9ca3af')
RED_DIM   = HexColor('#ff6b6b')
TEAL_DIM  = HexColor('#00b8a0')
GREEN_BG  = HexColor('#1f3a2e')
GREEN_TXT = HexColor('#4ade80')

BASE_DIR  = r'C:\Users\rodri\OneDrive\Documents\DD\stitch_kanbanpro_vsl_landing_page'

# ─────────────────────────────────────────────
# INDUSTRIAS — solo editar aqui para agregar nuevas
# ─────────────────────────────────────────────
INDUSTRIES = {

    'gym': {
        'filename':   'kanbanpro-gym-onepager.pdf',
        'meta_title': 'KanbanPro — Sistema de Gestion para Tu Gym',
        'tagline':    'Gestion visual para tu gym \u2014 Control total desde hoy',
        'sub_tags':   'Horarios  \u00b7  Instructores  \u00b7  Miembros  \u00b7  Equipos',
        'pain_title': 'El problema real de tu gym:',
        'pain_lines': [
            'Horarios por WhatsApp, instructores sin claridad,',
            'miembros que se van y no sabes por que.',
            'Todo en tu cabeza. Nada en un sistema que lo soporte.',
        ],
        'benefits': [
            ('Tablero de clases en tiempo real',
             'Ve todos los turnos del dia de un vistazo \u2014 desde tu celular'),
            ('Control de instructores sin WhatsApp caotico',
             'Cada instructor tiene su agenda clara, sin mensajes de ida y vuelta'),
            ('Seguimiento de miembros activos e inactivos',
             'Detecta quien esta por cancelar antes de que lo haga'),
            ('Gestion de equipos y zonas del gym',
             'Maquinas, limpieza y mantenimiento en un solo tablero'),
        ],
        'footer_micro': 'KanbanPro \u2014 Sistema Kanban para gyms, clinicas y negocios que crecen con orden.',
    },

    'vet': {
        'filename':   'kanbanpro-vet-onepager.pdf',
        'meta_title': 'KanbanPro \u2014 Sistema de Gestion para Tu Clinica Veterinaria',
        'tagline':    'Gestion visual para tu veterinaria \u2014 Sin caos operativo',
        'sub_tags':   'Citas  \u00b7  Cirugias  \u00b7  Hospitalizacion  \u00b7  Medicamentos',
        'pain_title': 'El caos real de tu veterinaria hoy:',
        'pain_lines': [
            'Citas que se cruzan, pacientes hospitalizados sin registro,',
            'medicacion que nadie sabe si ya fue aplicada.',
            'Tu clinica funciona \u2014 pero tu cabeza carga con todo el sistema.',
        ],
        'benefits': [
            ('Tablero de citas y cirugias en tiempo real',
             'Ve que sala esta ocupada, quien opera y a que hora \u2014 desde tu celular'),
            ('Control de pacientes hospitalizados',
             'Cada mascota con su tarjeta: medicacion, responsable y estado al dia'),
            ('Coordinacion de veterinarios sin WhatsApp caotico',
             'Cada medico ve su agenda del dia \u2014 sin mensajes de ida y vuelta'),
            ('Registro de tareas clinicas diarias',
             'Esterilizacion, limpieza, medicamentos y seguimientos en un solo lugar'),
        ],
        'footer_micro': 'KanbanPro \u2014 Sistema Kanban para veterinarias, gyms y negocios que crecen con orden.',
    },

    'estetica': {
        'filename':   'kanbanpro-estetica-onepager.pdf',
        'meta_title': 'KanbanPro \u2014 Sistema de Gestion para Tu Centro de Estetica',
        'tagline':    'Gestion visual para tu estetica \u2014 Citas y equipo bajo control',
        'sub_tags':   'Citas  \u00b7  Estilistas  \u00b7  Tratamientos  \u00b7  Productos',
        'pain_title': 'El problema real de tu estetica hoy:',
        'pain_lines': [
            'Citas dobles, estilistas sin claridad de su agenda,',
            'productos que se gastan y nadie sabe quien los uso.',
            'Todo en el celular de la recepcionista. Sin respaldo, sin control.',
        ],
        'benefits': [
            ('Tablero de citas del dia en tiempo real',
             'Cada estilista y cabina visible de un vistazo \u2014 sin llamadas internas'),
            ('Control de agenda por estilista o esteticista',
             'Cada profesional ve solo sus citas \u2014 sin depender de recepcion'),
            ('Seguimiento de productos y consumibles',
             'Registra que se uso en cada servicio \u2014 adiós a los faltantes sin explicacion'),
            ('Historial de tareas y limpieza de cabinas',
             'Protocolos de higiene y preparacion de cabinas en el mismo tablero'),
        ],
        'footer_micro': 'KanbanPro \u2014 Sistema Kanban para esteticas, spas y negocios de belleza.',
    },

    'restaurante': {
        'filename':   'kanbanpro-restaurante-onepager.pdf',
        'meta_title': 'KanbanPro \u2014 Sistema de Gestion para Tu Restaurante',
        'tagline':    'Gestion visual para tu restaurante \u2014 Cocina y salon en sincronía',
        'sub_tags':   'Pedidos  \u00b7  Cocina  \u00b7  Meseros  \u00b7  Delivery',
        'pain_title': 'El problema real de tu restaurante hoy:',
        'pain_lines': [
            'Pedidos que se pierden entre cocina y salon,',
            'meseros sin claridad de que mesa necesita que.',
            'En hora pico todo depende de que alguien grite mas duro.',
        ],
        'benefits': [
            ('Tablero de pedidos cocina\u2013salon en tiempo real',
             'Cocina sabe que hay pendiente \u2014 salon sabe que esta listo'),
            ('Control de mesas y estado de servicio',
             'Libre, ocupada, esperando cuenta \u2014 de un vistazo desde cualquier punto'),
            ('Coordinacion de delivery sin WhatsApp caotico',
             'Cada repartidor tiene su pedido asignado \u2014 sin confusion de rutas'),
            ('Registro de tareas de apertura y cierre',
             'Limpieza, mise en place y checklist de cierre en el mismo tablero'),
        ],
        'footer_micro': 'KanbanPro \u2014 Sistema Kanban para restaurantes, cafes y negocios de alimentos.',
    },

    'academia': {
        'filename':   'kanbanpro-academia-onepager.pdf',
        'meta_title': 'KanbanPro \u2014 Sistema de Gestion para Tu Academia',
        'tagline':    'Gestion visual para tu academia \u2014 Profesores y salones bajo control',
        'sub_tags':   'Horarios  \u00b7  Profesores  \u00b7  Salones  \u00b7  Estudiantes',
        'pain_title': 'El problema real de tu academia hoy:',
        'pain_lines': [
            'Horarios de profesores que cambian cada semana,',
            'salones que se cruzan y estudiantes sin confirmar asistencia.',
            'Todo coordinado en un grupo de WhatsApp que nadie lee a tiempo.',
        ],
        'benefits': [
            ('Tablero de horarios y salones en tiempo real',
             'Quien esta en que salon y a que hora \u2014 sin llamadas de ultimo momento'),
            ('Control de asistencia y seguimiento de grupos',
             'Detecta grupos con bajo rendimiento antes de que el estudiante cancele'),
            ('Coordinacion de profesores por hora o planta',
             'Cada docente ve su semana completa \u2014 sin depender de un solo coordinador'),
            ('Gestion de tareas administrativas',
             'Inscripciones, cobros pendientes y renovaciones en un solo tablero'),
        ],
        'footer_micro': 'KanbanPro \u2014 Sistema Kanban para academias, colegios y centros de ensenanza.',
    },

    'taller': {
        'filename':   'kanbanpro-taller-onepager.pdf',
        'meta_title': 'KanbanPro \u2014 Sistema de Gestion para Tu Taller Mecanico',
        'tagline':    'Gestion visual para tu taller \u2014 Ordenes y tecnicos bajo control',
        'sub_tags':   'Ordenes  \u00b7  Tecnicos  \u00b7  Repuestos  \u00b7  Vehiculos',
        'pain_title': 'El caos real de tu taller hoy:',
        'pain_lines': [
            'Ordenes de trabajo en papel, tecnicos sin claridad de que vehiculo les toca,',
            'repuestos que nadie sabe si llegaron o ya se usaron.',
            'Tu taller trabaja \u2014 pero tu eres el unico que sabe donde esta todo.',
        ],
        'benefits': [
            ('Tablero de ordenes de trabajo en tiempo real',
             'Cada vehiculo con su estado: recibido, en proceso o listo para entregar'),
            ('Control de tecnicos y bahias de trabajo',
             'Quien esta trabajando en que \u2014 sin preguntar ni interrumpir'),
            ('Seguimiento de repuestos y proveedores',
             'Que llego, que falta y que ya se instalo \u2014 todo en un solo lugar'),
            ('Historial de servicios por vehiculo',
             'Registro de cada intervencion \u2014 util para el cliente y para tu equipo'),
        ],
        'footer_micro': 'KanbanPro \u2014 Sistema Kanban para talleres, veterinarias y negocios que crecen con orden.',
    },

}

# ─────────────────────────────────────────────
# MOTOR DE RENDERIZADO (no tocar)
# ─────────────────────────────────────────────
W, H = A4  # 595 x 842 pt

def _bg(cv, x, y, w, h, color):
    cv.setFillColor(color); cv.rect(x, y, w, h, fill=1, stroke=0)

def _txt(cv, t, x, y, font='Helvetica', size=10, color=WHITE, align='left'):
    cv.setFillColor(color); cv.setFont(font, size)
    if align == 'center': cv.drawCentredString(x, y, t)
    elif align == 'right': cv.drawRightString(x, y, t)
    else: cv.drawString(x, y, t)

def _checkmark(cv, cx, cy, sz, color):
    cv.setStrokeColor(color); cv.setLineWidth(sz * 0.22); cv.setLineCap(1)
    p = cv.beginPath()
    p.moveTo(cx - sz*0.45, cy); p.lineTo(cx - sz*0.05, cy - sz*0.42)
    p.lineTo(cx + sz*0.52, cy + sz*0.38)
    cv.drawPath(p, stroke=1, fill=0)

def _benefit_row(cv, y, label, desc, idx):
    _bg(cv, 0, y - 14, W, 50, DARK_NAVY if idx % 2 == 0 else DARK_SURF)
    cv.setFillColor(TEAL); cv.circle(46, y + 16, 11, fill=1, stroke=0)
    _checkmark(cv, 46, y + 16, 10, DARK_NAVY)
    _txt(cv, label, 68, y + 20, 'Helvetica-Bold', 10.5, WHITE)
    _txt(cv, desc,  68, y + 6,  'Helvetica',      8.5,  GRAY)

def render(industry_key: str) -> str:
    """Genera el PDF para la industria dada. Devuelve la ruta del archivo."""
    cfg = INDUSTRIES[industry_key]
    output = f"{BASE_DIR}\\{cfg['filename']}"

    cv = canvas.Canvas(output, pagesize=A4)
    cv.setTitle(cfg['meta_title'])
    cv.setAuthor('KanbanPro')
    cv.setSubject(f"One-Pager Propuesta Comercial — {industry_key.capitalize()}")

    # 1. Fondo
    _bg(cv, 0, 0, W, H, DARK_NAVY)

    # 2. Header
    HEADER_H = 142
    _bg(cv, 0, H - HEADER_H, W, HEADER_H, TEAL)
    _bg(cv, 0, H - 8, W, 8, TEAL_DIM)
    _txt(cv, 'KanbanPro', W/2, H - 54, 'Helvetica-Bold', 40, DARK_NAVY, 'center')
    cv.setStrokeColor(DARK_NAVY); cv.setLineWidth(0.8); cv.setDash(4, 4)
    cv.line(60, H - 74, W - 60, H - 74); cv.setDash()
    _txt(cv, cfg['tagline'],  W/2, H - 95,  'Helvetica-Bold', 11.5, DARK_SURF, 'center')
    _txt(cv, cfg['sub_tags'], W/2, H - 118, 'Helvetica',       9,    DARK_SURF, 'center')
    cv.setFillColor(GOLD)
    cv.roundRect(W/2 - 55, H - 136, 110, 18, 6, fill=1, stroke=0)
    _txt(cv, 'USD 22  |  Pago unico de por vida', W/2, H - 131,
         'Helvetica-Bold', 8.5, DARK_NAVY, 'center')

    # 3. Problema
    PAIN_TOP = H - HEADER_H
    PAIN_H   = 100
    _bg(cv, 0, PAIN_TOP - PAIN_H, W, PAIN_H, DARK_SURF)
    cv.setFillColor(GOLD); cv.circle(50, PAIN_TOP - PAIN_H/2, 18, fill=1, stroke=0)
    _txt(cv, '!', 50, PAIN_TOP - PAIN_H/2 - 7, 'Helvetica-Bold', 22, DARK_NAVY, 'center')
    _txt(cv, cfg['pain_title'], 80, PAIN_TOP - 22, 'Helvetica-Bold', 11.5, GOLD)
    offsets = [40, 56, 74]
    for line, offset in zip(cfg['pain_lines'], offsets):
        color = WHITE if offset < 74 else GRAY
        _txt(cv, line, 80, PAIN_TOP - offset, 'Helvetica', 10 if offset < 74 else 9.5, color)

    # 4. Beneficios
    BENEFITS_TOP = PAIN_TOP - PAIN_H - 10
    for i, (label, desc) in enumerate(cfg['benefits']):
        _benefit_row(cv, BENEFITS_TOP - (i * 52), label, desc, i)

    # 5. Precio
    CTA_H     = 108
    PRICE_TOP = BENEFITS_TOP - (len(cfg['benefits']) * 52) - 18
    PRICE_H   = PRICE_TOP - CTA_H
    _bg(cv, 0, CTA_H, W, PRICE_H, DARK_SURF)
    cv.setStrokeColor(TEAL); cv.setLineWidth(2)
    cv.line(40, PRICE_TOP, W - 40, PRICE_TOP)
    mid = CTA_H + PRICE_H / 2
    _txt(cv, 'Compara antes de decidir:', W/2, mid + 82, 'Helvetica-Bold', 12, WHITE, 'center')
    comp = 'Competidores: USD 124.90 / mes (o mas)'
    cv.setFont('Helvetica', 10.5); cv.setFillColor(GRAY)
    sw = cv.stringWidth(comp, 'Helvetica', 10.5); cx = W/2 - sw/2
    cv.drawString(cx, mid + 56, comp)
    cv.setStrokeColor(RED_DIM); cv.setLineWidth(1.5)
    cv.line(cx, mid + 60, cx + sw, mid + 60)
    cv.setStrokeColor(TEAL_DIM); cv.setLineWidth(0.5); cv.setDash(3, 6)
    cv.line(W/2 - 80, mid + 40, W/2 + 80, mid + 40); cv.setDash()
    _txt(cv, 'USD 22', W/2, mid - 12, 'Helvetica-Bold', 52, GOLD, 'center')
    _txt(cv, 'Pago unico  \u00b7  Sin mensualidades  \u00b7  Acceso de por vida',
         W/2, mid - 32, 'Helvetica', 9, GRAY, 'center')
    cv.setFillColor(GREEN_BG)
    cv.roundRect(W/2 - 120, mid - 62, 240, 22, 6, fill=1, stroke=0)
    _txt(cv, 'Soporte incluido  \u00b7  Sin contrato  \u00b7  Cancelable cuando quieras',
         W/2, mid - 55, 'Helvetica', 7.5, GREEN_TXT, 'center')

    # 6. CTA Footer
    _bg(cv, 0, 0, W, CTA_H, TEAL)
    cv.setStrokeColor(GOLD); cv.setLineWidth(2.5); cv.line(0, CTA_H, W, CTA_H)
    _txt(cv, 'Escribeme \u2014 Te explico en 2 minutos como implementarlo',
         W/2, CTA_H - 26, 'Helvetica-Bold', 12, DARK_NAVY, 'center')
    cv.setFillColor(DARK_NAVY)
    cv.roundRect(W/2 - 150, CTA_H - 66, 300, 30, 9, fill=1, stroke=0)
    _txt(cv, 'WhatsApp: +57 320 997 4750',
         W/2, CTA_H - 56, 'Helvetica-Bold', 13, TEAL, 'center')
    _txt(cv, 'Disponible en hotmart.com  \u00b7  kanbanpro.co',
         W/2, CTA_H - 82, 'Helvetica', 9, DARK_SURF, 'center')
    _txt(cv, cfg['footer_micro'], W/2, 10, 'Helvetica', 6.5, DARK_SURF, 'center')

    cv.save()
    return output


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────
if __name__ == '__main__':
    key = sys.argv[1].lower() if len(sys.argv) > 1 else 'gym'

    if key == 'all':
        for k in INDUSTRIES:
            path = render(k)
            print(f'[OK] {k:15} -> {path}')
    elif key in INDUSTRIES:
        path = render(key)
        print(f'[OK] PDF generado: {path}')
    else:
        valid = ', '.join(INDUSTRIES.keys())
        print(f'[ERROR] Industria "{key}" no encontrada.')
        print(f'        Disponibles: {valid}')
        print(f'        Para agregar una nueva: edita INDUSTRIES en este archivo.')
        sys.exit(1)
