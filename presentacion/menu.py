from auxiliares import (
    nombre_app,
    version_app,
    mensaje_error_opcion,
    menu_principal, diccionario_menu_principal,
    menu_estudiantes, diccionario_menu_estudiantes,
    menu_configuracion, diccionario_menu_configuracion
)
from presentacion.presentacion_estudiante import (
    mostrar_listado_estudiantes,
    crear_estudiante,
    modificar_estudiante,
    eliminar_estudiante
)

def mostrar_menu(titulo, opciones):
    print(titulo)
    print(f'{"=" * len(titulo)}\n')
    for clave, valor in opciones.items():
        print(f'[{clave}] - {valor}')

def cargar_menu_estudiantes():
    while True:
        mostrar_menu(menu_estudiantes, diccionario_menu_estudiantes)
        opcion = input('Seleccione su opción: ')
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

def cargar_menu_configuracion():
    while True:
        mostrar_menu(menu_configuracion, diccionario_menu_configuracion)
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                print(f'{nombre_app} - Versión activa: {version_app}\n')
            case '2':
                print('Acceso a listado de direcciones...\n')
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
        opcion = input('Seleccione su opción: ')
        print()

        match opcion:
            case '1':
                cargar_menu_estudiantes()
            case '2':
                print('Módulo en construcción: Gestión de Docentes.\n')
            case '3':
                print('Módulo en construcción: Cursos y Asignaturas.\n')
            case '4':
                print('Módulo en construcción: Calificaciones.\n')
            case '5':
                cargar_menu_configuracion()
            case '0':
                print('Cerrando el sistema...\n')
                break
            case _:
                print(mensaje_error_opcion)