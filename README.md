# Sistema de Gestión Escolar - POO

Aplicación de gestión escolar desarrollada bajo el paradigma de **Programación Orientada a Objetos (POO)**, con diseño modular en capas y persistencia en **MySQL** mediante el ORM **Peewee**.

---

## 1. Conceptos de POO y Arquitectura

El sistema está diseñado siguiendo principios de ingeniería de software orientados a la mantenibilidad y extensibilidad:

| Concepto POO | Implementación en el Proyecto |
|---|---|
| **Clase / Modelo** | Molde que define la estructura y tipos de datos (ej: `Estudiante`, `Docente`, `Colegio`). Heredan de `BaseModel`. |
| **Objeto / Instancia** | Cada registro o fila obtenido de la base de datos se manipula como una instancia en memoria en Python. |
| **Atributos** | Campos del modelo mapeados a columnas SQL (`rut`, `nombre`, `matricula`, `correo`, etc.). |
| **Métodos y Persistencia** | Métodos como `.save()`, `.create()`, `.select()` y `.update()` para operaciones CRUD. |
| **Herencia** | Todas las clases de entidad heredan de `BaseModel`, la cual comparte la conexión activa a MySQL. |
| **Encapsulamiento** | Cada capa maneja su propia responsabilidad interna; la presentación no realiza consultas SQL directas. |
| **Abstracción** | Los repositorios exponen funciones claras (`listado_estudiantes()`, `registrar_estudiante()`) sin exponer detalles de bajo nivel. |

---

## 2. Estructura Modular del Proyecto

El proyecto implementa una arquitectura en capas con **alta cohesión** y **bajo acoplamiento**:

```text
Gestion_Escolar/
│
├── app.py                         # Punto de entrada principal de la aplicación
├── .env                           # Variables de entorno para credenciales de MySQL (excluido en git)
├── requirements.txt               # Dependencias del proyecto
├── README.md                      # Documentación del sistema
│
├── auxiliares/                    # Constantes globales y configuración transversal
│   ├── __init__.py
│   └── datos_app.py               # Nombre de app, versión y restricciones por defecto
│
├── datos/                         # Capa de Acceso a Datos y Persistencia
│   ├── __init__.py
│   ├── conexion.py                # Conexión centralizada a MySQL con Peewee y Decouple
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
│   │   ├── periodo_academico.py
│   │   └── usuario.py
│   │
│   ├── repositorios/              # Operaciones CRUD por cada entidad
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
│   │   └── repo_usuario.py
│   │
│   └── sql/                       # Scripts DDL de creación y carga de datos iniciales
│       ├── 2026.09.09_14.25_DDL_gestionescolar.sql
│       ├── 2026.09.30_14.53_Insert_direcciones.sql
│       ├── 2026.09.30_14.53_Insert_estados_asistencia.sql
│       ├── 2026.09.30_14.54_Insert_colegios.sql
│       ├── 2026.09.30_14.55_Insert_periodos_academicos.sql
│       ├── 2026.09.30_14.55_Insert_usuarios.sql
│       ├── 2026.09.30_14.56_Insert_cursos.sql
│       ├── 2026.09.30_14.56_Insert_docentes.sql
│       ├── 2026.09.30_14.57_Insert_asignaturas.sql
│       ├── 2026.09.30_14.57_Insert_estudiantes.sql
│       ├── 2026.09.30_14.58_Insert_calificaciones.sql
│       ├── 2026.09.30_14.58_Insert_evaluaciones.sql
│       └── 2026.09.30_14.59_Insert_asistencias.sql
│
├── negocio/                       # Capa de Lógica de Negocio y Reglas
│   └── __init__.py
│
└── presentacion/                  # Capa de Presentación e Interfaz de Consola
    ├── __init__.py
    └── menu.py                    # Menú de consola y visualización formateada
```

---

## 3. Entidades del Sistema Escolar

El dominio modela de forma integral la gestión académica y administrativa de una institución educativa:

1. **`Direcciones`**: Registro de domicilios de colegios, docentes y estudiantes.
2. **`Colegios`**: Instituciones educativas administradas por el sistema.
3. **`Usuarios`**: Cuentas del sistema con credenciales de acceso.
4. **`PeriodosAcademicos`**: Años escolares y semestres lectivos.
5. **`Cursos`**: Niveles y letras (ej: 1° Medio A) asociados a un periodo y colegio.
6. **`Docentes`**: Profesores con especialidad, RUT, contacto y establecimiento asociado.
7. **`Asignaturas`**: Materias impartidas en los cursos con horas semanales y docente asignado.
8. **`Estudiantes`**: Alumnos matriculados con RUT, matrícula, curso y datos personales.
9. **`Evaluaciones`**: Pruebas, trabajos o certámenes ponderados por asignatura.
10. **`Calificaciones`**: Registro de notas obtenidas por los estudiantes en las evaluaciones.
11. **`Asistencias`** y **`EstadosAsistencia`**: Control diario de asistencia (Presente, Ausente, Justificado).

---

## 4. Requisitos y Dependencias

- **Python**: 3.11 o superior.
- **MySQL Server**: 8.0 o compatible en ejecución local o remota.

### Instalación de dependencias:

```powershell
python -m pip install peewee PyMySQL python-decouple prettytable
```

O utilizando el archivo de requerimientos:

```powershell
python -m pip install -r requirements.txt
```

---

## 5. Configuración de Base de Datos

### Paso 1: Crear la Base de Datos y Tablas
1. Abrir MySQL Workbench o cliente por consola.
2. Ejecutar el script DDL ubicado en `datos/sql/2026.09.09_14.25_DDL_gestionescolar.sql`.
3. (Opcional) Ejecutar los scripts `Insert_*.sql` de la misma carpeta para poblar datos de prueba.

### Paso 2: Crear el archivo `.env`
En la raíz del proyecto (`Gestion_Escolar/`), crear o configurar el archivo `.env` con las credenciales de tu servidor MySQL:

```dotenv
db=gestion_escolar
host=localhost
port=3306
user=root
password=tu_contraseña_aqui
```

> [!NOTE]
> El archivo `.env` se encuentra protegido por `.gitignore` para no exponer contraseñas en el repositorio público.

---

## 6. Ejecución del Sistema

Para iniciar el sistema, ejecutar desde la raíz del proyecto:

```powershell
python app.py
```
