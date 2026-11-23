from datos.modelos.estado_asistencia import EstadoAsistencia


def listado_estados_asistencia():
    estados = EstadoAsistencia.select().where(EstadoAsistencia.habilitado == 1)
    return list(estados)


def obtener_estado_asistencia(id_estado):
    return EstadoAsistencia.get_or_none(EstadoAsistencia.id_estado_asistencia == id_estado)


def buscar_estado_asistencia(nombre_estado):
    return EstadoAsistencia.get_or_none(EstadoAsistencia.estado == nombre_estado)


def guardar_estado_asistencia(estado_asistencia: EstadoAsistencia):
    return estado_asistencia.save()


def registrar_estado_asistencia(estado, descripcion):
    nuevo = EstadoAsistencia(estado=estado, descripcion=descripcion)
    guardar_estado_asistencia(nuevo)
    return nuevo


def actualizar_estado_asistencia(id_estado, estado, descripcion):
    estado_asistencia = obtener_estado_asistencia(id_estado)
    if not estado_asistencia:
        return 0
    estado_asistencia.estado = estado
    estado_asistencia.descripcion = descripcion
    guardar_estado_asistencia(estado_asistencia)
    return 1


def eliminar_estado_asistencia(id_estado):
    filas = (EstadoAsistencia
             .update(habilitado=0)
             .where(EstadoAsistencia.id_estado_asistencia == id_estado)
             .execute())
    return filas