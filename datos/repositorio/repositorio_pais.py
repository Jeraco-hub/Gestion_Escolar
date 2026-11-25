from datos.modelos.pais import Pais
from auxiliares import mensaje_error

def listado_paises():
    try:
        paises = Pais.select().where(Pais.habilitado == True)
        if paises:
            return paises
    except Exception as error:
        print(f'{mensaje_error}{error}')

def buscar_paises(nombre_pais):
    try:
        return list(Pais.select().where(
            (Pais.pais.contains(nombre_pais)) & (Pais.habilitado == 1)
        ))
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return []


def obtener_pais_nombre(nombre_pais):
    try:
        return Pais.get_or_none(
            (Pais.pais.contains(nombre_pais)) & (Pais.habilitado == 1)
        )
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def obtener_pais_id(id_pais):
    try:
        return Pais.get_or_none(
            (Pais.id_pais == id_pais) & (Pais.habilitado == 1)
        )
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_pais(nombre, nacionalidad, iso2, iso3):
    try:
        nuevo = Pais(
            pais=nombre,
            nacionalidad=nacionalidad,
            iso2=iso2,
            iso3=iso3,
            habilitado=1
        )
        guardar_pais(nuevo)
        return nuevo
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def actualizar_pais(id_pais, nombre, nacionalidad, iso2, iso3):
    try:
        pais = obtener_pais_id(id_pais)
        if not pais:
            return None
        pais.pais = nombre
        pais.nacionalidad = nacionalidad
        pais.iso2 = iso2
        pais.iso3 = iso3
        guardar_pais(pais)
        return pais
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def eliminar_pais(id_pais):
    try:
        return (Pais
                .update(habilitado=0)
                .where(Pais.id_pais == id_pais)
                .execute())
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return 0


def guardar_pais(pais: Pais):
    try:
        respuesta = pais.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {pais.pais}')
        return respuesta
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return 0