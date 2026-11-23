-- Usuario inicial del sistema (para el login)
-- Correo: admin@colegio.cl | Contraseña: Admin#2026 (se guarda con hash bcrypt)
INSERT INTO usuarios (nombre, correo, contrasena, colegio) VALUES
(
    'Administrador',
    'admin@colegio.cl',
    '$2b$12$Egsob/eYWEHRSvSWtBsRVuhxoHfBWr6qRjKPLXyeYeqi71QrPodU6',
    (SELECT id_colegio FROM colegios ORDER BY id_colegio LIMIT 1)
)
ON DUPLICATE KEY UPDATE contrasena = '$2b$12$Egsob/eYWEHRSvSWtBsRVuhxoHfBWr6qRjKPLXyeYeqi71QrPodU6', habilitado = 1;