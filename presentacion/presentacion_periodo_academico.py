from datetime import datetime
from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero
from negocio.negocio_periodo_academico import (
    procesar_listado_periodos,
    periodo_por_id,
    registrar_nuevo_periodo,
    modificar_datos_periodo,
    deshabilitar_periodo
)


def _parsear_fecha(texto):
    try:
        return datetime.strptime(texto, '%d-%m-%Y').date()
    except ValueError:
        return None


def mostrar_listado_periodos():
    try:
        tabla = procesar_listado_periodos(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay períodos académicos registrados.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_periodo():
    print('\n--- Registrar Nuevo Período Académico ---')
    ano = pedir_entero('Ingrese Año (ej: 2025): ', minimo=2000)
    semestre = pedir_entero('Ingrese Semestre (1 o 2): ', minimo=1)
    while True:
        fecha_inicio_str = pedir_texto('Ingrese Fecha Inicio (DD-MM-AAAA): ', 10)
        fecha_inicio = _parsear_fecha(fecha_inicio_str)
        if fecha_inicio:
            break
        print('Fecha inválida. Use DD-MM-AAAA.')
    while True:
        fecha_fin_str = pedir_texto('Ingrese Fecha Fin (DD-MM-AAAA): ', 10)
        fecha_fin = _parsear_fecha(fecha_fin_str)
        if fecha_fin:
            break
        print('Fecha inválida. Use DD-MM-AAAA.')
    colegio = pedir_entero('Ingrese ID del colegio: ')
    registrar_nuevo_periodo(ano, semestre, fecha_inicio, fecha_fin, colegio)


def modificar_periodo():
    print('\n--- Modificar Período Académico ---')
    mostrar_listado_periodos()
    id_periodo = pedir_entero('Ingrese ID del período a modificar: ')
    periodo_obj = periodo_por_id(id_periodo)
    if periodo_obj and periodo_obj.habilitado == 1:
        print(f'\nPeríodo encontrado: {periodo_obj.ano} S{periodo_obj.semestre}')
        ano = pedir_entero(f'Nuevo año [{periodo_obj.ano}] (ENTER para conservar): ', opcional=True, minimo=2000) or periodo_obj.ano
        semestre = pedir_entero(f'Nuevo semestre [{periodo_obj.semestre}] (ENTER para conservar): ', opcional=True, minimo=1) or periodo_obj.semestre
        fecha_inicio_str = pedir_texto(f'Nueva fecha inicio [{periodo_obj.fecha_inicio}] DD-MM-AAAA (ENTER para conservar): ', 10, opcional=True)
        fecha_inicio = _parsear_fecha(fecha_inicio_str) if fecha_inicio_str else periodo_obj.fecha_inicio
        fecha_fin_str = pedir_texto(f'Nueva fecha fin [{periodo_obj.fecha_fin}] DD-MM-AAAA (ENTER para conservar): ', 10, opcional=True)
        fecha_fin = _parsear_fecha(fecha_fin_str) if fecha_fin_str else periodo_obj.fecha_fin
        colegio = pedir_entero(f'Nuevo ID colegio [{periodo_obj.colegio}] (ENTER para conservar): ', opcional=True) or periodo_obj.colegio
        modificar_datos_periodo(periodo_obj, ano, semestre, fecha_inicio, fecha_fin, colegio)
    else:
        print('Período no encontrado o inactivo.')


def eliminar_periodo():
    print('\n--- Eliminar Período Académico ---')
    mostrar_listado_periodos()
    id_periodo = pedir_entero('Ingrese ID del período a eliminar: ')
    periodo_obj = periodo_por_id(id_periodo)
    if periodo_obj and periodo_obj.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja el período {periodo_obj.ano} S{periodo_obj.semestre}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_periodo(periodo_obj.id_periodo)
    else:
        print('Período no encontrado.')