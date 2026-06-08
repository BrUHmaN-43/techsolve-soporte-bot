"""
TechSolve S.A. -- Soporte Técnico Nivel 1
Respuestas estándar del bot por estado y situación
"""

from bot.states import MAX_INTENTOS_AUTH


def bienvenida() -> str:
    return (
        "Bienvenido/a al sistema de Soporte Técnico de <strong>TechSolve S.A.</strong><br><br>"
        "Por favor ingresá tu <strong>número de legajo</strong> o tu "
        "<strong>correo corporativo</strong> para continuar."
    )


def error_legajo_no_encontrado(intentos_restantes: int) -> str:
    return (
        f"No encontré ese legajo en el sistema. "
        f"Verificá el dato e intentá de nuevo "
        f"<em>(intentos restantes: {intentos_restantes})</em>."
    )


def error_max_intentos() -> str:
    return (
        "Superaste el número de intentos permitidos. "
        "Por favor comunicáte con Soporte al <strong>interno 101</strong>."
    )


def saludo_usuario(nombre: str) -> str:
    return (
        f"¡Hola, <strong>{nombre}</strong>! Autenticación exitosa.<br><br>"
        "¿Cuál es el tipo de problema que tenés? Elegí una opción:<br><br>"
        "<strong>1</strong> — Hardware (equipo, teclado, monitor, impresora)<br>"
        "<strong>2</strong> — Software (aplicación no abre, errores del sistema)<br>"
        "<strong>3</strong> — Red / Conectividad (sin internet, VPN, carpetas)<br>"
        "<strong>4</strong> — Accesos y permisos (contraseña, cuenta bloqueada)"
    )


def menu_categorias() -> str:
    return (
        "¿Cuál es el tipo de problema? Elegí una opción:<br><br>"
        "<strong>1</strong> — Hardware<br>"
        "<strong>2</strong> — Software<br>"
        "<strong>3</strong> — Red / Conectividad<br>"
        "<strong>4</strong> — Accesos y permisos"
    )


def opcion_invalida() -> str:
    return (
        "Opción no válida. Por favor respondé con un número entre "
        "<strong>1</strong> y <strong>4</strong>."
    )


def entrada_no_numerica() -> str:
    return (
        "Necesito que elijas una opción con un número. Intentalo de nuevo."
    )


def solucion_encontrada(categoria: str, solucion: str) -> str:
    nombres = {
        "hardware": "Hardware",
        "software": "Software",
        "red":      "Red / Conectividad",
        "accesos":  "Accesos y permisos"
    }
    nombre_cat = nombres.get(categoria, categoria.capitalize())
    solucion_html = solucion.replace("\n", "<br>")
    return (
        f"Categoría: <strong>{nombre_cat}</strong><br><br>"
        f"{solucion_html}<br><br>"
        "¿El problema quedó resuelto? Respondé <strong>Sí</strong> o <strong>No</strong>."
    )


def sin_solucion_en_bd(categoria: str) -> str:
    return (
        f"No encontré una solución estándar para esa categoría. "
        f"Voy a escalar tu caso al equipo de soporte nivel 2.<br><br>"
        "¿Querés que registre el ticket como escalado? Respondé <strong>Sí</strong> o <strong>No</strong>."
    )


def ticket_cerrado(id_ticket: int) -> str:
    return (
        f"Excelente. El ticket <strong>#{id_ticket}</strong> quedó registrado como "
        f"<strong>Resuelto</strong>. ✓<br><br>"
        "Si necesitás abrir otro caso, escribí <strong>/reiniciar</strong>."
    )


def ticket_escalado(id_ticket: int) -> str:
    return (
        f"Entendido. El ticket <strong>#{id_ticket}</strong> fue escalado al equipo de "
        f"soporte <strong>Nivel 2</strong>. Un técnico se comunicará con vos a la brevedad.<br><br>"
        "Si necesitás abrir otro caso, escribí <strong>/reiniciar</strong>."
    )


def confirmacion_invalida() -> str:
    return (
        "Por favor respondé <strong>Sí</strong> o <strong>No</strong> "
        "para indicar si el problema quedó resuelto."
    )


def mensaje_vacio() -> str:
    return "No recibí ningún mensaje. Por favor escribí tu respuesta."


def sesion_reiniciada() -> str:
    return (
        "Sesión reiniciada. "
        "Ingresá tu <strong>legajo</strong> o <strong>correo corporativo</strong> para comenzar."
    )


def sesion_cancelada() -> str:
    return (
        "Sesión cancelada. No se guardó ningún ticket.<br><br>"
        "Si querés iniciar una nueva consulta, escribí <strong>/reiniciar</strong>."
    )


def estado_ticket(id_ticket: int, estado: str, fecha: str) -> str:
    return (
        f"Tu último ticket es el <strong>#{id_ticket}</strong>.<br>"
        f"Estado: <strong>{estado}</strong><br>"
        f"Fecha: {fecha}"
    )


def sin_tickets() -> str:
    return "No tenés tickets registrados aún."


def error_interno() -> str:
    return (
        "Ocurrió un error interno. Por favor intentá de nuevo o "
        "comunicáte con Soporte al <strong>interno 101</strong>."
    )
