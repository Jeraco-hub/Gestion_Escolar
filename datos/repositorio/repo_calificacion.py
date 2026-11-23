from datos.modelos.calificacion import Calificacion

def listado_calificaciones():
    calificaciones = Calificacion.select().where(Calificacion.habilitado == 1)
    return list(calificaciones)

def obtener_calificacion(id_calificacion):
    calificacion = Calificacion.get_or_none(Calificacion.id_calificacion == id_calificacion)
    return calificacion

def calificaciones_por_estudiante(id_estudiante):
    calificaciones = Calificacion.select().where(
        (Calificacion.estudiante == id_estudiante) & (Calificacion.habilitado == 1)
    )
    return list(calificaciones)

def calificaciones_por_evaluacion(id_evaluacion):
    calificaciones = Calificacion.select().where(
        (Calificacion.evaluacion == id_evaluacion) & (Calificacion.habilitado == 1)
    )
    return list(calificaciones)

def registrar_calificacion(estudiante, evaluacion, nota, fecha_registro, observacion):
    try:
        nueva = Calificacion.create(
            estudiante=estudiante,
            evaluacion=evaluacion,
            nota=nota,
            fecha_registro=fecha_registro,
            observacion=observacion,
            habilitado=1
        )
        return nueva
    except Exception as e:
        print(f"Error al registrar calificacion: {e}")
        return None

def actualizar_calificacion(id_calificacion, estudiante, evaluacion, nota, fecha_registro, observacion):
    try:
        consulta = Calificacion.update(
            estudiante=estudiante,
            evaluacion=evaluacion,
            nota=nota,
            fecha_registro=fecha_registro,
            observacion=observacion
        ).where(Calificacion.id_calificacion == id_calificacion)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar calificacion: {e}")

def eliminar_calificacion(id_calificacion):
    consulta = Calificacion.update(habilitado=0).where(Calificacion.id_calificacion == id_calificacion)
    consulta.execute()
