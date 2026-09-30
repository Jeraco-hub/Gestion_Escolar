-- Script de inserción para la tabla calificaciones
-- Registro de calificaciones obtenidas por los estudiantes

INSERT INTO calificaciones (estudiante, evaluacion, nota, fecha_registro, observacion) VALUES
(
    (SELECT id_estudiante FROM estudiantes WHERE rut = '23.456.789-1'), 
    (SELECT id_evaluacion FROM evaluaciones WHERE nombre = 'Control 1: Ecuaciones de Primer Grado'), 
    6.5, 
    STR_TO_DATE('18/04/2026', '%d/%m/%Y'), 
    'Excelente desempeño en desarrollo de ejercicios algebraicos.'
),
(
    (SELECT id_estudiante FROM estudiantes WHERE rut = '23.789.012-3'), 
    (SELECT id_evaluacion FROM evaluaciones WHERE nombre = 'Control 1: Ecuaciones de Primer Grado'), 
    5.8, 
    STR_TO_DATE('18/04/2026', '%d/%m/%Y'), 
    'Buen trabajo, corregir errores de signo.'
),
(
    (SELECT id_estudiante FROM estudiantes WHERE rut = '23.456.789-1'), 
    (SELECT id_evaluacion FROM evaluaciones WHERE nombre = 'Control de Lectura: Subterra'), 
    7.0, 
    STR_TO_DATE('12/04/2026', '%d/%m/%Y'), 
    'Destacada comprensión lectora.'
);