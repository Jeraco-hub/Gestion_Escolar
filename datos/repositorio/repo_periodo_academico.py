from datos.modelos.periodo_academico import PeriodoAcademico


def listado_periodos():
    periodos = PeriodoAcademico.select().where(PeriodoAcademico.habilitado == 1)
    return list(periodos)


def obtener_periodo(id_periodo):
    return PeriodoAcademico.get_or_none(PeriodoAcademico.id_periodo == id_periodo)


def buscar_periodo(ano, semestre, colegio):
    return PeriodoAcademico.get_or_none(
        (PeriodoAcademico.ano == ano) &
        (PeriodoAcademico.semestre == semestre) &
        (PeriodoAcademico.colegio == colegio)
    )


def guardar_periodo(periodo: PeriodoAcademico):
    return periodo.save()


def registrar_periodo(ano, semestre, fecha_inicio, fecha_fin, colegio):
    try:
        nuevo = PeriodoAcademico(
            ano=ano,
            semestre=semestre,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            colegio=colegio,
            habilitado=1
        )
        guardar_periodo(nuevo)
        return nuevo
    except Exception as error:
        print(f'Error al registrar período: {error}')
        return None


def actualizar_periodo(id_periodo, ano, semestre, fecha_inicio, fecha_fin, colegio):
    periodo = obtener_periodo(id_periodo)
    if not periodo:
        return 0
    periodo.ano = ano
    periodo.semestre = semestre
    periodo.fecha_inicio = fecha_inicio
    periodo.fecha_fin = fecha_fin
    periodo.colegio = colegio
    guardar_periodo(periodo)
    return 1


def eliminar_periodo(id_periodo):
    filas = (PeriodoAcademico
             .update(habilitado=0)
             .where(PeriodoAcademico.id_periodo == id_periodo)
             .execute())
    return filas