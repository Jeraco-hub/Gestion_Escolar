from datos.modelos.direccion import Direccion


def listado_direcciones():
    direcciones = Direccion.select().where(Direccion.habilitado == 1)
    return list(direcciones)


def obtener_direccion(id_direccion):
    return Direccion.get_or_none(Direccion.id_direccion == id_direccion)


def buscar_direccion(calle, numero, comuna):
    return Direccion.get_or_none(
        (Direccion.calle == calle) &
        (Direccion.numero == numero) &
        (Direccion.comuna == comuna)
    )


def registrar_direccion(calle, numero, comuna, ciudad):
    try:
        nueva = Direccion.create(
            calle=calle,
            numero=numero,
            comuna=comuna,
            ciudad=ciudad,
            habilitado=1
        )
        return nueva
    except Exception as error:
        print(f'Error al registrar dirección: {error}')
        return None


def actualizar_direccion(id_direccion, calle, numero, comuna, ciudad):
    filas = (Direccion
             .update(calle=calle, numero=numero, comuna=comuna, ciudad=ciudad)
             .where(Direccion.id_direccion == id_direccion)
             .execute())
    return filas


def eliminar_direccion(id_direccion):
    filas = (Direccion
             .update(habilitado=0)
             .where(Direccion.id_direccion == id_direccion)
             .execute())
    return filas