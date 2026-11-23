from datos.modelos.asistencia import Asistencia


def listado_asistencias():
    asistencias = Asistencia.select().where(Asistencia.habilitado == 1)
    return list(asistencias)


def obtener_asistencia(id_asistencia):
    return Asistencia.get_or_none(Asistencia.id_asistencia == id_asistencia)


def buscar_asistencia(estudiante, curso, fecha):
    return Asistencia.get_or_none(
        (Asistencia.estudiante == estudiante) &
        (Asistencia.curso == curso) &
        (Asistencia.fecha == fecha)
    )


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
    except Exception as error:
        print(f'Error al registrar asistencia: {error}')
        return None


def actualizar_asistencia(id_asistencia, estudiante, curso, fecha, estado_asistencia, justificacion):
    filas = (Asistencia
             .update(
                 estudiante=estudiante,
                 curso=curso,
                 fecha=fecha,
                 estado_asistencia=estado_asistencia,
                 justificacion=justificacion
             )
             .where(Asistencia.id_asistencia == id_asistencia)
             .execute())
    return filas


def eliminar_asistencia(id_asistencia):
    filas = (Asistencia
             .update(habilitado=0)
             .where(Asistencia.id_asistencia == id_asistencia)
             .execute())
    return filas