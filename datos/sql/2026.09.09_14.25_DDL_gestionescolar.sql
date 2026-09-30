CREATE DATABASE gestion_escolar;

USE gestion_escolar;

CREATE TABLE direcciones (
    id_direccion INTEGER AUTO_INCREMENT,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(5) NOT NULL,
    comuna VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_direcciones PRIMARY KEY (id_direccion)
) COMMENT = 'Tabla de direcciones para asociar a colegios, docentes y estudiantes';

CREATE TABLE colegios (
    id_colegio INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NULL,
    direccion INTEGER NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_colegios PRIMARY KEY (id_colegio),
    CONSTRAINT fk_colegios_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion)
) COMMENT = 'Tabla de instituciones educativas o colegios';

CREATE TABLE usuarios (
    id_usuario INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    colegio INTEGER NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_usuarios PRIMARY KEY (id_usuario),
    CONSTRAINT uk_usuarios_correo UNIQUE (correo),
    CONSTRAINT fk_usuarios_colegios FOREIGN KEY (colegio) REFERENCES colegios(id_colegio)
) COMMENT = 'Tabla de usuarios del sistema con credenciales de acceso';

CREATE TABLE periodos_academicos (
    id_periodo INTEGER AUTO_INCREMENT,
    ano INTEGER NOT NULL,
    semestre INTEGER NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    colegio INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_periodos PRIMARY KEY (id_periodo),
    CONSTRAINT fk_periodos_colegios FOREIGN KEY (colegio) REFERENCES colegios(id_colegio)
) COMMENT = 'Tabla de periodos académicos anuales y semestrales';

CREATE TABLE cursos (
    id_curso INTEGER AUTO_INCREMENT,
    nivel VARCHAR(50) NOT NULL,
    letra VARCHAR(10) NOT NULL,
    periodo INTEGER NOT NULL,
    colegio INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_cursos PRIMARY KEY (id_curso),
    CONSTRAINT fk_cursos_periodos FOREIGN KEY (periodo) REFERENCES periodos_academicos(id_periodo),
    CONSTRAINT fk_cursos_colegios FOREIGN KEY (colegio) REFERENCES colegios(id_colegio)
) COMMENT = 'Tabla de cursos o niveles escolares';

CREATE TABLE docentes (
    id_docente INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(20) NOT NULL,
    especialidad VARCHAR(50) NULL,
    fecha_nacimiento DATE NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NULL,
    direccion INTEGER NULL,
    colegio INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_docentes PRIMARY KEY (id_docente),
    CONSTRAINT uk_docentes_rut UNIQUE (rut),
    CONSTRAINT uk_docentes_correo UNIQUE (correo),
    CONSTRAINT fk_docentes_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion),
    CONSTRAINT fk_docentes_colegios FOREIGN KEY (colegio) REFERENCES colegios(id_colegio)
) COMMENT = 'Tabla de profesores o docentes';

CREATE TABLE asignaturas (
    id_asignatura INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    horas_semanales INTEGER NOT NULL,
    docente INTEGER NULL,
    curso INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_asignaturas PRIMARY KEY (id_asignatura),
    CONSTRAINT fk_asignaturas_docentes FOREIGN KEY (docente) REFERENCES docentes(id_docente),
    CONSTRAINT fk_asignaturas_cursos FOREIGN KEY (curso) REFERENCES cursos(id_curso)
) COMMENT = 'Tabla de asignaturas o materias impartidas en los cursos';

CREATE TABLE estudiantes (
    id_estudiante INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(20) NOT NULL,
    matricula VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE NULL,
    correo VARCHAR(100) NULL,
    telefono VARCHAR(15) NULL,
    curso INTEGER NULL,
    direccion INTEGER NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_estudiantes PRIMARY KEY (id_estudiante),
    CONSTRAINT uk_estudiantes_rut UNIQUE (rut),
    CONSTRAINT uk_estudiantes_matricula UNIQUE (matricula),
    CONSTRAINT fk_estudiantes_cursos FOREIGN KEY (curso) REFERENCES cursos(id_curso),
    CONSTRAINT fk_estudiantes_direcciones FOREIGN KEY (direccion) REFERENCES direcciones(id_direccion)
) COMMENT = 'Tabla de estudiantes matriculados';

CREATE TABLE evaluaciones (
    id_evaluacion INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    ponderacion FLOAT NOT NULL,
    fecha DATE NOT NULL,
    asignatura INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_evaluaciones PRIMARY KEY (id_evaluacion),
    CONSTRAINT fk_evaluaciones_asignaturas FOREIGN KEY (asignatura) REFERENCES asignaturas(id_asignatura)
) COMMENT = 'Tabla de evaluaciones o pruebas asociadas a una asignatura';

CREATE TABLE calificaciones (
    id_calificacion INTEGER AUTO_INCREMENT,
    estudiante INTEGER NOT NULL,
    evaluacion INTEGER NOT NULL,
    nota FLOAT NOT NULL,
    fecha_registro DATE NOT NULL,
    observacion VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_calificaciones PRIMARY KEY (id_calificacion),
    CONSTRAINT fk_calificaciones_estudiantes FOREIGN KEY (estudiante) REFERENCES estudiantes(id_estudiante),
    CONSTRAINT fk_calificaciones_evaluaciones FOREIGN KEY (evaluacion) REFERENCES evaluaciones(id_evaluacion)
) COMMENT = 'Tabla de notas u calificaciones obtenidas por los estudiantes';

CREATE TABLE estados_asistencia (
    id_estado_asistencia INTEGER AUTO_INCREMENT,
    estado VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_estados_asistencia PRIMARY KEY (id_estado_asistencia),
    CONSTRAINT uk_estados_asistencia_estado UNIQUE (estado)
) COMMENT = 'Tabla del catálogo de estados de asistencia';

CREATE TABLE asistencias (
    id_asistencia INTEGER AUTO_INCREMENT,
    estudiante INTEGER NOT NULL,
    curso INTEGER NOT NULL,
    fecha DATE NOT NULL,
    estado_asistencia INTEGER NOT NULL,
    justificacion VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_asistencias PRIMARY KEY (id_asistencia),
    CONSTRAINT fk_asistencias_estudiantes FOREIGN KEY (estudiante) REFERENCES estudiantes(id_estudiante),
    CONSTRAINT fk_asistencias_cursos FOREIGN KEY (curso) REFERENCES cursos(id_curso),
    CONSTRAINT fk_asistencias_estados FOREIGN KEY (estado_asistencia) REFERENCES estados_asistencia(id_estado_asistencia)
) COMMENT = 'Tabla de registros diarios de asistencia de los estudiantes';