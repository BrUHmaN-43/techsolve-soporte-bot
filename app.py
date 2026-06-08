"""
TechSolve S.A. -- Soporte Técnico Nivel 1
Servidor principal Flask -- Chatbot de soporte
"""

import os
import sqlite3
import uuid
from datetime import datetime

from flask import Flask, request, jsonify, render_template, session

from bot.states import (
    SesionBot, CATEGORIAS, MAX_INTENTOS_AUTH,
    INICIO, AUTENTICANDO, MENU, PROCESANDO,
    ESPERANDO_CONFIRMACION, CERRADO, ESCALADO,
    ERROR_AUTH, ERROR_INPUT, FIN
)
import bot.responses as resp

# ──────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "techsolve-dev-secret-2024")

DB_PATH = os.path.join(os.path.dirname(__file__), "techsolve.db")


# ──────────────────────────────────────────────
# Helpers de base de datos
# ──────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def buscar_usuario(legajo_o_email: str):
    """Busca un usuario activo por legajo o email."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM usuarios WHERE (legajo=? OR email=?) AND activo=1",
        (legajo_o_email, legajo_o_email)
    )
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def buscar_solucion(categoria: str) -> str | None:
    """Devuelve la primera solución de la categoría dada."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT solucion FROM soluciones WHERE categoria=? LIMIT 1",
        (categoria,)
    )
    row = cur.fetchone()
    conn.close()
    return row["solucion"] if row else None


def registrar_ticket(id_usuario: int, categoria: str, descripcion: str, estado: str) -> int:
    """Crea un ticket y devuelve su id."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO tickets (id_usuario, categoria, descripcion, estado, fecha_apertura)
           VALUES (?, ?, ?, ?, ?)""",
        (id_usuario, categoria, descripcion, estado, datetime.now().isoformat())
    )
    conn.commit()
    ticket_id = cur.lastrowid
    conn.close()
    return ticket_id


def cerrar_ticket(id_ticket: int, estado: str):
    """Actualiza el estado y fecha de cierre de un ticket."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tickets SET estado=?, fecha_cierre=? WHERE id_ticket=?",
        (estado, datetime.now().isoformat(), id_ticket)
    )
    conn.commit()
    conn.close()


def ultimo_ticket_usuario(id_usuario: int):
    """Devuelve el último ticket del usuario."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """SELECT id_ticket, estado, fecha_apertura FROM tickets
           WHERE id_usuario=? ORDER BY id_ticket DESC LIMIT 1""",
        (id_usuario,)
    )
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


# ──────────────────────────────────────────────
# Gestión de sesión del bot
# ──────────────────────────────────────────────

def cargar_sesion() -> SesionBot:
    if "bot_session" in session:
        return SesionBot.from_dict(session["bot_session"])
    sid = str(uuid.uuid4())
    return SesionBot(sid)


def guardar_sesion(sesion: SesionBot):
    session["bot_session"] = sesion.to_dict()


# ──────────────────────────────────────────────
# Lógica principal del bot (máquina de estados)
# ──────────────────────────────────────────────

def procesar_mensaje(texto: str, sesion: SesionBot) -> str:
    """
    Procesa el mensaje del usuario según el estado actual
    y devuelve la respuesta del bot.
    Implementa el flujo BPMN completo con manejo del camino infeliz.
    """
    texto = texto.strip()

    # Comandos globales (funcionan en cualquier estado)
    if texto.lower() == "/reiniciar":
        sesion.resetear()
        return resp.sesion_reiniciada()

    if texto.lower() == "/cancelar":
        sesion.resetear()
        return resp.sesion_cancelada()

    if texto.lower() == "/estado":
        if sesion.usuario:
            ticket = ultimo_ticket_usuario(sesion.usuario["id_usuario"])
            if ticket:
                return resp.estado_ticket(
                    ticket["id_ticket"], ticket["estado"], ticket["fecha_apertura"]
                )
        return resp.sin_tickets()

    # Mensaje vacío
    if not texto:
        return resp.mensaje_vacio()

    # ── Estado: INICIO ──────────────────────────────
    if sesion.estado == INICIO:
        sesion.transicionar(AUTENTICANDO)
        usuario = buscar_usuario(texto)
        if usuario:
            sesion.usuario = usuario
            sesion.intentos_auth = 0
            sesion.transicionar(MENU)
            return resp.saludo_usuario(usuario["nombre"])
        else:
            sesion.intentos_auth += 1
            restantes = MAX_INTENTOS_AUTH - sesion.intentos_auth
            if restantes <= 0:
                sesion.transicionar(FIN)
                return resp.error_max_intentos()
            sesion.transicionar(INICIO)
            return resp.error_legajo_no_encontrado(restantes)

    # ── Estado: MENU ───────────────────────────────
    elif sesion.estado == MENU:
        if not texto.isdigit():
            return resp.entrada_no_numerica()
        if texto not in CATEGORIAS:
            return resp.opcion_invalida()

        sesion.categoria = CATEGORIAS[texto]
        sesion.transicionar(PROCESANDO)

        solucion = buscar_solucion(sesion.categoria)
        if solucion:
            sesion.solucion = solucion
            sesion.transicionar(ESPERANDO_CONFIRMACION)
            return resp.solucion_encontrada(sesion.categoria, solucion)
        else:
            # Sin solución en BD → escalar directamente
            id_ticket = registrar_ticket(
                sesion.usuario["id_usuario"],
                sesion.categoria,
                f"Sin solución estándar para: {sesion.categoria}",
                "Escalado"
            )
            sesion.id_ticket = id_ticket
            sesion.transicionar(ESCALADO)
            return resp.ticket_escalado(id_ticket)

    # ── Estado: ESPERANDO_CONFIRMACION ─────────────
    elif sesion.estado == ESPERANDO_CONFIRMACION:
        respuesta = texto.lower().strip()
        if respuesta in ("si", "sí", "s", "yes", "1"):
            id_ticket = registrar_ticket(
                sesion.usuario["id_usuario"],
                sesion.categoria,
                sesion.solucion or "Solución estándar aplicada",
                "Resuelto"
            )
            sesion.id_ticket = id_ticket
            cerrar_ticket(id_ticket, "Resuelto")
            sesion.transicionar(CERRADO)
            return resp.ticket_cerrado(id_ticket)

        elif respuesta in ("no", "n", "0"):
            id_ticket = registrar_ticket(
                sesion.usuario["id_usuario"],
                sesion.categoria,
                sesion.solucion or "Solución estándar no funcionó",
                "Escalado"
            )
            sesion.id_ticket = id_ticket
            cerrar_ticket(id_ticket, "Escalado")
            sesion.transicionar(ESCALADO)
            return resp.ticket_escalado(id_ticket)

        else:
            return resp.confirmacion_invalida()

    # ── Estados finales ────────────────────────────
    elif sesion.estado in (CERRADO, ESCALADO, FIN):
        return (
            "Tu consulta ya fue procesada. "
            "Escribí <strong>/reiniciar</strong> para iniciar una nueva."
        )

    # Fallback
    return resp.error_interno()


# ──────────────────────────────────────────────
# Rutas Flask
# ──────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/start", methods=["POST"])
def start():
    """Inicia una nueva sesión y devuelve el mensaje de bienvenida."""
    sesion = SesionBot(str(uuid.uuid4()))
    guardar_sesion(sesion)
    return jsonify({"mensaje": resp.bienvenida(), "estado": sesion.estado})


@app.route("/api/chat", methods=["POST"])
def chat():
    """Recibe el mensaje del usuario y devuelve la respuesta del bot."""
    data = request.get_json(silent=True) or {}
    texto = data.get("mensaje", "").strip()

    sesion = cargar_sesion()
    respuesta = procesar_mensaje(texto, sesion)
    guardar_sesion(sesion)

    return jsonify({
        "mensaje": respuesta,
        "estado":  sesion.estado,
        "usuario": sesion.usuario["nombre"] if sesion.usuario else None
    })


if __name__ == "__main__":
    # Verificar que la BD exista
    if not os.path.exists(DB_PATH):
        print("ERROR: Base de datos no encontrada.")
        print("Ejecutá primero: python database/init_db.py")
    else:
        app.run(debug=True, port=5000)
