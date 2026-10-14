from datos.modelos.asistencia import Asistencia

def listado_asistencias():
    asistencias = Asistencia.select().where(Asistencia.habilitado == 1)
    return list(asistencias)

def obtener_asistencia(id_asistencia):
    asistencia = Asistencia.get_or_none(Asistencia.id_asistencia == id_asistencia)
    return asistencia

def asistencias_por_estudiante(id_estudiante):
    asistencias = Asistencia.select().where(
        (Asistencia.estudiante == id_estudiante) & (Asistencia.habilitado == 1)
    )
    return list(asistencias)

def asistencias_por_curso(id_curso, fecha):
    asistencias = Asistencia.select().where(
        (Asistencia.curso == id_curso) & (Asistencia.fecha == fecha) & (Asistencia.habilitado == 1)
    )
    return list(asistencias)

def registrar_asistencia(estudiante, curso, fecha, estado_asistencia, justificacion):
    try:
        nueva = Asistencia.create(
            estudiante=estudiante,
            curso=curso,
            fecha=fecha,
            estado_asistencia=estado_asistencia,
            justificacion=justificacion,
            habilitado=1
        )
        return nueva
    except Exception as e:
        print(f"Error al registrar asistencia: {e}")
        return None

def actualizar_asistencia(id_asistencia, estudiante, curso, fecha, estado_asistencia, justificacion):
    try:
        consulta = Asistencia.update(
            estudiante=estudiante,
            curso=curso,
            fecha=fecha,
            estado_asistencia=estado_asistencia,
            justificacion=justificacion
        ).where(Asistencia.id_asistencia == id_asistencia)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar asistencia: {e}")

def eliminar_asistencia(id_asistencia):
    consulta = Asistencia.update(habilitado=0).where(Asistencia.id_asistencia == id_asistencia)
    consulta.execute()
