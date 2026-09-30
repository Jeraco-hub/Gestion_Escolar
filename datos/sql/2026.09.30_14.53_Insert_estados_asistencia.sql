-- Script de inserción para la tabla estados_asistencia
-- Catálogo de estados diarios del estudiante en el aula

INSERT INTO estados_asistencia (estado, descripcion) VALUES
('Presente', 'El estudiante asistió puntualmente a la jornada de clases.'),
('Ausente Injustificado', 'El estudiante no se presentó a clases y no existe justificativo médico ni del apoderado.'),
('Ausente Justificado', 'El estudiante no asistió pero cuenta con certificado médico o aviso formal del apoderado.'),
('Atraso', 'El estudiante ingresó a la sala de clases posterior al horario establecido.'),
('Retirado', 'El estudiante fue retirado del establecimiento antes del término de la jornada por su apoderado.');