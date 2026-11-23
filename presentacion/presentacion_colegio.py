from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero
from negocio.negocio_colegio import (
    procesar_listado_colegios,
    colegio_por_id,
    registrar_nuevo_colegio,
    modificar_datos_colegio,
    deshabilitar_colegio
)


def mostrar_listado_colegios():
    try:
        tabla = procesar_listado_colegios(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay colegios registrados.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_colegio():
    print('\n--- Registrar Nuevo Colegio ---')
    nombre = pedir_texto('Ingrese Nombre: ', 100)
    telefono = pedir_texto('Ingrese Teléfono (opcional): ', 15, opcional=True)
    direccion = pedir_entero('Ingrese ID de la dirección (opcional): ', opcional=True)
    registrar_nuevo_colegio(nombre, telefono, direccion)


def modificar_colegio():
    print('\n--- Modificar Colegio ---')
    mostrar_listado_colegios()
    id_colegio = pedir_entero('Ingrese ID del colegio a modificar: ')
    colegio_obj = colegio_por_id(id_colegio)
    if colegio_obj and colegio_obj.habilitado == 1:
        print(f'\nColegio encontrado: {colegio_obj.nombre}')
        nombre = pedir_texto(f'Nuevo nombre [{colegio_obj.nombre}] (ENTER para conservar): ', 100, opcional=True) or colegio_obj.nombre
        telefono = pedir_texto(f'Nuevo teléfono [{colegio_obj.telefono or "N/A"}] (ENTER para conservar): ', 15, opcional=True) or colegio_obj.telefono
        direccion = pedir_entero(f'Nuevo ID de dirección [{colegio_obj.direccion or "N/A"}] (ENTER para conservar): ', opcional=True) or colegio_obj.direccion
        modificar_datos_colegio(colegio_obj, nombre, telefono, direccion)
    else:
        print('Colegio no encontrado o inactivo.')


def eliminar_colegio():
    print('\n--- Eliminar Colegio ---')
    mostrar_listado_colegios()
    id_colegio = pedir_entero('Ingrese ID del colegio a eliminar: ')
    colegio_obj = colegio_por_id(id_colegio)
    if colegio_obj and colegio_obj.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja el colegio {colegio_obj.nombre}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_colegio(colegio_obj.id_colegio)
    else:
        print('Colegio no encontrado.')