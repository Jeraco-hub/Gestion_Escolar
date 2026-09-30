CREATE DATABASE gestion_escolar;

USE gestion_escolar;

CREATE TABLE direccion (
    id_direccion INTEGER AUTO_INCREMENT,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(5) NOT NULL,
    comuna INTEGER NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_direccion PRIMARY KEY (id_direccion)
) COMMENT = 'Tabla de direcciones para asociar a colegios, docentes y estudiantes';

CREATE TABLE colegio (
    id_colegio INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NULL,
    direccion INTEGER NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_colegio PRIMARY KEY (id_colegio),
    CONSTRAINT fk_colegio_direccion FOREIGN KEY (direccion) REFERENCES direccion(id_direccion)
) COMMENT = 'Tabla de instituciones educativas o colegios';

CREATE TABLE usuario (
    id_usuario INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    colegio INTEGER NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_usuario PRIMARY KEY (id_usuario),
    CONSTRAINT uk_usuario_correo UNIQUE (correo),
    CONSTRAINT fk_usuario_colegio FOREIGN KEY (colegio) REFERENCES colegio(id_colegio)
) COMMENT = 'Tabla de usuarios del sistema con credenciales de acceso';

CREATE TABLE periodo_academico (
    id_periodo INTEGER AUTO_INCREMENT,
    ano INTEGER NOT NULL,
    semestre INTEGER NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    colegio INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_periodo PRIMARY KEY (id_periodo),
    CONSTRAINT fk_periodo_colegio FOREIGN KEY (colegio) REFERENCES colegio(id_colegio)
) COMMENT = 'Tabla de periodos académicos anuales y semestrales';

CREATE TABLE curso (
    id_curso INTEGER AUTO_INCREMENT,
    nivel VARCHAR(50) NOT NULL,
    letra VARCHAR(10) NOT NULL,
    periodo INTEGER NOT NULL,
    colegio INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_curso PRIMARY KEY (id_curso),
    CONSTRAINT fk_curso_periodo FOREIGN KEY (periodo) REFERENCES periodo_academico(id_periodo),
    CONSTRAINT fk_curso_colegio FOREIGN KEY (colegio) REFERENCES colegio(id_colegio)
) COMMENT = 'Tabla de cursos o niveles escolares';

CREATE TABLE docente (
    id_docente INTEGER AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE NULL,
    correo VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NULL,
    direccion INTEGER NULL,
    colegio INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_docente PRIMARY KEY (id_docente),
    CONSTRAINT uk_docente_rut UNIQUE (rut),
    CONSTRAINT uk_docente_correo UNIQUE (correo),
    CONSTRAINT fk_docente_direccion FOREIGN KEY (direccion) REFERENCES direccion(id_direccion),
    CONSTRAINT fk_docente_colegio FOREIGN KEY (colegio) REFERENCES colegio(id_colegio)
) COMMENT = 'Tabla de profesores o docentes';

CREATE TABLE asignatura (
    id_asignatura INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    horas_semanales INTEGER NOT NULL,
    docente INTEGER NULL,
    curso INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_asignatura PRIMARY KEY (id_asignatura),
    CONSTRAINT fk_asignatura_docente FOREIGN KEY (docente) REFERENCES docente(id_docente),
    CONSTRAINT fk_asignatura_curso FOREIGN KEY (curso) REFERENCES curso(id_curso)
) COMMENT = 'Tabla de asignaturas o materias impartidas en los cursos';

CREATE TABLE estudiante (
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
    
    CONSTRAINT pk_estudiante PRIMARY KEY (id_estudiante),
    CONSTRAINT uk_estudiante_rut UNIQUE (rut),
    CONSTRAINT uk_estudiante_matricula UNIQUE (matricula),
    CONSTRAINT fk_estudiante_curso FOREIGN KEY (curso) REFERENCES curso(id_curso),
    CONSTRAINT fk_estudiante_direccion FOREIGN KEY (direccion) REFERENCES direccion(id_direccion)
) COMMENT = 'Tabla de estudiantes matriculados';

CREATE TABLE evaluacion (
    id_evaluacion INTEGER AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    ponderacion FLOAT NOT NULL,
    fecha DATE NOT NULL,
    asignatura INTEGER NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_evaluacion PRIMARY KEY (id_evaluacion),
    CONSTRAINT fk_evaluacion_asignatura FOREIGN KEY (asignatura) REFERENCES asignatura(id_asignatura)
) COMMENT = 'Tabla de evaluaciones o pruebas asociadas a una asignatura';

CREATE TABLE calificacion (
    id_calificacion INTEGER AUTO_INCREMENT,
    estudiante INTEGER NOT NULL,
    evaluacion INTEGER NOT NULL,
    nota FLOAT NOT NULL,
    fecha_registro DATE NOT NULL,
    observacion VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_calificacion PRIMARY KEY (id_calificacion),
    CONSTRAINT fk_calificacion_estudiante FOREIGN KEY (estudiante) REFERENCES estudiante(id_estudiante),
    CONSTRAINT fk_calificacion_evaluacion FOREIGN KEY (evaluacion) REFERENCES evaluacion(id_evaluacion)
) COMMENT = 'Tabla de notas u calificaciones obtenidas por los estudiantes';

CREATE TABLE estado_asistencia (
    id_estado_asistencia INTEGER AUTO_INCREMENT,
    estado VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_estado_asistencia PRIMARY KEY (id_estado_asistencia),
    CONSTRAINT uk_estado_nombre UNIQUE (estado)
) COMMENT = 'Tabla del catálogo de estados de asistencia';

CREATE TABLE asistencia (
    id_asistencia INTEGER AUTO_INCREMENT,
    estudiante INTEGER NOT NULL,
    curso INTEGER NOT NULL,
    fecha DATE NOT NULL,
    estado_asistencia INTEGER NOT NULL,
    justificacion VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_asistencia PRIMARY KEY (id_asistencia),
    CONSTRAINT fk_asistencia_estudiante FOREIGN KEY (estudiante) REFERENCES estudiante(id_estudiante),
    CONSTRAINT fk_asistencia_curso FOREIGN KEY (curso) REFERENCES curso(id_curso),
    CONSTRAINT fk_asistencia_estado FOREIGN KEY (estado_asistencia) REFERENCES estado_asistencia(id_estado_asistencia)
) COMMENT = 'Tabla de registros diarios de asistencia de los estudiantes';