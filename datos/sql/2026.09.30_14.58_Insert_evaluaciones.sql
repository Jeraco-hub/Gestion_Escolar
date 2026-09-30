-- Script de inserción para la tabla evaluaciones
-- Planificación de pruebas y ponderaciones

INSERT INTO evaluaciones (nombre, ponderacion, fecha, asignatura) VALUES
(
    'Control 1: Ecuaciones de Primer Grado', 
    0.20, 
    STR_TO_DATE('15/04/2026', '%d/%m/%Y'), 
    (SELECT id_asignatura FROM asignaturas WHERE nombre = 'Álgebra y Funciones' LIMIT 1)
),
(
    'Prueba Parcial: Sistemas Lineales', 
    0.35, 
    STR_TO_DATE('20/05/2026', '%d/%m/%Y'), 
    (SELECT id_asignatura FROM asignaturas WHERE nombre = 'Álgebra y Funciones' LIMIT 1)
),
(
    'Control de Lectura: Subterra', 
    0.25, 
    STR_TO_DATE('10/04/2026', '%d/%m/%Y'), 
    (SELECT id_asignatura FROM asignaturas WHERE nombre = 'Lenguaje y Comunicación' LIMIT 1)
);