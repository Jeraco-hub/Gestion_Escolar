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
    except Exception as error:
        print(f'Error al registrar período: {error}')
        return None


def actualizar_periodo(id_periodo, ano, semestre, fecha_inicio, fecha_fin, colegio):
    filas = (PeriodoAcademico
             .update(
                 ano=ano,
                 semestre=semestre,
                 fecha_inicio=fecha_inicio,
                 fecha_fin=fecha_fin,
                 colegio=colegio
             )
             .where(PeriodoAcademico.id_periodo == id_periodo)
             .execute())
    return filas


def eliminar_periodo(id_periodo):
    filas = (PeriodoAcademico
             .update(habilitado=0)
             .where(PeriodoAcademico.id_periodo == id_periodo)
             .execute())
    return filas