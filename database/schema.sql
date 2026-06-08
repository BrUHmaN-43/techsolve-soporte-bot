-- TechSolve S.A. -- Soporte Técnico Nivel 1
-- Esquema de base de datos

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario    INTEGER PRIMARY KEY AUTOINCREMENT,
    legajo        VARCHAR(20) UNIQUE NOT NULL,
    nombre        VARCHAR(100) NOT NULL,
    email         VARCHAR(150) UNIQUE NOT NULL,
    activo        BOOLEAN DEFAULT 1
);

CREATE TABLE IF NOT EXISTS soluciones (
    id_solucion   INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria     VARCHAR(50) NOT NULL,
    descripcion   TEXT NOT NULL,
    solucion      TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets (
    id_ticket      INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario     INTEGER NOT NULL,
    categoria      VARCHAR(50) NOT NULL,
    descripcion    TEXT NOT NULL,
    estado         VARCHAR(20) NOT NULL DEFAULT 'Abierto',
    fecha_apertura DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_cierre   DATETIME,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
