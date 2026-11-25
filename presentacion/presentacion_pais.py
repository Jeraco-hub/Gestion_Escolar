from prettytable import PrettyTable
from auxiliares import mensaje_error
from negocio.negocio_pais import (
    procesar_listado_paises,
    crear_objeto_pais,
    pais_por_nombre,
    modificar_datos_pais,
    deshabilitar_pais
)


def mostrar_listado_paises():
    try:
        tabla = procesar_listado_paises(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay países registrados o habilitados.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_pais():
    nombre = input('Ingrese nombre del país: ').strip()
    nacionalidad = input('Ingrese nacionalidad: ').strip()
    iso2 = input('Ingrese código ISO 2: ').strip()
    iso3 = input('Ingrese código ISO 3: ').strip()
    if not all([nombre, nacionalidad, iso2, iso3]):
        print('Todos los datos son obligatorios.')
        return
    crear_objeto_pais(nombre, nacionalidad, iso2, iso3)


def modificar_pais():
    nombre_pais = input('Ingrese nombre del país: ').strip()
    pais = pais_por_nombre(nombre_pais)
    if not pais:
        print('País no encontrado o inactivo.')
        return

    print('País Encontrado:')
    print(f'Nombre: {pais.pais}\nNacionalidad: {pais.nacionalidad}')
    nombre = input(f'Nuevo nombre [{pais.pais}]: ').strip() or pais.pais
    nacionalidad = input(f'Nueva nacionalidad [{pais.nacionalidad}]: ').strip() or pais.nacionalidad
    iso2 = input(f'Nuevo código ISO 2 [{pais.iso2}]: ').strip() or pais.iso2
    iso3 = input(f'Nuevo código ISO 3 [{pais.iso3}]: ').strip() or pais.iso3
    modificar_datos_pais(pais.id_pais, nombre, nacionalidad, iso2, iso3)


def eliminar_pais():
    nombre_pais = input('Ingrese nombre del país: ').strip()
    pais = pais_por_nombre(nombre_pais)
    if not pais:
        print('País no encontrado o inactivo.')
        return

    print('Se eliminará el país:')
    print(f'Nombre: {pais.pais}\nNacionalidad: {pais.nacionalidad}')
    confirmacion = input('¿Está seguro de dar de baja este país? (s/n): ')
    if confirmacion.lower() == 's':
        deshabilitar_pais(pais.id_pais)
