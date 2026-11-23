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

def guardar_evaluacion(evaluacion: Evaluacion):
    return evaluacion.save()

def registrar_evaluacion(nombre, ponderacion, fecha, asignatura):
    try:
        nueva = Evaluacion(
            nombre=nombre,
            ponderacion=ponderacion,
            fecha=fecha,
            asignatura=asignatura,
            habilitado=1
        )
        guardar_evaluacion(nueva)
        return nueva
    except Exception as e:
        print(f"Error al registrar evaluacion: {e}")
        return None

def actualizar_evaluacion(id_evaluacion, nombre, ponderacion, fecha, asignatura):
    try:
        evaluacion = obtener_evaluacion(id_evaluacion)
        if not evaluacion:
            return
        evaluacion.nombre = nombre
        evaluacion.ponderacion = ponderacion
        evaluacion.fecha = fecha
        evaluacion.asignatura = asignatura
        guardar_evaluacion(evaluacion)
    except Exception as e:
        print(f"Error al actualizar evaluacion: {e}")

def eliminar_evaluacion(id_evaluacion):
    consulta = Evaluacion.update(habilitado=0).where(Evaluacion.id_evaluacion == id_evaluacion)
    consulta.execute()