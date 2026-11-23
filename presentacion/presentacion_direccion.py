from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero
from negocio.negocio_direccion import (
    procesar_listado_direcciones,
    direccion_por_id,
    registrar_nueva_direccion,
    modificar_datos_direccion,
    deshabilitar_direccion
)


def mostrar_listado_direcciones():
    try:
        tabla = procesar_listado_direcciones(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay direcciones registradas.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_direccion():
    print('\n--- Registrar Nueva Dirección ---')
    calle = pedir_texto('Ingrese Calle: ', 50)
    numero = pedir_texto('Ingrese Número: ', 5)
    comuna = pedir_texto('Ingrese Comuna: ', 50)
    ciudad = pedir_texto('Ingrese Ciudad: ', 50)
    registrar_nueva_direccion(calle, numero, comuna, ciudad)


def modificar_direccion():
    print('\n--- Modificar Dirección ---')
    mostrar_listado_direcciones()
    id_direccion = pedir_entero('Ingrese ID de la dirección a modificar: ')
    direccion_obj = direccion_por_id(id_direccion)
    if direccion_obj and direccion_obj.habilitado == 1:
        print(f'\nDirección encontrada: {direccion_obj.calle} {direccion_obj.numero}, {direccion_obj.comuna}')
        calle = pedir_texto(f'Nueva calle [{direccion_obj.calle}] (ENTER para conservar): ', 50, opcional=True) or direccion_obj.calle
        numero = pedir_texto(f'Nuevo número [{direccion_obj.numero}] (ENTER para conservar): ', 5, opcional=True) or direccion_obj.numero
        comuna = pedir_texto(f'Nueva comuna [{direccion_obj.comuna}] (ENTER para conservar): ', 50, opcional=True) or direccion_obj.comuna
        ciudad = pedir_texto(f'Nueva ciudad [{direccion_obj.ciudad}] (ENTER para conservar): ', 50, opcional=True) or direccion_obj.ciudad
        modificar_datos_direccion(direccion_obj, calle, numero, comuna, ciudad)
    else:
        print('Dirección no encontrada o inactiva.')


def eliminar_direccion():
    print('\n--- Eliminar Dirección ---')
    mostrar_listado_direcciones()
    id_direccion = pedir_entero('Ingrese ID de la dirección a eliminar: ')
    direccion_obj = direccion_por_id(id_direccion)
    if direccion_obj and direccion_obj.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja la dirección {direccion_obj.calle} {direccion_obj.numero}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_direccion(direccion_obj.id_direccion)
    else:
        print('Dirección no encontrada.')