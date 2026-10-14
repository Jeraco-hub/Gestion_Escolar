from datos.modelos.colegio import Colegio

def listado_colegios():
    colegios = Colegio.select().where(Colegio.habilitado == 1)
    return list(colegios)

def obtener_colegio(id_colegio):
    colegio = Colegio.get_or_none(Colegio.id_colegio == id_colegio)
    return colegio

def registrar_colegio(nombre, telefono, direccion):
    try:
        nuevo = Colegio.create(
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
            habilitado=1
        )
        return nuevo
    except Exception as e:
        print(f"Error al registrar colegio: {e}")
        return None

def actualizar_colegio(id_colegio, nombre, telefono, direccion):
    try:
        consulta = Colegio.update(
            nombre=nombre,
            telefono=telefono,
            direccion=direccion
        ).where(Colegio.id_colegio == id_colegio)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar colegio: {e}")

def eliminar_colegio(id_colegio):
    consulta = Colegio.update(habilitado=0).where(Colegio.id_colegio == id_colegio)
    consulta.execute()
