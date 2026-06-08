-- Datos de prueba -- TechSolve S.A.

INSERT OR IGNORE INTO usuarios (legajo, nombre, email) VALUES
    ('EMP001', 'Ana García',      'ana.garcia@techsolve.com'),
    ('EMP002', 'Carlos López',    'carlos.lopez@techsolve.com'),
    ('EMP003', 'María Fernández', 'maria.fernandez@techsolve.com'),
    ('EMP004', 'Juan Pérez',      'juan.perez@techsolve.com'),
    ('EMP005', 'Laura Martínez',  'laura.martinez@techsolve.com');

INSERT OR IGNORE INTO soluciones (categoria, descripcion, solucion) VALUES
    ('hardware', 'El equipo no enciende',
     '1. Verificá que el cable de alimentación esté bien conectado.\n2. Intentá con otro tomacorriente.\n3. Presioná el botón de encendido durante 10 segundos.\n4. Si el problema persiste, el equipo será revisado por técnicos.'),

    ('hardware', 'El monitor no muestra imagen',
     '1. Revisá que el cable de video (HDMI/VGA) esté bien conectado al monitor y a la PC.\n2. Verificá que el monitor esté encendido y en la entrada correcta.\n3. Probá con otro cable o monitor.\n4. Reiniciá el equipo.'),

    ('hardware', 'El teclado o mouse no responde',
     '1. Desconectá y volvé a conectar el dispositivo.\n2. Probá en otro puerto USB.\n3. Si es inalámbrico, reemplazá las pilas.\n4. Reiniciá el equipo.'),

    ('software', 'Una aplicación no abre o se congela',
     '1. Cerrá la aplicación desde el Administrador de Tareas (Ctrl+Alt+Supr).\n2. Reiniciá la aplicación.\n3. Reiniciá el equipo.\n4. Si persiste, desinstalá y volvé a instalar la aplicación.'),

    ('software', 'Error al iniciar sesión en el sistema',
     '1. Verificá que el Bloq Mayús no esté activado.\n2. Intentá restablecer tu contraseña desde el portal de autoservicio.\n3. Si no recordás la contraseña, contactá a soporte para un reseteo.'),

    ('software', 'El sistema operativo funciona muy lento',
     '1. Cerrá las aplicaciones que no estés usando.\n2. Reiniciá el equipo.\n3. Verificá que el disco duro tenga al menos 10% de espacio libre.\n4. Ejecutá el antivirus.'),

    ('red', 'No tengo acceso a internet',
     '1. Verificá que el cable de red esté conectado o que el Wi-Fi esté activado.\n2. Reiniciá el router (desconectalo 30 segundos).\n3. Ejecutá el diagnóstico de red de Windows.\n4. Verificá que no haya cortes reportados en el área.'),

    ('red', 'No puedo conectarme a la VPN',
     '1. Verificá que tengas internet antes de conectarte a la VPN.\n2. Revisá que tus credenciales de VPN sean correctas.\n3. Cerrá y volvé a abrir el cliente VPN.\n4. Reiniciá el equipo.'),

    ('red', 'No puedo acceder a carpetas compartidas',
     '1. Verificá que estés conectado a la red corporativa o VPN.\n2. Asegurate de tener los permisos correctos sobre la carpeta.\n3. Intentá acceder usando la ruta completa (\\\\servidor\\carpeta).\n4. Contactá a soporte si el problema persiste.'),

    ('accesos', 'Mi cuenta está bloqueada',
     '1. Esperá 15 minutos y volvé a intentar.\n2. Si sigue bloqueada, un administrador debe desbloquearte manualmente.\n3. Contactá a soporte indicando tu legajo y correo corporativo.'),

    ('accesos', 'Necesito restablecer mi contraseña',
     '1. Ingresá al portal de autoservicio: https://intranet.techsolve.com/password\n2. Ingresá tu legajo y correo corporativo.\n3. Seguí los pasos para crear una nueva contraseña.\n4. La nueva contraseña debe tener al menos 8 caracteres, mayúsculas y números.'),

    ('accesos', 'No tengo permisos para acceder a un recurso',
     '1. Verificá con tu supervisor que deberías tener acceso a ese recurso.\n2. Si el acceso fue aprobado, soporte lo configurará en un plazo de 24 horas.\n3. Completá el formulario de solicitud de accesos en la intranet.');
