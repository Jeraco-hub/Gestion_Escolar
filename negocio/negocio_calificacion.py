from datetime import date
from prettytable import PrettyTable
from datos.repositorios.repo_calificacion import (
    listado_calificaciones,
    obtener_calificacion,
    calificaciones_por_estudiante,
    registrar_calificacion,
    actualizar_calificacion,
    eliminar_calificacion
)
from datos.repositorios.repo_estudiante import obtener_estudiante
from datos.repositorios.repo_evaluacion import obtener_evaluacion
from auxiliares import mensaje_error


def _nombre_estudiante(id_estudiante):
    estudiante = obtener_estudiante(id_estudiante)
    if not estudiante:
        return f'ID {id_estudiante}'
    return f'{estudiante.nombre} {estudiante.apellido}'


def _nombre_evaluacion(id_evaluacion):
    evaluacion = obtener_evaluacion(id_evaluacion)
    if not evaluacion:
        return f'ID {id_evaluacion}'
    return evaluacion.nombre


def procesar_listado_calificaciones(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Estudiante', 'Evaluación', 'Nota', 'Fecha', 'Observación']
    calificaciones = listado_calificaciones()
    if not calificaciones:
        return None
    for c in calificaciones:
        tabla.add_row([
            c.id_calificacion,
            _nombre_estudiante(c.estudiante),
            _nombre_evaluacion(c.evaluacion),
            c.nota,
            c.fecha_registro,
            c.observacion if c.observacion else '-'
        ])
    return tabla


def procesar_calificaciones_estudiante(tabla: PrettyTable, id_estudiante: int):
    tabla.field_names = ['ID', 'Evaluación', 'Nota', 'Fecha', 'Observación']
    calificaciones = calificaciones_por_estudiante(id_estudiante)
    if not calificaciones:
        return None, None
    for c in calificaciones:
        tabla.add_row([
            c.id_calificacion,
            _nombre_evaluacion(c.evaluacion),
            c.nota,
            c.fecha_registro,
            c.observacion if c.observacion else '-'
        ])
    promedio = round(sum(c.nota for c in calificaciones) / len(calificaciones), 1)
    return tabla, promedio

def calificacion_por_id(id_calificacion: int):
    try:
        return obtener_calificacion(id_calificacion)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def estudiante_valido(id_estudiante: int):
    estudiante = obtener_estudiante(id_estudiante)
    if not estudiante or estudiante.habilitado != 1:
        print('El estudiante indicado no existe o está deshabilitado.')
        return None
    return estudiante


def _validar_referencias(estudiante, evaluacion):
    if not estudiante_valido(estudiante):
        return False
    evaluacion_obj = obtener_evaluacion(evaluacion)
    if not evaluacion_obj or evaluacion_obj.habilitado != 1:
        print('La evaluación indicada no existe o está deshabilitada.')
        return False
    return True


def registrar_nueva_calificacion(estudiante, evaluacion, nota, observacion):
    try:
        if not _validar_referencias(estudiante, evaluacion):
            return None

        for c in calificaciones_por_estudiante(estudiante):
            if c.evaluacion == evaluacion:
                print('Ese estudiante ya tiene una nota en esa evaluación. Use la opción Modificar.')
                return None

        nueva = registrar_calificacion(estudiante, evaluacion, nota, date.today(), observacion or None)
        if nueva:
            print(f'Calificación {nota} registrada con éxito.')
            return nueva
        print('No se pudo registrar la calificación.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_calificacion(calificacion, nota, observacion):
    try:
        actualizar_calificacion(
            calificacion.id_calificacion,
            calificacion.estudiante,
            calificacion.evaluacion,
            nota,
            calificacion.fecha_registro,
            observacion or None
        )
        print('Calificación actualizada correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_calificacion(id_calificacion: int):
    try:
        eliminar_calificacion(id_calificacion)
        print('Calificación deshabilitada con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')