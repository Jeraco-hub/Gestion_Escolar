from datos.modelos.periodo_academico import PeriodoAcademico

def listado_periodos():
    periodos = PeriodoAcademico.select().where(PeriodoAcademico.habilitado == 1)
    return list(periodos)

def obtener_periodo(id_periodo):
    periodo = PeriodoAcademico.get_or_none(PeriodoAcademico.id_periodo == id_periodo)
    return periodo

def registrar_periodo(ano, semestre, fecha_inicio, fecha_fin, colegio):
    try:
        nuevo = PeriodoAcademico.create(
            ano=ano,
            semestre=semestre,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            colegio=colegio,
            habilitado=1
        )
        return nuevo
    except Exception as e:
        print(f"Error al registrar periodo: {e}")
        return None

def actualizar_periodo(id_periodo, ano, semestre, fecha_inicio, fecha_fin, colegio):
    try:
        consulta = PeriodoAcademico.update(
            ano=ano,
            semestre=semestre,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            colegio=colegio
        ).where(PeriodoAcademico.id_periodo == id_periodo)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar periodo: {e}")

def eliminar_periodo(id_periodo):
    consulta = PeriodoAcademico.update(habilitado=0).where(PeriodoAcademico.id_periodo == id_periodo)
    consulta.execute()
