"""
TechSolve S.A. -- Soporte Técnico Nivel 1
Máquina de estados finita del chatbot
Estados: INICIO, AUTENTICANDO, MENU, PROCESANDO,
         ESPERANDO_CONFIRMACION, CERRADO, ESCALADO,
         ERROR_AUTH, ERROR_INPUT
"""

# Estados posibles del bot
INICIO                  = "INICIO"
AUTENTICANDO            = "AUTENTICANDO"
MENU                    = "MENU"
PROCESANDO              = "PROCESANDO"
ESPERANDO_CONFIRMACION  = "ESPERANDO_CONFIRMACION"
CERRADO                 = "CERRADO"
ESCALADO                = "ESCALADO"
ERROR_AUTH              = "ERROR_AUTH"
ERROR_INPUT             = "ERROR_INPUT"
FIN                     = "FIN"

# Categorías disponibles
CATEGORIAS = {
    "1": "hardware",
    "2": "software",
    "3": "red",
    "4": "accesos"
}

MAX_INTENTOS_AUTH = 3


class SesionBot:
    """
    Representa la sesión de un usuario con el bot.
    Guarda el estado actual y los datos acumulados durante el flujo.
    """

    def __init__(self, session_id: str):
        self.session_id       = session_id
        self.estado           = INICIO
        self.estado_anterior  = None
        self.intentos_auth    = 0
        self.usuario          = None       # dict con datos del usuario autenticado
        self.categoria        = None       # categoría elegida
        self.solucion         = None       # solución encontrada en BD
        self.id_ticket        = None       # ticket generado

    def transicionar(self, nuevo_estado: str):
        """Registra el estado anterior y avanza al nuevo estado."""
        self.estado_anterior = self.estado
        self.estado = nuevo_estado

    def resetear(self):
        """Reinicia la sesión al estado INICIO manteniendo el session_id."""
        self.__init__(self.session_id)

    def to_dict(self) -> dict:
        """Serializa la sesión para guardarla en Flask session."""
        return {
            "session_id":      self.session_id,
            "estado":          self.estado,
            "estado_anterior": self.estado_anterior,
            "intentos_auth":   self.intentos_auth,
            "usuario":         self.usuario,
            "categoria":       self.categoria,
            "solucion":        self.solucion,
            "id_ticket":       self.id_ticket,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "SesionBot":
        """Reconstruye una sesión desde el dict guardado en Flask session."""
        obj = cls(data["session_id"])
        obj.estado           = data.get("estado", INICIO)
        obj.estado_anterior  = data.get("estado_anterior")
        obj.intentos_auth    = data.get("intentos_auth", 0)
        obj.usuario          = data.get("usuario")
        obj.categoria        = data.get("categoria")
        obj.solucion         = data.get("solucion")
        obj.id_ticket        = data.get("id_ticket")
        return obj
