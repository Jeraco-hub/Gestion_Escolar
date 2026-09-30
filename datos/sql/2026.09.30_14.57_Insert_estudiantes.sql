-- Script de inserción para la tabla estudiantes
-- Alumnos matriculados en los distintos niveles

INSERT INTO estudiantes (nombre, apellido, rut, matricula, fecha_nacimiento, correo, telefono, curso, direccion) VALUES
(
    'Sebastián Ignacio', 
    'Morales Rivera', 
    '23.456.789-1', 
    'MAT-2026-001', 
    STR_TO_DATE('14/03/2010', '%d/%m/%Y'), 
    'smorales@alumnos.cl', 
    '+56955512345', 
    (SELECT id_curso FROM cursos WHERE nivel = '1° Medio' AND letra = 'A' LIMIT 1), 
    (SELECT id_direccion FROM direcciones WHERE calle = 'Pasaje Las Camelias' AND numero = '12')
),
(
    'Valentina Paz', 
    'Contreras Soto', 
    '23.789.012-3', 
    'MAT-2026-002', 
    STR_TO_DATE('22/09/2010', '%d/%m/%Y'), 
    'vcontreras@alumnos.cl', 
    '+56955567890', 
    (SELECT id_curso FROM cursos WHERE nivel = '1° Medio' AND letra = 'A' LIMIT 1), 
    (SELECT id_direccion FROM direcciones WHERE calle = 'Calle San Martín' AND numero = '321')
);