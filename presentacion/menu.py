from auxiliares import (
    nombre_app,
    version_app,
    mensaje_error_opcion,
    menu_principal, diccionario_menu_principal,
    menu_estudiantes, diccionario_menu_estudiantes,
    menu_cursos_asignaturas, diccionario_menu_cursos_asignaturas,
    menu_calificaciones, diccionario_menu_calificaciones,
    menu_docentes, diccionario_menu_docentes,
    menu_usuarios, diccionario_menu_usuarios,
    menu_configuracion, diccionario_menu_configuracion,
    menu_pais, diccionario_menu_pais,
    menu_estado_asistencia, diccionario_menu_estado_asistencia,
    menu_direccion, diccionario_menu_direccion,
    menu_colegio, diccionario_menu_colegio,
    menu_periodo, diccionario_menu_periodo
)
from presentacion.presentacion_estudiante import (
    mostrar_listado_estudiantes,
    crear_estudiante,
    modificar_estudiante,
    eliminar_estudiante
)
from presentacion.presentacion_curso import (
    mostrar_listado_cursos,
    crear_curso,
    modificar_curso,
    eliminar_curso
)
from presentacion.presentacion_asignatura import (
    mostrar_listado_asignaturas,
    crear_asignatura,
    modificar_asignatura,
    eliminar_asignatura
)
from presentacion.presentacion_calificacion import (
    mostrar_listado_calificaciones,
    mostrar_calificaciones_estudiante,
    crear_calificacion,
    modificar_calificacion,
    eliminar_calificacion
)
from presentacion.presentacion_evaluacion import (
    mostrar_listado_evaluaciones,
    crear_evaluacion,
    modificar_evaluacion,
    eliminar_evaluacion
)
from presentacion.presentacion_asistencia import (
    mostrar_listado_asistencias,
    mostrar_asistencias_estudiante,
    mostrar_asistencias_curso,
    crear_asistencia,
    modificar_asistencia,
    eliminar_asistencia
)
from presentacion.presentacion_periodo_academico import (
    mostrar_listado_periodos,
    crear_periodo,
    modificar_periodo,
    eliminar_periodo
)
from presentacion.presentacion_colegio import (
    mostrar_listado_colegios,
    crear_colegio,
    modificar_colegio,
    eliminar_colegio
)
from presentacion.presentacion_direccion import (
    mostrar_listado_direcciones,
    crear_direccion,
    modificar_direccion,
    eliminar_direccion
)
from presentacion.presentacion_estado_asistencia import (
    mostrar_listado_estados,
    crear_estado,
    modificar_estado,
    eliminar_estado
)
from presentacion.presentacion_pais import (
    mostrar_listado_paises,
    crear_pais,
    modificar_pais,
    eliminar_pais
)
from presentacion.presentacion_docente import (
    mostrar_listado_docentes,
    crear_docente,
    modificar_docente,
    eliminar_docente
)
from presentacion.presentacion_usuario import (
    mostrar_listado_usuarios,
    crear_usuario,
    modificar_usuario,
    eliminar_usuario
)

PROMPT_OPCION = 'Seleccione su opción: '

def mostrar_menu(titulo, opciones):
    print(titulo)
    print(f'{"=" * len(titulo)}\n')
    for clave, valor in opciones.items():
        print(f'[{clave}] - {valor}')

def cargar_menu_estudiantes():
    while True:
        mostrar_menu(menu_estudiantes, diccionario_menu_estudiantes)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_estudiantes()
            case '2':
                crear_estudiante()
            case '3':
                modificar_estudiante()
            case '4':
                eliminar_estudiante()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_usuarios():
    while True:
        mostrar_menu(menu_usuarios, diccionario_menu_usuarios)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_usuarios()
            case '2':
                crear_usuario()
            case '3':
                modificar_usuario()
            case '4':
                eliminar_usuario()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_docentes():
    while True:
        mostrar_menu(menu_docentes, diccionario_menu_docentes)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_docentes()
            case '2':
                crear_docente()
            case '3':
                modificar_docente()
            case '4':
                eliminar_docente()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_cursos_asignaturas():
    while True:
        mostrar_menu(menu_cursos_asignaturas, diccionario_menu_cursos_asignaturas)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_cursos()
            case '2':
                crear_curso()
            case '3':
                modificar_curso()
            case '4':
                eliminar_curso()
            case '5':
                mostrar_listado_asignaturas()
            case '6':
                crear_asignatura()
            case '7':
                modificar_asignatura()
            case '8':
                eliminar_asignatura()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_calificaciones():
    while True:
        mostrar_menu(menu_calificaciones, diccionario_menu_calificaciones)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_calificaciones()
            case '2':
                mostrar_calificaciones_estudiante()
            case '3':
                crear_calificacion()
            case '4':
                modificar_calificacion()
            case '5':
                eliminar_calificacion()
            case '6':
                mostrar_listado_evaluaciones()
            case '7':
                crear_evaluacion()
            case '8':
                modificar_evaluacion()
            case '9':
                eliminar_evaluacion()
            case '10':
                mostrar_listado_asistencias()
            case '11':
                mostrar_asistencias_estudiante()
            case '12':
                mostrar_asistencias_curso()
            case '13':
                crear_asistencia()
            case '14':
                modificar_asistencia()
            case '15':
                eliminar_asistencia()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_pais():
    while True:
        mostrar_menu(menu_pais, diccionario_menu_pais)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_paises()
            case '2':
                crear_pais()
            case '3':
                modificar_pais()
            case '4':
                eliminar_pais()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_estado_asistencia():
    while True:
        mostrar_menu(menu_estado_asistencia, diccionario_menu_estado_asistencia)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_estados()
            case '2':
                crear_estado()
            case '3':
                modificar_estado()
            case '4':
                eliminar_estado()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_direccion():
    while True:
        mostrar_menu(menu_direccion, diccionario_menu_direccion)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_direcciones()
            case '2':
                crear_direccion()
            case '3':
                modificar_direccion()
            case '4':
                eliminar_direccion()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_colegio():
    while True:
        mostrar_menu(menu_colegio, diccionario_menu_colegio)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_colegios()
            case '2':
                crear_colegio()
            case '3':
                modificar_colegio()
            case '4':
                eliminar_colegio()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_periodo():
    while True:
        mostrar_menu(menu_periodo, diccionario_menu_periodo)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                mostrar_listado_periodos()
            case '2':
                crear_periodo()
            case '3':
                modificar_periodo()
            case '4':
                eliminar_periodo()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu_configuracion():
    while True:
        mostrar_menu(menu_configuracion, diccionario_menu_configuracion)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                print(f'{nombre_app} - Versión activa: {version_app}\n')
            case '2':
                cargar_menu_pais()
            case '3':
                cargar_menu_estado_asistencia()
            case '4':
                cargar_menu_direccion()
            case '5':
                cargar_menu_colegio()
            case '6':
                cargar_menu_periodo()
            case '0':
                print('Volviendo al Menú Principal...\n')
                break
            case _:
                print(mensaje_error_opcion)

def cargar_menu():
    print(f'\n{nombre_app} - {version_app}')
    print(f'{"=" * (len(nombre_app) + len(version_app) + 3)}\n')

    while True:
        mostrar_menu(menu_principal, diccionario_menu_principal)
        opcion = input(PROMPT_OPCION)
        print()

        match opcion:
            case '1':
                cargar_menu_estudiantes()
            case '2':
                cargar_menu_docentes()
            case '3':
                cargar_menu_cursos_asignaturas()
            case '4':
                cargar_menu_calificaciones()
            case '5':
                cargar_menu_configuracion()
            case '6':
                cargar_menu_usuarios()
            case '0':
                print('Cerrando el sistema...\n')
                break
            case _:
                print(mensaje_error_opcion)