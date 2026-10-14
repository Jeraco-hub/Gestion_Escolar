from datos.modelos.docente import Docente

def listado_docentes():
    docentes = Docente.select().where(Docente.habilitado == 1)
    return list(docentes)

def obtener_docente(id_docente):
    docente = Docente.get_or_none(Docente.id_docente == id_docente)
    return docente

def buscar_por_rut(rut):
    docente = Docente.get_or_none(Docente.rut == rut)
    return docente

def registrar_docente(nombre, apellido, rut, especialidad, fecha_nacimiento, correo, telefono, direccion, colegio):
    try:
        nuevo = Docente.create(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            especialidad=especialidad,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            colegio=colegio,
            habilitado=1
        )
        return nuevo
    except Exception as e:
        print(f"Error al registrar docente: {e}")
        return None

def actualizar_docente(id_docente, nombre, apellido, rut, especialidad, fecha_nacimiento, correo, telefono, direccion, colegio):
    try:
        consulta = Docente.update(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            especialidad=especialidad,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            colegio=colegio
        ).where(Docente.id_docente == id_docente)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar docente: {e}")

def eliminar_docente(id_docente):
    consulta = Docente.update(habilitado=0).where(Docente.id_docente == id_docente)
    consulta.execute()
