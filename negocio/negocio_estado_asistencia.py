from prettytable import PrettyTable
from datos.repositorios.repo_estado_asistencia import (
    listado_estados_asistencia,
    obtener_estado_asistencia,
    buscar_estado_asistencia,
    registrar_estado_asistencia,
    actualizar_estado_asistencia,
    eliminar_estado_asistencia
)
from auxiliares import mensaje_error


def procesar_listado_estados(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Estado', 'Descripción']
    estados = listado_estados_asistencia()
    if not estados:
        return None
    for e in estados:
        tabla.add_row([e.id_estado_asistencia, e.estado, e.descripcion or 'N/A'])
    return tabla


def estado_por_id(id_estado: int):
    try:
        return obtener_estado_asistencia(id_estado)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_nuevo_estado(estado, descripcion):
    try:
        existente = buscar_estado_asistencia(estado)
        if existente:
            if existente.habilitado == 1:
                print('Ya existe un estado activo con ese nombre.')
            else:
                print('Ya existe un estado deshabilitado con ese nombre.')
            return None
        nuevo = registrar_estado_asistencia(estado, descripcion)
        if nuevo:
            print(f'Estado {estado} registrado con éxito.')
            return nuevo
        print('No se pudo registrar el estado.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_estado(estado_obj, estado, descripcion):
    try:
        otro = buscar_estado_asistencia(estado)
        if otro and otro.id_estado_asistencia != estado_obj.id_estado_asistencia:
            print('Ya existe otro estado con ese nombre.')
            return
        actualizar_estado_asistencia(estado_obj.id_estado_asistencia, estado, descripcion)
        print('Datos del estado actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_estado(id_estado: int):
    try:
        eliminar_estado_asistencia(id_estado)
        print('Estado deshabilitado con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')