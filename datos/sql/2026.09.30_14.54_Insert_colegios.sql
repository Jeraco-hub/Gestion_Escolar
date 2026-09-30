-- Script de inserción para la tabla colegios
-- Instituciones educativas registradas en el sistema

INSERT INTO colegios (nombre, telefono, direccion) VALUES
(
    'Liceo Experimental Santiago', 
    '+56222223344', 
    (SELECT id_direccion FROM direcciones WHERE calle = 'Av. Libertador Bernardo O''Higgins' AND numero = '1050')
),
(
    'Colegio Bicentenario Providencia', 
    '+56223334455', 
    (SELECT id_direccion FROM direcciones WHERE calle = 'Av. Pedro de Valdivia' AND numero = '1234')
);