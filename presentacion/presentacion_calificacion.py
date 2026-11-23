from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero, pedir_nota
from negocio.negocio_calificacion import (
    procesar_listado_calificaciones,
    procesar_calificaciones_estudiante,
    calificacion_por_id,
    estudiante_valido,
    registrar_nueva_calificacion,
    modificar_datos_calificacion,
    deshabilitar_calificacion
)


def mostrar_listado_calificaciones():
    try:
        tabla = procesar_listado_calificaciones(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay calificaciones registradas o habilitadas.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def mostrar_calificaciones_estudiante():
    print('\n--- Calificaciones por Estudiante ---')
    id_estudiante = pedir_entero('Ingrese ID del estudiante: ')
    try:
        estudiante = estudiante_valido(id_estudiante)
        if not estudiante:
            return
        tabla, promedio = procesar_calificaciones_estudiante(PrettyTable(), id_estudiante)
        if tabla:
            print(f'\nEstudiante: {estudiante.nombre} {estudiante.apellido}')
            print(tabla)
            print(f'Promedio: {promedio}')
        else:
            print('Este estudiante no tiene calificaciones registradas.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_calificacion():
    print('\n--- Registrar Nueva Calificación ---')
    estudiante = pedir_entero('Ingrese ID del estudiante: ')
    evaluacion = pedir_entero('Ingrese ID de la evaluación: ')
    nota = pedir_nota('Ingrese la nota (1.0 a 7.0): ')
    observacion = pedir_texto('Ingrese observación (opcional): ', 255, opcional=True)

    registrar_nueva_calificacion(estudiante, evaluacion, nota, observacion)

def modificar_calificacion():
    print('\n--- Modificar Calificación ---')
    mostrar_listado_calificaciones()
    id_calificacion = pedir_entero('Ingrese ID de la calificación a modificar: ')
    calificacion = calificacion_por_id(id_calificacion)
    if calificacion and calificacion.habilitado == 1:
        print(f'\nCalificación encontrada: nota {calificacion.nota}')
        nota = pedir_nota(f'Nueva nota [{calificacion.nota}] (ENTER para conservar): ', opcional=True) or calificacion.nota
        observacion = pedir_texto(f'Nueva observación [{calificacion.observacion or "-"}] (ENTER para conservar): ', 255, opcional=True) or calificacion.observacion

        modificar_datos_calificacion(calificacion, nota, observacion)
    else:
        print('Calificación no encontrada o inactiva.')


def eliminar_calificacion():
    print('\n--- Eliminar Calificación ---')
    mostrar_listado_calificaciones()
    id_calificacion = pedir_entero('Ingrese ID de la calificación a eliminar: ')
    calificacion = calificacion_por_id(id_calificacion)
    if calificacion and calificacion.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja la calificación {calificacion.nota}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_calificacion(calificacion.id_calificacion)
    else:
        print('Calificación no encontrada.')