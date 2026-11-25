from prettytable import PrettyTable
from datos.repositorio.repositorio_pais import (
    listado_paises,
    buscar_paises,
    obtener_pais_nombre,
    registrar_pais,
    actualizar_pais,
    eliminar_pais
)
from auxiliares import mensaje_error


def procesar_listado_paises(tabla: PrettyTable):
    tabla.field_names = ['Id', 'País', 'Nacionalidad', 'ISO 2', 'ISO 3']
    lista_paises = listado_paises()
    if not lista_paises:
        return None
    for pais in lista_paises:
        tabla.add_row([
            pais.id_pais,
            pais.pais,
            pais.nacionalidad,
            pais.iso2,
            pais.iso3
        ])
    return tabla


def listado_paises_nombre(tabla: PrettyTable, nombre_pais):
    id_paises = []
    tabla.field_names = ['Id', 'País', 'Nacionalidad']
    lista_paises = buscar_paises(nombre_pais)
    if not lista_paises:
        return None, id_paises
    for pais in lista_paises:
        tabla.add_row([pais.id_pais, pais.pais, pais.nacionalidad])
        id_paises.append(pais.id_pais)
    return tabla, id_paises


def pais_por_nombre(nombre_pais):
    try:
        return obtener_pais_nombre(nombre_pais)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def crear_objeto_pais(nombre, nacionalidad, iso2, iso3):
    try:
        nuevo = registrar_pais(nombre, nacionalidad, iso2, iso3)
        if nuevo:
            print(f'País {nombre} registrado con éxito.')
        return nuevo
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_pais(id_pais, nombre, nacionalidad, iso2, iso3):
    try:
        pais = actualizar_pais(id_pais, nombre, nacionalidad, iso2, iso3)
        if pais:
            print('Datos del país actualizados correctamente.')
        else:
            print('País no encontrado.')
        return pais
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def deshabilitar_pais(id_pais):
    try:
        filas = eliminar_pais(id_pais)
        if filas:
            print('País deshabilitado con éxito (Borrado lógico).')
        else:
            print('País no encontrado.')
        return filas
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return 0
