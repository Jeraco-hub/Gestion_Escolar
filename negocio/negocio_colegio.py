from prettytable import PrettyTable
from datos.repositorio.repo_colegio import (
    listado_colegios,
    obtener_colegio,
    buscar_colegio,
    registrar_colegio,
    actualizar_colegio,
    eliminar_colegio
)
from auxiliares import mensaje_error


def procesar_listado_colegios(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Nombre', 'Teléfono', 'Dirección']
    colegios = listado_colegios()
    if not colegios:
        return None
    for c in colegios:
        tabla.add_row([c.id_colegio, c.nombre, c.telefono or 'N/A', c.direccion or 'N/A'])
    return tabla


def colegio_por_id(id_colegio: int):
    try:
        return obtener_colegio(id_colegio)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_nuevo_colegio(nombre, telefono, direccion):
    try:
        existente = buscar_colegio(nombre)
        if existente:
            if existente.habilitado == 1:
                print('Ya existe un colegio activo con ese nombre.')
            else:
                print('Ya existe un colegio deshabilitado con ese nombre.')
            return None
        nuevo = registrar_colegio(nombre, telefono, direccion)
        if nuevo:
            print(f'Colegio {nombre} registrado con éxito.')
            return nuevo
        print('No se pudo registrar el colegio.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_colegio(colegio_obj, nombre, telefono, direccion):
    try:
        otro = buscar_colegio(nombre)
        if otro and otro.id_colegio != colegio_obj.id_colegio:
            print('Ya existe otro colegio con ese nombre.')
            return
        actualizar_colegio(colegio_obj.id_colegio, nombre, telefono, direccion)
        print('Datos del colegio actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_colegio(id_colegio: int):
    try:
        eliminar_colegio(id_colegio)
        print('Colegio deshabilitado con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')