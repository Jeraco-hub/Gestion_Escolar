-- Script de inserción para la tabla asistencias
-- Registro diario de presencia de estudiantes en el aula

INSERT INTO asistencias (estudiante, curso, fecha, estado_asistencia, justificacion) VALUES
(
    (SELECT id_estudiante FROM estudiantes WHERE rut = '23.456.789-1'), 
    (SELECT id_curso FROM cursos WHERE nivel = '1° Medio' AND letra = 'A' LIMIT 1), 
    STR_TO_DATE('01/04/2026', '%d/%m/%Y'), 
    (SELECT id_estado_asistencia FROM estados_asistencia WHERE estado = 'Presente'), 
    NULL
),
(
    (SELECT id_estudiante FROM estudiantes WHERE rut = '23.789.012-3'), 
    (SELECT id_curso FROM cursos WHERE nivel = '1° Medio' AND letra = 'A' LIMIT 1), 
    STR_TO_DATE('01/04/2026', '%d/%m/%Y'), 
    (SELECT id_estado_asistencia FROM estados_asistencia WHERE estado = 'Ausente Justificado'), 
    'Presenta certificado médico por cuadro respiratorio.'
);