from prettytable import PrettyTable
from datos.repositorios.repo_asistencia import (
    listado_asistencias,
    obtener_asistencia,
    buscar_asistencia,
    asistencias_por_estudiante,
    asistencias_por_curso,
    registrar_asistencia,
    actualizar_asistencia,
    eliminar_asistencia
)
from auxiliares import mensaje_error


def procesar_listado_asistencias(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Estudiante', 'Curso', 'Fecha', 'Estado', 'Justificación']
    asistencias = listado_asistencias()
    if not asistencias:
        return None
    for a in asistencias:
        tabla.add_row([
            a.id_asistencia,
            a.estudiante,
            a.curso,
            a.fecha,
            a.estado_asistencia,
            a.justificacion or 'N/A'
        ])
    return tabla


def procesar_asistencias_estudiante(tabla: PrettyTable, id_estudiante):
    tabla.field_names = ['ID', 'Curso', 'Fecha', 'Estado', 'Justificación']
    asistencias = asistencias_por_estudiante(id_estudiante)
    if not asistencias:
        return None
    for a in asistencias:
        tabla.add_row([
            a.id_asistencia,
            a.curso,
            a.fecha,
            a.estado_asistencia,
            a.justificacion or 'N/A'
        ])
    return tabla


def procesar_asistencias_curso(tabla: PrettyTable, id_curso, fecha):
    tabla.field_names = ['ID', 'Estudiante', 'Fecha', 'Estado', 'Justificación']
    asistencias = asistencias_por_curso(id_curso, fecha)
    if not asistencias:
        return None
    for a in asistencias:
        tabla.add_row([
            a.id_asistencia,
            a.estudiante,
            a.fecha,
            a.estado_asistencia,
            a.justificacion or 'N/A'
        ])
    return tabla


def asistencia_por_id(id_asistencia: int):
    try:
        return obtener_asistencia(id_asistencia)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_nueva_asistencia(estudiante, curso, fecha, estado_asistencia, justificacion):
    try:
        existente = buscar_asistencia(estudiante, curso, fecha)
        if existente:
            if existente.habilitado == 1:
                print('Ya existe una asistencia activa para ese estudiante, curso y fecha.')
            else:
                print('Ya existe una asistencia deshabilitada para ese estudiante, curso y fecha.')
            return None
        nueva = registrar_asistencia(estudiante, curso, fecha, estado_asistencia, justificacion)
        if nueva:
            print(f'Asistencia del estudiante {estudiante} registrada con éxito.')
            return nueva
        print('No se pudo registrar la asistencia.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_asistencia(asistencia_obj, estudiante, curso, fecha, estado_asistencia, justificacion):
    try:
        otra = buscar_asistencia(estudiante, curso, fecha)
        if otra and otra.id_asistencia != asistencia_obj.id_asistencia:
            print('Ya existe otra asistencia con ese estudiante, curso y fecha.')
            return
        actualizar_asistencia(asistencia_obj.id_asistencia, estudiante, curso, fecha, estado_asistencia, justificacion)
        print('Datos de la asistencia actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_asistencia(id_asistencia: int):
    try:
        eliminar_asistencia(id_asistencia)
        print('Asistencia deshabilitada con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')