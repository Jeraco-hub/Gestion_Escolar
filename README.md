# Sistema de Gestión Escolar - POO

## Integrantes

- **Darío**
- **Miguel Nahuel**

**Asignatura:** Programación Orientada a Objetos - Evaluación N°3

Aplicación de gestión escolar desarrollada bajo el paradigma de **Programación Orientada a Objetos (POO)**, con diseño modular en capas y persistencia en **MySQL** mediante el ORM **Peewee**.

---

## 1. Conceptos de POO y Arquitectura

El sistema está diseñado siguiendo principios de ingeniería de software orientados a la mantenibilidad y extensibilidad:

| Concepto POO | Implementación en el Proyecto |
|---|---|
| **Clase / Modelo** | Molde que define la estructura y tipos de datos (ej: `Estudiante`, `Docente`, `Colegio`, `Pais`). Heredan de `ModelBase`. |
| **Objeto / Instancia** | Cada registro o fila obtenido de la base de datos se manipula como una instancia en memoria en Python. |
| **Atributos** | Campos del modelo mapeados a columnas SQL (`rut`, `nombre`, `matricula`, `correo`, `iso2`, etc.). |
| **Métodos y Persistencia** | Métodos como `.save()`, `.create()`, `.select()` y `.update()` para operaciones CRUD. |
| **Herencia** | Todas las clases de entidad heredan de `ModelBase`, la cual comparte la conexión activa a MySQL. |
| **Encapsulamiento** | Cada capa maneja su propia responsabilidad interna; la presentación no realiza consultas SQL directas. |
| **Abstracción** | Los repositorios exponen funciones claras (`listado_estudiantes()`, `registrar_estudiante()`) sin exponer detalles de bajo nivel. |

---

## 2. Estructura Modular del Proyecto

El proyecto implementa una arquitectura en capas con **alta cohesión** y **bajo acoplamiento**:

```text
Gestion_Escolar/
│
├── main.py                         # Punto de entrada (login + menú principal)
├── .env.example                   # Plantilla de variables de entorno para MySQL
├── requirements.txt               # Dependencias del proyecto
├── README.md                      # Documentación del sistema
│
├── auxiliares/                    # Constantes globales y configuración transversal
│   ├── __init__.py
│   ├── datos_app.py               # Nombre de app, versión y restricciones por defecto
│   ├── entradas.py                # Helpers de entrada (pedir_texto, pedir_entero, pedir_fecha, pedir_ponderacion)
│   ├── menu_app.py                # Textos y opciones de los menús de consola
│   └── validaciones.py            # Validaciones de RUT, correo, largo, fecha y contraseña
│
├── datos/                         # Capa de Acceso a Datos y Persistencia
│   ├── __init__.py
│   ├── conexion.py                # Conexión centralizada a MySQL con Peewee y Decouple
│   ├── model_base.py               # Clase base ORM (ModelBase) compartida por los modelos
│   │
│   ├── modelos/                   # Modelos de datos (Clases ORM)
│   │   ├── asignatura.py
│   │   ├── asistencia.py
│   │   ├── calificacion.py
│   │   ├── colegio.py
│   │   ├── curso.py
│   │   ├── direccion.py
│   │   ├── docente.py
│   │   ├── estado_asistencia.py
│   │   ├── estudiante.py
│   │   ├── evaluacion.py
│   │   ├── pais.py
│   │   ├── periodo_academico.py
│   │   └── usuario.py
│   │
│   ├── repositorio/              # Operaciones CRUD por cada entidad
│   │   ├── __init__.py
│   │   ├── repo_asignatura.py
│   │   ├── repo_asistencia.py
│   │   ├── repo_calificacion.py
│   │   ├── repo_colegio.py
│   │   ├── repo_curso.py
│   │   ├── repo_direccion.py
│   │   ├── repo_docente.py
│   │   ├── repo_estado_asistencia.py
│   │   ├── repo_estudiante.py
│   │   ├── repo_evaluacion.py
│   │   ├── repo_periodo_academico.py
│   │   ├── repo_usuario.py
│   │   └── repositorio_pais.py
│   │
│   └── sql/                       # Scripts DDL de creación y carga de datos iniciales
│       ├── 01_crear_tablas.sql    # DDL canónico (13 tablas)
│       ├── 02_datos_prueba.sql
│       ├── 2026.09.09_14.25_DDL_gestionescolar.sql  # Histórico (Evaluación 2)
│       └── 2026.09.30_*.sql       # Inserts por tabla
│
├── negocio/                       # Capa de Lógica de Negocio y Reglas
│   ├── __init__.py
│   ├── negocio_asignatura.py
│   ├── negocio_asistencia.py
│   ├── negocio_calificacion.py
│   ├── negocio_colegio.py
│   ├── negocio_curso.py
│   ├── negocio_direccion.py
│   ├── negocio_docente.py
│   ├── negocio_estado_asistencia.py
│   ├── negocio_estudiante.py
│   ├── negocio_evaluacion.py
│   ├── negocio_login.py
│   ├── negocio_pais.py
│   ├── negocio_periodo_academico.py
│   └── negocio_usuario.py
│
└── presentacion/                  # Capa de Presentación e Interfaz de Consola
    ├── __init__.py
    ├── menu.py                    # Menú de consola y visualización formateada
    ├── presentacion_asignatura.py
    ├── presentacion_asistencia.py
    ├── presentacion_calificacion.py
    ├── presentacion_colegio.py
    ├── presentacion_curso.py
    ├── presentacion_direccion.py
    ├── presentacion_docente.py
    ├── presentacion_estado_asistencia.py
    ├── presentacion_estudiante.py
    ├── presentacion_evaluacion.py
    ├── presentacion_login.py
    ├── presentacion_pais.py
    ├── presentacion_periodo_academico.py
    └── presentacion_usuario.py
```

---

## 3. Entidades del Sistema Escolar

1. **`Paises`**: Catálogo de países con nacionalidad e ISO 2/ISO 3.
2. **`Direcciones`**: Registro de domicilios de colegios, docentes y estudiantes.
3. **`Colegios`**: Instituciones educativas administradas por el sistema.
4. **`Usuarios`**: Cuentas del sistema con credenciales de acceso (login).
5. **`PeriodosAcademicos`**: Años escolares y semestres lectivos.
6. **`Cursos`**: Niveles y letras (ej: 1° Medio A) asociados a un periodo y colegio.
7. **`Docentes`**: Profesores con especialidad, RUT, contacto y establecimiento asociado.
8. **`Asignaturas`**: Materias impartidas en los cursos con horas semanales y docente asignado.
9. **`Estudiantes`**: Alumnos matriculados con RUT, matrícula, curso y datos personales.
10. **`Evaluaciones`**: Pruebas, trabajos o certámenes ponderados por asignatura.
11. **`Calificaciones`**: Registro de notas obtenidas por los estudiantes en las evaluaciones.
12. **`Asistencias`** y **`EstadosAsistencia`**: Control diario de asistencia (Presente, Ausente, Justificado).

---

## 4. Requisitos y Dependencias

- **Python**: 3.11 o superior.
- **MySQL Server**: 8.0 o compatible.

### Instalación:

```powershell
python -m pip install -r requirements.txt
```

---

## 5. Configuración de Base de Datos

### Paso 1: Crear la Base de Datos y Tablas

1. Abrir MySQL Workbench o cliente por consola.
2. Crear la base de datos `gestion_escolar`.
3. Ejecutar `datos/sql/01_crear_tablas.sql` (crea todas las tablas).
4. (Opcional) Ejecutar `datos/sql/02_datos_prueba.sql` para datos de prueba (incluye `admin@colegio.cl` / `Admin#2026`).

### Paso 2: Crear el archivo `.env` (copiar `.env.example` y completar)

```dotenv
db=gestion_escolar
host=localhost
port=3306
user=root
password=tu_contraseña_aqui
```

> El archivo `.env` está protegido por `.gitignore`.

---

## 6. Ejecución del Sistema

```powershell
python main.py
```

Al arrancar, aparece el **Inicio de Sesión**. Ingresa con:

- **Correo**: `admin@colegio.cl`
- **Contraseña**: `Admin#2026`

---

## 7. Funcionalidades Implementadas

### Login
- Autenticación contra `usuarios` (correo + contraseña).
- Contraseña oculta con `maskpass`.
- Contraseñas almacenadas con hash bcrypt (nunca en texto plano).
- Máximo 3 intentos.

### Módulos con CRUD completo (3 capas)

| Módulo | Listar | Registrar | Modificar | Eliminar (lógico) |
|---|---|---|---|---|
| Estudiantes | ✅ | ✅ | ✅ | ✅ |
| Docentes | ✅ | ✅ | ✅ | ✅ |
| Cursos | ✅ | ✅ | ✅ | ✅ |
| Asignaturas | ✅ | ✅ | ✅ | ✅ |
| Calificaciones | ✅ | ✅ | ✅ | ✅ |
| Evaluaciones | ✅ | ✅ | ✅ | ✅ |
| Usuarios | ✅ | ✅ | ✅ | ✅ |
| Países | ✅ | ✅ | ✅ | ✅ |
| Estados de Asistencia | ✅ | ✅ | ✅ | ✅ |
| Direcciones | ✅ | ✅ | ✅ | ✅ |
| Colegios | ✅ | ✅ | ✅ | ✅ |
| Períodos Académicos | ✅ | ✅ | ✅ | ✅ |
| Asistencias | ✅ | ✅ | ✅ | ✅ |

### Consultas especiales
- **Calificaciones por Estudiante** con promedio.
- **Asistencias por Estudiante**.
- **Asistencias por Curso y Fecha**.

### Menú Principal

```
[1] - Gestión de Estudiantes
[2] - Gestión de Docentes
[3] - Gestión de Cursos y Asignaturas
[4] - Reportes y Calificaciones
[5] - Configuración del Sistema
[6] - Gestión de Usuarios
[0] - Salir
```

### Configuración del Sistema

```
[1] - Información de la Aplicación
[2] - Gestión de Países
[3] - Gestión de Estados de Asistencia
[4] - Gestión de Direcciones
[5] - Gestión de Colegios
[6] - Gestión de Períodos Académicos
[0] - Volver al Menú Principal
```

### Reportes y Calificaciones

```
[1] - Listado de Calificaciones
[2] - Calificaciones por Estudiante (con promedio)
[3] - Registrar Calificación
[4] - Modificar Calificación
[5] - Eliminar Calificación (Borrado Lógico)
[6] - Listado de Evaluaciones
[7] - Registrar Evaluación
[8] - Modificar Evaluación
[9] - Eliminar Evaluación (Borrado Lógico)
[10] - Listado de Asistencias
[11] - Asistencias por Estudiante
[12] - Asistencias por Curso y Fecha
[13] - Registrar Asistencia
[14] - Modificar Asistencia
[15] - Eliminar Asistencia (Borrado Lógico)
[0] - Volver al Menú Principal
```

---

## 8. Convenciones de Trabajo

- **3 capas**: `datos/` → `negocio/` → `presentacion/`.
- **Borrado lógico**: todas las entidades usan `habilitado = 1/0`, nunca `DELETE`.
- **Nombres claros**: módulos, clases, funciones y variables descriptivas.
- **Sin SQL en presentación**: la presentación solo llama a negocio.
- **Credenciales fuera del código**: `.env` + `python-decouple`.
