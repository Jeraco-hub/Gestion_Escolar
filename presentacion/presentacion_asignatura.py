from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero
from negocio.negocio_asignatura import (
    procesar_listado_asignaturas,
    asignatura_por_id,
    registrar_nueva_asignatura,
    modificar_datos_asignatura,
    deshabilitar_asignatura
)


def mostrar_listado_asignaturas():
    try:
        tabla = procesar_listado_asignaturas(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay asignaturas registradas o habilitadas.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_asignatura():
    print('\n--- Registrar Nueva Asignatura ---')
    nombre = pedir_texto('Ingrese Nombre: ', 100)
    horas = pedir_entero('Ingrese horas semanales: ')
    docente = pedir_entero('Ingrese ID del docente (opcional): ', opcional=True)
    curso = pedir_entero('Ingrese ID del curso: ')

    registrar_nueva_asignatura(nombre, horas, docente, curso)


def modificar_asignatura():
    print('\n--- Modificar Asignatura ---')
    mostrar_listado_asignaturas()
    id_asignatura = pedir_entero('Ingrese ID de la asignatura a modificar: ')
    asignatura = asignatura_por_id(id_asignatura)
    if asignatura and asignatura.habilitado == 1:
        print(f'\nAsignatura encontrada: {asignatura.nombre}')
        nombre = pedir_texto(f'Nuevo nombre [{asignatura.nombre}] (ENTER para conservar): ', 100, opcional=True) or asignatura.nombre
        horas = pedir_entero(f'Nuevas horas semanales [{asignatura.horas_semanales}] (ENTER para conservar): ', opcional=True) or asignatura.horas_semanales
        docente = pedir_entero(f'Nuevo ID de docente [{asignatura.docente}] (ENTER para conservar): ', opcional=True) or asignatura.docente
        curso = pedir_entero(f'Nuevo ID de curso [{asignatura.curso}] (ENTER para conservar): ', opcional=True) or asignatura.curso

        modificar_datos_asignatura(asignatura, nombre, horas, docente, curso)
    else:
        print('Asignatura no encontrada o inactiva.')


def eliminar_asignatura():
    print('\n--- Eliminar Asignatura ---')
    mostrar_listado_asignaturas()
    id_asignatura = pedir_entero('Ingrese ID de la asignatura a eliminar: ')
    asignatura = asignatura_por_id(id_asignatura)
    if asignatura and asignatura.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja la asignatura {asignatura.nombre}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_asignatura(asignatura.id_asignatura)
    else:
        print('Asignatura no encontrada.')