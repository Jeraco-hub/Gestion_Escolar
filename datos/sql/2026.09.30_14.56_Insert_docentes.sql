-- Script de inserción para la tabla docentes
-- Profesores adscritos al establecimiento educacional

INSERT INTO docentes (nombre, apellido, rut, especialidad, fecha_nacimiento, correo, telefono, direccion, colegio) VALUES
(
    'Claudio Andrés', 
    'Bravo Muñoz', 
    '15.420.312-8', 
    'Matemáticas y Física', 
    STR_TO_DATE('18/06/1984', '%d/%m/%Y'), 
    'cbravo@liceoexperimental.cl', 
    '+56987654321', 
    (SELECT id_direccion FROM direcciones WHERE calle = 'Calle Los Alerces' AND numero = '450'), 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')
),
(
    'Andrea Nicole', 
    'Fuentes Tapia', 
    '16.890.543-K', 
    'Lengua y Literatura', 
    STR_TO_DATE('04/11/1987', '%d/%m/%Y'), 
    'afuentes@liceoexperimental.cl', 
    '+56912345678', 
    (SELECT id_direccion FROM direcciones WHERE calle = 'Av. Vicuña Mackenna' AND numero = '7890'), 
    (SELECT id_colegio FROM colegios WHERE nombre = 'Liceo Experimental Santiago')
);