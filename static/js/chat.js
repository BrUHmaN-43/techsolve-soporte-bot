/* TechSolve S.A. — Chatbot frontend */

const messagesEl = document.getElementById("chat-messages");
const inputEl    = document.getElementById("user-input");
const sendBtn    = document.getElementById("send-btn");

// ── Inicializar chat al cargar la página ──────────────────
window.addEventListener("DOMContentLoaded", async () => {
  await iniciarSesion();
  inputEl.focus();
});

async function iniciarSesion() {
  try {
    const res  = await fetch("/api/start", { method: "POST" });
    const data = await res.json();
    agregarBurbuja(data.mensaje, "bot");
  } catch (e) {
    agregarBurbuja("Error al conectar con el servidor. Recargá la página.", "bot");
  }
}

// ── Enviar mensaje ─────────────────────────────────────────
async function enviarMensaje() {
  const texto = inputEl.value.trim();
  if (!texto) return;

  agregarBurbuja(texto, "user");
  inputEl.value = "";
  bloquearInput(true);

  const typingId = mostrarTyping();

  try {
    const res  = await fetch("/api/chat", {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ mensaje: texto }),
    });
    const data = await res.json();
    quitarTyping(typingId);
    agregarBurbuja(data.mensaje, "bot");
  } catch (e) {
    quitarTyping(typingId);
    agregarBurbuja("Error de conexión. Intentá de nuevo.", "bot");
  } finally {
    bloquearInput(false);
    inputEl.focus();
  }
}

function enviarComando(cmd) {
  inputEl.value = cmd;
  enviarMensaje();
}

// ── Enter para enviar ──────────────────────────────────────
inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    enviarMensaje();
  }
});

// ── Burbujas ───────────────────────────────────────────────
function agregarBurbuja(html, tipo) {
  const wrap = document.createElement("div");
  wrap.style.display = "flex";
  wrap.style.flexDirection = "column";
  wrap.style.alignItems = tipo === "user" ? "flex-end" : "flex-start";

  const burbuja = document.createElement("div");
  burbuja.classList.add("bubble", tipo === "user" ? "bubble-user" : "bubble-bot");
  burbuja.innerHTML = html;

  const tiempo = document.createElement("span");
  tiempo.classList.add("bubble-time");
  tiempo.textContent = horaActual();

  wrap.appendChild(burbuja);
  wrap.appendChild(tiempo);
  messagesEl.appendChild(wrap);
  scrollAbajo();
}

// ── Typing indicator ───────────────────────────────────────
function mostrarTyping() {
  const id = "typing-" + Date.now();
  const el = document.createElement("div");
  el.id = id;
  el.classList.add("typing");
  el.innerHTML = "<span></span><span></span><span></span>";
  messagesEl.appendChild(el);
  scrollAbajo();
  return id;
}

function quitarTyping(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

// ── Helpers ────────────────────────────────────────────────
function bloquearInput(estado) {
  inputEl.disabled = estado;
  sendBtn.disabled = estado;
}

function scrollAbajo() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function horaActual() {
  const d = new Date();
  return d.getHours().toString().padStart(2, "0") + ":" +
         d.getMinutes().toString().padStart(2, "0");
}
