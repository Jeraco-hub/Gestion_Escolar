from datos.modelos.direccion import Direccion

def listado_direcciones():
    # Obtiene todas las direcciones habilitadas
    direcciones = Direccion.select().where(Direccion.habilitado == 1)
    return list(direcciones)

def registrar_direccion(calle, numero, comuna, ciudad):
    try:
        nueva_dir = Direccion.create(
            calle=calle,
            numero=numero,
            comuna=comuna,
            ciudad=ciudad,
            habilitado=1
        )
        return nueva_dir
    except Exception as e:
        print(f"Error al registrar dirección: {e}")
        return None