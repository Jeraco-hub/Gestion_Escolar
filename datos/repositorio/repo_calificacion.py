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

def guardar_calificacion(calificacion: Calificacion):
    return calificacion.save()

def registrar_calificacion(estudiante, evaluacion, nota, fecha_registro, observacion):
    try:
        nueva = Calificacion(
            estudiante=estudiante,
            evaluacion=evaluacion,
            nota=nota,
            fecha_registro=fecha_registro,
            observacion=observacion,
            habilitado=1
        )
        guardar_calificacion(nueva)
        return nueva
    except Exception as e:
        print(f"Error al registrar calificacion: {e}")
        return None

def actualizar_calificacion(id_calificacion, estudiante, evaluacion, nota, fecha_registro, observacion):
    try:
        calificacion = obtener_calificacion(id_calificacion)
        if not calificacion:
            return
        calificacion.estudiante = estudiante
        calificacion.evaluacion = evaluacion
        calificacion.nota = nota
        calificacion.fecha_registro = fecha_registro
        calificacion.observacion = observacion
        guardar_calificacion(calificacion)
    except Exception as e:
        print(f"Error al actualizar calificacion: {e}")

def eliminar_calificacion(id_calificacion):
    consulta = Calificacion.update(habilitado=0).where(Calificacion.id_calificacion == id_calificacion)
    consulta.execute()