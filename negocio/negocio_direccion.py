from prettytable import PrettyTable
from datos.repositorios.repo_direccion import (
    listado_direcciones,
    obtener_direccion,
    buscar_direccion,
    registrar_direccion,
    actualizar_direccion,
    eliminar_direccion
)
from auxiliares import mensaje_error


def procesar_listado_direcciones(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Calle', 'Número', 'Comuna', 'Ciudad']
    direcciones = listado_direcciones()
    if not direcciones:
        return None
    for d in direcciones:
        tabla.add_row([d.id_direccion, d.calle, d.numero, d.comuna, d.ciudad])
    return tabla


def direccion_por_id(id_direccion: int):
    try:
        return obtener_direccion(id_direccion)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_nueva_direccion(calle, numero, comuna, ciudad):
    try:
        existente = buscar_direccion(calle, numero, comuna)
        if existente:
            if existente.habilitado == 1:
                print('Ya existe una dirección activa con esos datos.')
            else:
                print('Ya existe una dirección deshabilitada con esos datos.')
            return None
        nueva = registrar_direccion(calle, numero, comuna, ciudad)
        if nueva:
            print(f'Dirección {calle} {numero}, {comuna} registrada con éxito.')
            return nueva
        print('No se pudo registrar la dirección.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_direccion(direccion_obj, calle, numero, comuna, ciudad):
    try:
        otra = buscar_direccion(calle, numero, comuna)
        if otra and otra.id_direccion != direccion_obj.id_direccion:
            print('Ya existe otra dirección con esos datos.')
            return
        actualizar_direccion(direccion_obj.id_direccion, calle, numero, comuna, ciudad)
        print('Datos de la dirección actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_direccion(id_direccion: int):
    try:
        eliminar_direccion(id_direccion)
        print('Dirección deshabilitada con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')