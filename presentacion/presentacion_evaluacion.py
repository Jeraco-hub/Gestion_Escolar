from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero, pedir_fecha, pedir_ponderacion
from negocio.negocio_evaluacion import (
    procesar_listado_evaluaciones,
    evaluacion_por_id,
    registrar_nueva_evaluacion,
    modificar_datos_evaluacion,
    deshabilitar_evaluacion
)


def mostrar_listado_evaluaciones():
    try:
        tabla = procesar_listado_evaluaciones(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay evaluaciones registradas o habilitadas.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_evaluacion():
    print('\n--- Registrar Nueva Evaluación ---')
    nombre = pedir_texto('Ingrese Nombre (ej: Prueba 1): ', 100)
    ponderacion = pedir_ponderacion('Ingrese ponderación en % (1 a 100): ')
    fecha = pedir_fecha('Ingrese fecha (DD-MM-AAAA): ')
    asignatura = pedir_entero('Ingrese ID de la asignatura: ')

    registrar_nueva_evaluacion(nombre, ponderacion, fecha, asignatura)


def modificar_evaluacion():
    print('\n--- Modificar Evaluación ---')
    mostrar_listado_evaluaciones()
    id_evaluacion = pedir_entero('Ingrese ID de la evaluación a modificar: ')
    evaluacion = evaluacion_por_id(id_evaluacion)
    if evaluacion and evaluacion.habilitado == 1:
        print(f'\nEvaluación encontrada: {evaluacion.nombre}')
        nombre = pedir_texto(f'Nuevo nombre [{evaluacion.nombre}] (ENTER para conservar): ', 100, opcional=True) or evaluacion.nombre
        ponderacion = pedir_ponderacion(f'Nueva ponderación [{evaluacion.ponderacion}] (ENTER para conservar): ', opcional=True) or evaluacion.ponderacion
        fecha = pedir_fecha(f'Nueva fecha [{evaluacion.fecha}] DD-MM-AAAA (ENTER para conservar): ', opcional=True) or evaluacion.fecha
        asignatura = pedir_entero(f'Nuevo ID de asignatura [{evaluacion.asignatura}] (ENTER para conservar): ', opcional=True) or evaluacion.asignatura

        modificar_datos_evaluacion(evaluacion, nombre, ponderacion, fecha, asignatura)
    else:
        print('Evaluación no encontrada o inactiva.')


def eliminar_evaluacion():
    print('\n--- Eliminar Evaluación ---')
    mostrar_listado_evaluaciones()
    id_evaluacion = pedir_entero('Ingrese ID de la evaluación a eliminar: ')
    evaluacion = evaluacion_por_id(id_evaluacion)
    if evaluacion and evaluacion.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja la evaluación {evaluacion.nombre}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_evaluacion(evaluacion.id_evaluacion)
    else:
        print('Evaluación no encontrada.')