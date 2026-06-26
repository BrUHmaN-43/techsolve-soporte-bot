# TechSolve Soporte Bot

Chatbot de **Soporte Técnico Nivel 1** para TechSolve S.A.  
Trabajo Práctico Integrador — Organización Empresarial — TUP UTN

---

## Descripción

Sistema de chatbot web que automatiza el proceso de soporte técnico nivel 1 mediante una máquina de estados finita implementada en Python/Flask, siguiendo el flujo modelado en el diagrama BPMN 2.0.

El bot permite a los empleados:
- Autenticarse con su legajo o correo corporativo
- Seleccionar la categoría de su problema
- Recibir una solución estándar desde la base de datos
- Confirmar si el problema fue resuelto o escalarlo al nivel 2
- Consultar el estado de su último ticket

---

## Tecnologías

| Capa       | Tecnología                  |
|------------|-----------------------------|
| Frontend   | HTML5, CSS3, JavaScript     |
| Backend    | Python 3.10+, Flask 3.x     |
| Base datos | SQLite (desarrollo)         |
| Lógica     | Máquina de estados (FSM)    |

---

## Estructura del proyecto

```
techsolve-soporte-bot/
├── app.py                  # Servidor Flask principal
├── requirements.txt        # Dependencias
├── bot/
│   ├── states.py           # Máquina de estados y clase SesionBot
│   └── responses.py        # Mensajes del bot por estado
├── database/
│   ├── schema.sql          # Definición de tablas
│   ├── seed_data.sql       # Usuarios y soluciones de prueba
│   └── init_db.py          # Script de inicialización
├── static/
│   ├── css/style.css       # Estilos del chat
│   └── js/chat.js          # Lógica del frontend
├── templates/
│   └── index.html          # Interfaz del chatbot
└── docs/
    └── bpmn_soporte.png    # Diagrama BPMN 2.0
```

---

## Instalación y despliegue local

### Requisitos previos
- Python 3.10 o superior
- pip
- Utilizar el CMD
### Pasos

**1. Copiar la dirección de ruta y pegarlo en el CMD**
```bash
cd C:\Users\PC\Downloads\techsolve-soporte-bot-main\techsolve-soporte-bot-main
```

**2. Crear y activar entorno virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**4. Inicializar la base de datos**
```bash
python database/init_db.py
```

**5. Ejecutar el servidor**
```bash
python app.py
```

El chatbot queda disponible en: **http://localhost:5000**

---

## Usuarios de prueba

| Legajo  | Nombre           | Email                            |
|---------|------------------|----------------------------------|
| EMP001  | Ana García       | ana.garcia@techsolve.com         |
| EMP002  | Carlos López     | carlos.lopez@techsolve.com       |
| EMP003  | María Fernández  | maria.fernandez@techsolve.com    |
| EMP004  | Juan Pérez       | juan.perez@techsolve.com         |
| EMP005  | Laura Martínez   | laura.martinez@techsolve.com     |

---

## Comandos del bot

| Comando      | Función                                         |
|--------------|-------------------------------------------------|
| `/reiniciar` | Vuelve al inicio sin guardar ticket             |
| `/cancelar`  | Abandona el flujo actual                        |
| `/estado`    | Muestra el estado del último ticket del usuario |

---

## Diagrama BPMN

El diagrama BPMN 2.0 del proceso se encuentra en `/docs/bpmn_soporte.png`.  
Incluye dos carriles: **Usuario** y **Sistema/Bot**, con las dos compuertas XOR del flujo.

---

## Autor

Trabajo Práctico Integrador — Cátedra Organización Empresarial  
Tecnicatura Universitaria en Programación — UTN — Julián Salcedo Scardino / Comisión: M26 C1-16 / DNI: 47975164
