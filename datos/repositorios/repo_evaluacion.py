from datos.modelos.evaluacion import Evaluacion

def listado_evaluaciones():
    evaluaciones = Evaluacion.select().where(Evaluacion.habilitado == 1)
    return list(evaluaciones)

def obtener_evaluacion(id_evaluacion):
    evaluacion = Evaluacion.get_or_none(Evaluacion.id_evaluacion == id_evaluacion)
    return evaluacion

def evaluaciones_por_asignatura(id_asignatura):
    evaluaciones = Evaluacion.select().where(
        (Evaluacion.asignatura == id_asignatura) & (Evaluacion.habilitado == 1)
    )
    return list(evaluaciones)

def registrar_evaluacion(nombre, ponderacion, fecha, asignatura):
    try:
        nueva = Evaluacion.create(
            nombre=nombre,
            ponderacion=ponderacion,
            fecha=fecha,
            asignatura=asignatura,
            habilitado=1
        )
        return nueva
    except Exception as e:
        print(f"Error al registrar evaluacion: {e}")
        return None

def actualizar_evaluacion(id_evaluacion, nombre, ponderacion, fecha, asignatura):
    try:
        consulta = Evaluacion.update(
            nombre=nombre,
            ponderacion=ponderacion,
            fecha=fecha,
            asignatura=asignatura
        ).where(Evaluacion.id_evaluacion == id_evaluacion)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar evaluacion: {e}")

def eliminar_evaluacion(id_evaluacion):
    consulta = Evaluacion.update(habilitado=0).where(Evaluacion.id_evaluacion == id_evaluacion)
    consulta.execute()
