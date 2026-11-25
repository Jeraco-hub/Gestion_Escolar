# INFORME TÉCNICO DE ARQUITECTURA Y DISEÑO
## Sistema de Gestión Escolar - Programación Orientada a Objetos (POO)

---

**Asignatura:** Programación Orientada a Objetos  
**Docente:** Erick Bailey  
**Integrantes:** Darío Candia, Miguel Nahuel  
**Proyecto:** Sistema de Gestión Escolar  
**Tecnologías:** Python 3.11+, Peewee ORM, PyMySQL, MySQL Server, Python-Decouple, PrettyTable, bcrypt, MaskPass  
**Fecha:** Octubre 2026  

---

## 1. Introducción y Objetivos del Proyecto

El presente proyecto consiste en el diseño e implementación de un **Sistema de Gestión Escolar**, desarrollado bajo los principios de la **Programación Orientada a Objetos (POO)** y una **arquitectura modular de software en capas**.

### Objetivos Principales:
1. **Modularización rigurosa:** Separar de manera estricta las responsabilidades de la aplicación en capas de **Presentación**, **Negocio** y **Datos**.
2. **Mapeo Objeto-Relacional (ORM):** Reemplazar la manipulación manual de cadenas SQL por objetos y clases de Python mediante **Peewee ORM**, garantizando tipado, integridad y mantenibilidad.
3. **Patrón Repositorio:** Centralizar el acceso y manipulación de datos en módulos especializados para desacoplar la base de datos de la lógica de interfaz.
4. **Seguridad y buenas prácticas:** Gestión de credenciales mediante variables de entorno (`.env`), soporte de borrado lógico (*soft-delete* vía bandera `habilitado`) y control de versiones colaborativo en Git/GitHub.

---

## 2. Fundamentos de POO y Principios de Diseño Aplicados

El proyecto refleja la aplicación directa de los conceptos fundamentales evaluados en la asignatura:

```mermaid
classDiagram
    class ModelBase {
        <<Peewee Model>>
        +Meta database
    }
    class Pais {
        +AutoField id_pais
        +CharField pais
        +CharField nacionalidad
        +CharField iso2
        +CharField iso3
        +IntegerField habilitado
    }
    class Direccion {
        +AutoField id_direccion
        +CharField calle
        +CharField numero
        +CharField comuna
        +CharField ciudad
        +IntegerField habilitado
    }
    class Colegio {
        +AutoField id_colegio
        +CharField nombre
        +CharField telefono
        +IntegerField direccion
        +IntegerField habilitado
    }
    class Usuario {
        +AutoField id_usuario
        +CharField nombre
        +CharField correo
        +CharField contrasena
        +IntegerField colegio
        +IntegerField habilitado
    }
    class PeriodoAcademico {
        +AutoField id_periodo
        +IntegerField ano
        +IntegerField semestre
        +DateField fecha_inicio
        +DateField fecha_fin
        +IntegerField colegio
        +IntegerField habilitado
    }
    class Curso {
        +AutoField id_curso
        +CharField nivel
        +CharField letra
        +IntegerField periodo
        +IntegerField colegio
        +IntegerField habilitado
    }
    class Docente {
        +AutoField id_docente
        +CharField nombre
        +CharField apellido
        +CharField rut
        +CharField especialidad
        +CharField correo
        +IntegerField direccion
        +IntegerField colegio
        +IntegerField habilitado
    }
    class Asignatura {
        +AutoField id_asignatura
        +CharField nombre
        +IntegerField horas_semanales
        +IntegerField docente
        +IntegerField curso
        +IntegerField habilitado
    }
    class Estudiante {
        +AutoField id_estudiante
        +CharField nombre
        +CharField apellido
        +CharField rut
        +CharField matricula
        +DateField fecha_nacimiento
        +CharField correo
        +IntegerField curso
        +IntegerField direccion
        +IntegerField habilitado
    }
    class Evaluacion {
        +AutoField id_evaluacion
        +CharField nombre
        +FloatField ponderacion
        +DateField fecha
        +IntegerField asignatura
        +IntegerField habilitado
    }
    class Calificacion {
        +AutoField id_calificacion
        +IntegerField estudiante
        +IntegerField evaluacion
        +FloatField nota
        +DateField fecha_registro
        +IntegerField habilitado
    }
    class Asistencia {
        +AutoField id_asistencia
        +IntegerField estudiante
        +IntegerField curso
        +DateField fecha
        +IntegerField estado_asistencia
        +IntegerField habilitado
    }
    class EstadoAsistencia {
        +AutoField id_estado_asistencia
        +CharField estado
        +CharField descripcion
        +IntegerField habilitado
    }

    ModelBase <|-- Pais : Herencia
    ModelBase <|-- Direccion : Herencia
    ModelBase <|-- Colegio : Herencia
    ModelBase <|-- Usuario : Herencia
    ModelBase <|-- PeriodoAcademico : Herencia
    ModelBase <|-- Curso : Herencia
    ModelBase <|-- Docente : Herencia
    ModelBase <|-- Asignatura : Herencia
    ModelBase <|-- Estudiante : Herencia
    ModelBase <|-- Evaluacion : Herencia
    ModelBase <|-- Calificacion : Herencia
    ModelBase <|-- Asistencia : Herencia
    ModelBase <|-- EstadoAsistencia : Herencia
```

| Concepto POO | Justificación e Implementación en el Código |
|---|---|
| **Clase y Molde** | Cada entidad del dominio escolar cuenta con su propia clase (ej. `Estudiante`, `Docente`, `Curso`, `Evaluacion`). |
| **Objeto e Instancia** | Las consultas a la base de datos no retornan tuplas anónimas, sino instancias de objetos con propiedades y métodos asociados. |
| **Atributos de Datos** | Cada columna de la tabla relacional se modela como un atributo tipado (`CharField`, `IntegerField`, `DateField`, `FloatField`). |
| **Herencia** | Las 13 clases de datos heredan de `ModelBase`, la cual comparte la conexión activa y la configuración de metadatos de la base de datos. |
| **Encapsulamiento** | La capa de presentación desconoce la estructura de las tablas SQL o los motores de bases de datos; únicamente interactúa con la capa de negocio, que a su vez usa los repositorios. |
| **Abstracción** | Un repositorio abstrae consultas complejas con funciones semánticas como `listado_estudiantes()` o `buscar_por_rut(rut)`. |
| **Seguridad** | El hash bcrypt de contraseñas se calcula en `negocio/`, nunca en la interfaz; las credenciales MySQL se leen de `.env` con `python-decouple`. |
| **Modularidad** | Alta cohesión (cada módulo resuelve una única tarea) y bajo acoplamiento (los módulos dependen de contratos simples y no de implementaciones internas). |

---

## 3. Arquitectura del Software en Tres Capas

La aplicación está organizada siguiendo el patrón arquitectónico clásico de tres capas:

```mermaid
flowchart TD
    subgraph CAPA_PRESENTACION["1. Capa de Presentación (presentacion/)"]
        UI["main.py (Login + menú principal)"]
        MENU["menu.py (Menú interactivo PrettyTable)"]
    end

    subgraph CAPA_NEGOCIO["2. Capa de Negocio (negocio/)"]
        RULES["Reglas, cálculo de promedios, hash bcrypt y formateo"]
    end

    subgraph CAPA_DATOS["3. Capa de Datos (datos/)"]
        REPOS["Repositorios CRUD (repo_*.py / repositorio_pais.py)"]
        MODELS["Modelos Peewee ORM (modelos/*.py)"]
        CONN["conexion.py (.env + Peewee)"]
    end

    subgraph DB["Motor de Base de Datos"]
        MYSQL[(MySQL Server: gestion_escolar)]
    end

    UI --> MENU
    MENU --> RULES
    RULES --> REPOS
    REPOS --> MODELS
    MODELS --> CONN
    CONN --> MYSQL
```

### Descripción de Componentes:
- **`main.py`:** Punto de arranque del programa. Solicita el inicio de sesión (`iniciar_sesion()`) y, si es correcto, invoca al menú principal.
- **`auxiliares/`:** Módulo transversal que contiene variables globales (`nombre_app`, `version_app`) y constantes como `defecto = "DEFAULT 1"`.
- **`presentacion/`:** Interfaz de usuario por consola. Construye tablas legibles mediante `PrettyTable` y recopila entradas del usuario.
- **`negocio/`:** Alberga las reglas de negocio, validaciones y transformaciones lógicas antes de persistir o presentar.
- **`datos/conexion.py`:** Centraliza la conexión hacia MySQL usando `python-decouple` para no quemar contraseñas en el código fuente.
- **`datos/modelos/`:** Un archivo por cada tabla relacional con su mapeo ORM.
- **`datos/repositorio/`:** Funciones de persistencia agrupadas por entidad (`listado_`, `obtener_`, `registrar_`, `actualizar_`, `eliminar_`).
- **`datos/sql/`:** Scripts DDL y DML para recrear y poblar la base de datos desde cero en cualquier equipo. El DDL canónico es `01_crear_tablas.sql`; el script fechado se conserva como histórico de la Evaluación 2.

---

## 4. Modelo de Datos y Entidades Escolares

El sistema abarca **13 tablas**, diseñadas para satisfacer todas las necesidades operativas de una institución educativa. `Paises` es un catálogo independiente (no tiene claves foráneas) y el resto se relaciona según el modelo siguiente:

```mermaid
erDiagram
    DIRECCIONES ||--o{ COLEGIOS : "ubica a"
    DIRECCIONES ||--o{ DOCENTES : "domicilio"
    DIRECCIONES ||--o{ ESTUDIANTES : "domicilio"
    COLEGIOS ||--o{ USUARIOS : "pertenece"
    COLEGIOS ||--o{ PERIODOS_ACADEMICOS : "organiza"
    COLEGIOS ||--o{ DOCENTES : "emplea"
    COLEGIOS ||--o{ CURSOS : "imparte"
    PERIODOS_ACADEMICOS ||--o{ CURSOS : "define vigencia"
    DOCENTES ||--o{ ASIGNATURAS : "dicta"
    CURSOS ||--o{ ASIGNATURAS : "contiene"
    CURSOS ||--o{ ESTUDIANTES : "matricula"
    ASIGNATURAS ||--o{ EVALUACIONES : "programa"
    ESTUDIANTES ||--o{ CALIFICACIONES : "obtiene"
    EVALUACIONES ||--o{ CALIFICACIONES : "evalua"
    ESTUDIANTES ||--o{ ASISTENCIAS : "registra"
    CURSOS ||--o{ ASISTENCIAS : "en el contexto de"
    ESTADOS_ASISTENCIA ||--o{ ASISTENCIAS : "clasifica"
```

### Diccionario de Módulos Implementados:

1. **`Pais` (`paises`):** Catálogo de países con nacionalidad y códigos ISO 2 / ISO 3.
2. **`Direccion` (`direcciones`):** Almacena calle, número, comuna y ciudad. Base compartida por personas y colegios.
3. **`Colegio` (`colegios`):** Entidad educativa central con teléfono y dirección.
4. **`Usuario` (`usuarios`):** Acceso administrativo con nombre, correo único y contraseña con hash bcrypt.
5. **`PeriodoAcademico` (`periodos_academicos`):** Define el año y semestre escolar con fechas de inicio y fin.
6. **`Curso` (`cursos`):** Nivel (ej: "3° Medio") y letra ("A", "B"), vinculado a su colegio y periodo.
7. **`Docente` (`docentes`):** Profesores del establecimiento con RUT único, correo, especialidad y dirección.
8. **`Asignatura` (`asignaturas`):** Materias lectivas (ej: "Matemáticas"), con carga horaria semanal y docente asignado.
9. **`Estudiante` (`estudiantes`):** Alumnos con matrícula única, RUT, fecha de nacimiento, contacto y curso.
10. **`Evaluacion` (`evaluaciones`):** Certámenes o exámenes con fecha y porcentaje de ponderación.
11. **`Calificacion` (`calificaciones`):** Notas numéricas (float) asignadas a un estudiante por cada evaluación con fecha y observación.
12. **`Asistencia` (`asistencias`):** Registro de asistencia diaria de un estudiante en un curso, con justificación opcional.
13. **`EstadoAsistencia` (`estados_asistencia`):** Catálogo de estados (Presente, Ausente, Justificado) usado por `Asistencia`.

---

## 5. Implementación del Patrón Repositorio y CRUD

Cada entidad cuenta con un repositorio homólogo en `datos/repositorio/` que ofrece operaciones atómicas estandarizadas:

```python
# Ejemplo: repo_estudiante.py

def listado_estudiantes():
    estudiantes = Estudiante.select().where(Estudiante.habilitado == 1)
    return list(estudiantes)

def guardar_estudiante(estudiante: Estudiante):
    return estudiante.save()

def registrar_estudiante(nombre, apellido, rut, matricula, ...):
    nuevo = Estudiante(
        nombre=nombre,
        apellido=apellido,
        rut=rut,
        matricula=matricula,
        ...
        habilitado=1
    )
    guardar_estudiante(nuevo)
    return nuevo

def eliminar_estudiante(id_estudiante):
    # Borrado lógico (Soft-delete) para mantener trazabilidad histórica
    consulta = Estudiante.update(habilitado=0).where(Estudiante.id_estudiante == id_estudiante)
    consulta.execute()
```

### Características Técnicas del Repositorio:
- **Borrado Lógico (*Soft Delete*):** La eliminación no destruye el registro físico con `DELETE FROM`, sino que actualiza `habilitado = 0`, preservando la integridad referencial de calificaciones y asistencias pasadas.
- **Consultas Filtradas:** Los listados filtran por defecto los registros habilitados (`where(Entidad.habilitado == 1)`).
- **Mapeo Directo a Instancias:** Las funciones devuelven objetos Peewee que pueden ser consultados o pasados a la capa de presentación.

---

## 6. Configuración, Despliegue y Pruebas

### Requisitos Previos:
- Python 3.11 / 3.12 instalado.
- Servidor MySQL activo en `localhost:3306`.

### Pasos de Instalación:

1. **Instalación de paquetes:**
   ```powershell
   python -m pip install -r requirements.txt
   ```

2. **Carga de Base de Datos:**
   Crear la base `gestion_escolar` y ejecutar en MySQL Workbench el DDL canónico:
   `datos/sql/01_crear_tablas.sql`
   (opcional: `datos/sql/02_datos_prueba.sql` para cargar datos de ejemplo y el usuario `admin@colegio.cl`).

3. **Configuración de Variables de Entorno (`.env`):**
   Copiar `.env.example` como `.env` y completar:
   ```dotenv
   db=gestion_escolar
   host=localhost
   port=3306
   user=root
   password=tu_contraseña
   ```

4. **Ejecución:**
   ```powershell
   python main.py
   ```

---

## 7. Conclusión

El proyecto **Gestión Escolar** cumple a cabalidad con los estándares exigidos por la cátedra de Programación Orientada a Objetos:
- Implementación real y funcional del **ORM Peewee** sobre MySQL.
- **Separación de responsabilidades** limpia entre datos, lógica y presentación.
- Código legible, mantenible y sin dependencias superfluas.
- Repositorio en GitHub ordenado con historial de commits descriptivo y control de ramas limpio.

