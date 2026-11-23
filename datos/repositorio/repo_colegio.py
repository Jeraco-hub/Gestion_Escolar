from datos.modelos.colegio import Colegio


def listado_colegios():
    colegios = Colegio.select().where(Colegio.habilitado == 1)
    return list(colegios)


def obtener_colegio(id_colegio):
    return Colegio.get_or_none(Colegio.id_colegio == id_colegio)


def buscar_colegio(nombre):
    return Colegio.get_or_none(Colegio.nombre == nombre)


def registrar_colegio(nombre, telefono, direccion):
    try:
        nuevo = Colegio.create(
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
            habilitado=1
        )
        return nuevo
    except Exception as error:
        print(f'Error al registrar colegio: {error}')
        return None


def actualizar_colegio(id_colegio, nombre, telefono, direccion):
    filas = (Colegio
             .update(nombre=nombre, telefono=telefono, direccion=direccion)
             .where(Colegio.id_colegio == id_colegio)
             .execute())
    return filas


def eliminar_colegio(id_colegio):
    filas = (Colegio
             .update(habilitado=0)
             .where(Colegio.id_colegio == id_colegio)
             .execute())
    return filas