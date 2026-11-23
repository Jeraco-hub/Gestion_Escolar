from prettytable import PrettyTable
from datos.repositorio.repo_evaluacion import (
    listado_evaluaciones,
    obtener_evaluacion,
    evaluaciones_por_asignatura,
    registrar_evaluacion,
    actualizar_evaluacion,
    eliminar_evaluacion
)
from datos.repositorio.repo_asignatura import obtener_asignatura
from auxiliares import mensaje_error


def _nombre_asignatura(id_asignatura):
    asignatura = obtener_asignatura(id_asignatura)
    if not asignatura:
        return f'ID {id_asignatura}'
    return asignatura.nombre


def procesar_listado_evaluaciones(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Nombre', 'Ponderación (%)', 'Fecha', 'Asignatura']
    evaluaciones = listado_evaluaciones()
    if not evaluaciones:
        return None
    for e in evaluaciones:
        tabla.add_row([
            e.id_evaluacion,
            e.nombre,
            e.ponderacion,
            e.fecha,
            _nombre_asignatura(e.asignatura)
        ])
    return tabla


def evaluacion_por_id(id_evaluacion: int):
    try:
        return obtener_evaluacion(id_evaluacion)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def _asignatura_valida(id_asignatura):
    asignatura = obtener_asignatura(id_asignatura)
    if not asignatura or asignatura.habilitado != 1:
        print('La asignatura indicada no existe o está deshabilitada.')
        return False
    return True


def _nombre_repetido(nombre, asignatura, id_actual=None):
    for e in evaluaciones_por_asignatura(asignatura):
        if e.habilitado == 1 and e.nombre.lower() == nombre.lower() and e.id_evaluacion != id_actual:
            return True
    return False


def registrar_nueva_evaluacion(nombre, ponderacion, fecha, asignatura):
    try:
        if not _asignatura_valida(asignatura):
            return None
        if _nombre_repetido(nombre, asignatura):
            print('Ya existe una evaluación con ese nombre en esa asignatura.')
            return None
        nueva = registrar_evaluacion(nombre, ponderacion, fecha, asignatura)
        if nueva:
            print(f'Evaluación {nombre} registrada con éxito.')
            return nueva
        print('No se pudo registrar la evaluación.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_evaluacion(evaluacion, nombre, ponderacion, fecha, asignatura):
    try:
        if not _asignatura_valida(asignatura):
            return
        if _nombre_repetido(nombre, asignatura, evaluacion.id_evaluacion):
            print('Ya existe otra evaluación con ese nombre en esa asignatura.')
            return
        actualizar_evaluacion(evaluacion.id_evaluacion, nombre, ponderacion, fecha, asignatura)
        print('Datos de la evaluación actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_evaluacion(id_evaluacion: int):
    try:
        eliminar_evaluacion(id_evaluacion)
        print('Evaluación deshabilitada con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')