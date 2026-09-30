-- Script de inserción para la tabla cursos
-- Niveles escolares activos en el periodo académico

INSERT INTO cursos (nivel, letra, periodo, colegio) VALUES
(
    '1° Medio', 
    'A', 
    (SELECT id_periodo FROM periodos_academicos WHERE ano = 2026 AND semestre = 1 AND colegio = (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')), 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')
),
(
    '1° Medio', 
    'B', 
    (SELECT id_periodo FROM periodos_academicos WHERE ano = 2026 AND semestre = 1 AND colegio = (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')), 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')
),
(
    '2° Medio', 
    'A', 
    (SELECT id_periodo FROM periodos_academicos WHERE ano = 2026 AND semestre = 1 AND colegio = (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')), 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')
);