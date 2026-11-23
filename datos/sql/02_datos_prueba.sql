-- ============================================================
-- 02_datos_prueba.sql
-- Gestion Escolar - Datos de prueba
-- Ejecutar despues de 01_crear_tablas.sql
-- ============================================================

INSERT INTO paises (pais, nacionalidad, iso2, iso3) VALUES
('Chile', 'Chilena', 'CL', 'CHL'),
('Argentina', 'Argentina', 'AR', 'ARG'),
('Peru', 'Peruana', 'PE', 'PER');

INSERT INTO direcciones (calle, numero, comuna, ciudad) VALUES
('Av. Siempre Viva', '742', 'Springfield', 'Santiago'),
('Calle Falsa', '123', 'Centro', 'Valparaiso');

INSERT INTO colegios (nombre, telefono, direccion) VALUES
('Colegio Nacional', '+56911111111', 1);

INSERT INTO periodos_academicos (ano, semestre, fecha_inicio, fecha_fin, colegio) VALUES
(2025, 1, '2025-03-01', '2025-07-15', 1),
(2025, 2, '2025-08-01', '2025-12-15', 1);

INSERT INTO usuarios (nombre, correo, contrasena, colegio) VALUES
('Administrador', 'admin@colegio.cl', '$2b$12$Egsob/eYWEHRSvSWtBsRVuhxoHfBWr6qRjKPLXyeYeqi71QrPodU6', 1);

INSERT INTO cursos (nivel, letra, periodo, colegio) VALUES
('1 Medio', 'A', 1, 1),
('1 Medio', 'B', 1, 1),
('2 Medio', 'A', 1, 1);

INSERT INTO docentes (nombre, apellido, rut, especialidad, fecha_nacimiento, correo, telefono, direccion, colegio) VALUES
('Juan', 'Perez', '11111111-1', 'Matematica', '1980-05-10', 'juan.perez@colegio.cl', '+56922222222', 1, 1),
('Maria', 'Gonzalez', '22222222-2', 'Lenguaje', '1985-08-20', 'maria.gonzalez@colegio.cl', '+56933333333', 2, 1);

INSERT INTO estudiantes (nombre, apellido, rut, matricula, fecha_nacimiento, correo, telefono, curso, direccion) VALUES
('Pedro', 'Ramirez', '33333333-3', 'MAT-001', '2010-01-15', 'pedro.ramirez@alumno.cl', '+56944444444', 1, 1),
('Ana', 'Lopez', '44444444-4', 'MAT-002', '2010-03-22', 'ana.lopez@alumno.cl', '+56955555555', 1, 2);

INSERT INTO asignaturas (nombre, horas_semanales, docente, curso) VALUES
('Matematica', 6, 1, 1),
('Lenguaje', 6, 2, 1),
('Ciencias', 4, 1, 1);

INSERT INTO evaluaciones (nombre, ponderacion, fecha, asignatura) VALUES
('Prueba 1', 30, '2025-04-15', 1),
('Examen', 40, '2025-06-20', 1);

INSERT INTO calificaciones (estudiante, evaluacion, nota, fecha_registro, observacion) VALUES
(1, 1, 6.5, '2025-04-20', 'Buen desempeno'),
(2, 1, 5.8, '2025-04-20', NULL);

INSERT INTO estados_asistencia (estado, descripcion) VALUES
('Presente', 'Asistio a clases'),
('Ausente', 'No asistio sin justificacion'),
('Justificado', 'Ausencia con justificacion');

INSERT INTO asistencias (estudiante, curso, fecha, estado_asistencia, justificacion) VALUES
(1, 1, '2025-04-15', 1, NULL),
(2, 1, '2025-04-15', 2, 'Certificado medico');