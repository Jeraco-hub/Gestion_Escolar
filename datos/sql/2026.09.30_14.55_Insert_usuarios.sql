-- Script de inserción para la tabla usuarios
-- Credenciales de acceso de directivos y administradores del establecimiento

INSERT INTO usuarios (nombre, correo, contrasena, colegio) VALUES
(
    'Rodrigo González Valenzuela', 
    'admin.santiago@gestion.cl', 
    '$2y$10$wE7YgJ6vYlq8lKm8U9n5eeuHk2g8W5tL4yR9z7oM3xJ1qW5vA1bCe', 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')
),
(
    'Marcela Paz Sepúlveda', 
    'direccion.providencia@gestion.cl', 
    '$2y$10$tM3xJ1qW5vA1bCewE7YgJ6vYlq8lKm8U9n5eeuHk2g8W5tL4yR9z7o', 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Colegio Bicentenario Providencia')
);