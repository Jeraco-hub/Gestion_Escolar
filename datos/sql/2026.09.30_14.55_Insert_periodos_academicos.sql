-- Script de inserción para la tabla periodos_academicos
-- Fechas de inicio y fin por ciclo semestral

INSERT INTO periodos_academicos (ano, semestre, fecha_inicio, fecha_fin, colegio) VALUES
(
    2026, 
    1, 
    STR_TO_DATE('01/03/2026', '%d/%m/%Y'), 
    STR_TO_DATE('10/07/2026', '%d/%m/%Y'), 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')
),
(
    2026, 
    2, 
    STR_TO_DATE('27/07/2026', '%d/%m/%Y'), 
    STR_TO_DATE('18/12/2026', '%d/%m/%Y'), 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')
);