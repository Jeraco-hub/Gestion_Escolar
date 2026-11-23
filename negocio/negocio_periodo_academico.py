from prettytable import PrettyTable
from datos.repositorio.repo_periodo_academico import (
    listado_periodos,
    obtener_periodo,
    buscar_periodo,
    registrar_periodo,
    actualizar_periodo,
    eliminar_periodo
)
from auxiliares import mensaje_error


def procesar_listado_periodos(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Año', 'Semestre', 'Inicio', 'Fin', 'Colegio']
    periodos = listado_periodos()
    if not periodos:
        return None
    for p in periodos:
        tabla.add_row([
            p.id_periodo,
            p.ano,
            p.semestre,
            p.fecha_inicio,
            p.fecha_fin,
            p.colegio
        ])
    return tabla


def periodo_por_id(id_periodo: int):
    try:
        return obtener_periodo(id_periodo)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_nuevo_periodo(ano, semestre, fecha_inicio, fecha_fin, colegio):
    try:
        existente = buscar_periodo(ano, semestre, colegio)
        if existente:
            if existente.habilitado == 1:
                print('Ya existe un período activo con ese año, semestre y colegio.')
            else:
                print('Ya existe un período deshabilitado con ese año, semestre y colegio.')
            return None
        nuevo = registrar_periodo(ano, semestre, fecha_inicio, fecha_fin, colegio)
        if nuevo:
            print(f'Período {ano} S{semestre} registrado con éxito.')
            return nuevo
        print('No se pudo registrar el período.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_periodo(periodo_obj, ano, semestre, fecha_inicio, fecha_fin, colegio):
    try:
        otro = buscar_periodo(ano, semestre, colegio)
        if otro and otro.id_periodo != periodo_obj.id_periodo:
            print('Ya existe otro período con ese año, semestre y colegio.')
            return
        actualizar_periodo(periodo_obj.id_periodo, ano, semestre, fecha_inicio, fecha_fin, colegio)
        print('Datos del período actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_periodo(id_periodo: int):
    try:
        eliminar_periodo(id_periodo)
        print('Período deshabilitado con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')