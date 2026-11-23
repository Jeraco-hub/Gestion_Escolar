-- ============================================================
-- 01_crear_tablas.sql
-- Gestion Escolar - Creacion de tablas (MySQL)
-- Ejecutar sobre la base de datos: gestion_escolar
-- ============================================================

CREATE TABLE IF NOT EXISTS paises (
    id_pais INT AUTO_INCREMENT PRIMARY KEY,
    pais VARCHAR(50) NOT NULL,
    nacionalidad VARCHAR(50) NULL,
    iso2 CHAR(2) NOT NULL,
    iso3 CHAR(3) NOT NULL,
    habilitado INT DEFAULT 1
);

CREATE TABLE IF NOT EXISTS direcciones (
    id_direccion INT AUTO_INCREMENT PRIMARY KEY,
    calle VARCHAR(50) NOT NULL,
    numero VARCHAR(5) NOT NULL,
    comuna VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    habilitado INT DEFAULT 1
);

CREATE TABLE IF NOT EXISTS colegios (
    id_colegio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15) NULL,
    direccion INT NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_colegio_direccion (direccion)
);

CREATE TABLE IF NOT EXISTS periodos_academicos (
    id_periodo INT AUTO_INCREMENT PRIMARY KEY,
    ano INT NOT NULL,
    semestre INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    colegio INT NOT NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_periodo_colegio (colegio)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    colegio INT NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_usuario_colegio (colegio)
);

CREATE TABLE IF NOT EXISTS cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nivel VARCHAR(50) NOT NULL,
    letra VARCHAR(10) NOT NULL,
    periodo INT NOT NULL,
    colegio INT NOT NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_curso_periodo (periodo),
    INDEX idx_curso_colegio (colegio)
);

CREATE TABLE IF NOT EXISTS docentes (
    id_docente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(20) NOT NULL UNIQUE,
    especialidad VARCHAR(50) NULL,
    fecha_nacimiento DATE NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15) NULL,
    direccion INT NULL,
    colegio INT NOT NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_docente_direccion (direccion),
    INDEX idx_docente_colegio (colegio)
);

CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    rut VARCHAR(20) NOT NULL UNIQUE,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    fecha_nacimiento DATE NULL,
    correo VARCHAR(100) NULL,
    telefono VARCHAR(15) NULL,
    curso INT NULL,
    direccion INT NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_estudiante_curso (curso),
    INDEX idx_estudiante_direccion (direccion)
);

CREATE TABLE IF NOT EXISTS asignaturas (
    id_asignatura INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    horas_semanales INT NOT NULL,
    docente INT NULL,
    curso INT NOT NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_asignatura_docente (docente),
    INDEX idx_asignatura_curso (curso)
);

CREATE TABLE IF NOT EXISTS evaluaciones (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ponderacion FLOAT NOT NULL,
    fecha DATE NOT NULL,
    asignatura INT NOT NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_evaluacion_asignatura (asignatura)
);

CREATE TABLE IF NOT EXISTS calificaciones (
    id_calificacion INT AUTO_INCREMENT PRIMARY KEY,
    estudiante INT NOT NULL,
    evaluacion INT NOT NULL,
    nota FLOAT NOT NULL,
    fecha_registro DATE NOT NULL,
    observacion VARCHAR(255) NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_calificacion_estudiante (estudiante),
    INDEX idx_calificacion_evaluacion (evaluacion)
);

CREATE TABLE IF NOT EXISTS estados_asistencia (
    id_estado_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    estado VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(255) NULL,
    habilitado INT DEFAULT 1
);

CREATE TABLE IF NOT EXISTS asistencias (
    id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    estudiante INT NOT NULL,
    curso INT NOT NULL,
    fecha DATE NOT NULL,
    estado_asistencia INT NOT NULL,
    justificacion VARCHAR(255) NULL,
    habilitado INT DEFAULT 1,
    INDEX idx_asistencia_estudiante (estudiante),
    INDEX idx_asistencia_curso (curso),
    INDEX idx_asistencia_estado (estado_asistencia)
);