from datos.modelos.estado_asistencia import EstadoAsistencia


def listado_estados_asistencia():
    estados = EstadoAsistencia.select().where(EstadoAsistencia.habilitado == 1)
    return list(estados)


def obtener_estado_asistencia(id_estado):
    return EstadoAsistencia.get_or_none(EstadoAsistencia.id_estado_asistencia == id_estado)


def buscar_estado_asistencia(nombre_estado):
    return EstadoAsistencia.get_or_none(EstadoAsistencia.estado == nombre_estado)


def registrar_estado_asistencia(estado, descripcion):
    nuevo = EstadoAsistencia.create(estado=estado, descripcion=descripcion)
    return nuevo


def actualizar_estado_asistencia(id_estado, estado, descripcion):
    filas = (EstadoAsistencia
             .update(estado=estado, descripcion=descripcion)
             .where(EstadoAsistencia.id_estado_asistencia == id_estado)
             .execute())
    return filas


def eliminar_estado_asistencia(id_estado):
    filas = (EstadoAsistencia
             .update(habilitado=0)
             .where(EstadoAsistencia.id_estado_asistencia == id_estado)
             .execute())
    return filas