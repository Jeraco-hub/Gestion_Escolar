from datos.modelos.estado_asistencia import EstadoAsistencia

def listado_estados_asistencia():
    estados = EstadoAsistencia.select().where(EstadoAsistencia.habilitado == 1)
    return list(estados)

def obtener_estado_asistencia(id_estado):
    estado = EstadoAsistencia.get_or_none(EstadoAsistencia.id_estado_asistencia == id_estado)
    return estado
