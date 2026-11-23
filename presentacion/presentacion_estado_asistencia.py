from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero
from negocio.negocio_estado_asistencia import (
    procesar_listado_estados,
    estado_por_id,
    registrar_nuevo_estado,
    modificar_datos_estado,
    deshabilitar_estado
)


def mostrar_listado_estados():
    try:
        tabla = procesar_listado_estados(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay estados de asistencia registrados.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_estado():
    print('\n--- Registrar Nuevo Estado de Asistencia ---')
    estado = pedir_texto('Ingrese Estado (ej: Presente): ', 50)
    descripcion = pedir_texto('Ingrese Descripción (opcional): ', 255, opcional=True)
    registrar_nuevo_estado(estado, descripcion)


def modificar_estado():
    print('\n--- Modificar Estado de Asistencia ---')
    mostrar_listado_estados()
    id_estado = pedir_entero('Ingrese ID del estado a modificar: ')
    estado_obj = estado_por_id(id_estado)
    if estado_obj and estado_obj.habilitado == 1:
        print(f'\nEstado encontrado: {estado_obj.estado}')
        estado = pedir_texto(f'Nuevo estado [{estado_obj.estado}] (ENTER para conservar): ', 50, opcional=True) or estado_obj.estado
        descripcion = pedir_texto(f'Nueva descripción [{estado_obj.descripcion or "N/A"}] (ENTER para conservar): ', 255, opcional=True) or estado_obj.descripcion
        modificar_datos_estado(estado_obj, estado, descripcion)
    else:
        print('Estado no encontrado o inactivo.')


def eliminar_estado():
    print('\n--- Eliminar Estado de Asistencia ---')
    mostrar_listado_estados()
    id_estado = pedir_entero('Ingrese ID del estado a eliminar: ')
    estado_obj = estado_por_id(id_estado)
    if estado_obj and estado_obj.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja el estado {estado_obj.estado}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_estado(estado_obj.id_estado_asistencia)
    else:
        print('Estado no encontrado.')