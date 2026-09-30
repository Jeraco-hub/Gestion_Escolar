-- Script de inserción para la tabla asignaturas
-- Asignaturas asignadas a un docente y a un curso

INSERT INTO asignaturas (nombre, horas_semanales, docente, curso) VALUES
(
    'Álgebra y Funciones', 
    6, 
    (SELECT id_docente FROM docentes WHERE rut = '15.420.312-8'), 
    (SELECT id_curso FROM cursos WHERE nivel = '1° Medio' AND letra = 'A' LIMIT 1)
),
(
    'Lenguaje y Comunicación', 
    6, 
    (SELECT id_docente FROM docentes WHERE rut = '16.890.543-K'), 
    (SELECT id_curso FROM cursos WHERE nivel = '1° Medio' AND letra = 'A' LIMIT 1)
);