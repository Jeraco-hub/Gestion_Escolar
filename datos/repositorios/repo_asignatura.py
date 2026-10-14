from datos.modelos.asignatura import Asignatura

def listado_asignaturas():
    asignaturas = Asignatura.select().where(Asignatura.habilitado == 1)
    return list(asignaturas)

def obtener_asignatura(id_asignatura):
    asignatura = Asignatura.get_or_none(Asignatura.id_asignatura == id_asignatura)
    return asignatura

def registrar_asignatura(nombre, horas_semanales, docente, curso):
    try:
        nueva = Asignatura.create(
            nombre=nombre,
            horas_semanales=horas_semanales,
            docente=docente,
            curso=curso,
            habilitado=1
        )
        return nueva
    except Exception as e:
        print(f"Error al registrar asignatura: {e}")
        return None

def actualizar_asignatura(id_asignatura, nombre, horas_semanales, docente, curso):
    try:
        consulta = Asignatura.update(
            nombre=nombre,
            horas_semanales=horas_semanales,
            docente=docente,
            curso=curso
        ).where(Asignatura.id_asignatura == id_asignatura)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar asignatura: {e}")

def eliminar_asignatura(id_asignatura):
    consulta = Asignatura.update(habilitado=0).where(Asignatura.id_asignatura == id_asignatura)
    consulta.execute()
