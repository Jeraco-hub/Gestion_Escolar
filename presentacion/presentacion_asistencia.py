from datetime import datetime
from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero
from negocio.negocio_asistencia import (
    procesar_listado_asistencias,
    procesar_asistencias_estudiante,
    procesar_asistencias_curso,
    asistencia_por_id,
    registrar_nueva_asistencia,
    modificar_datos_asistencia,
    deshabilitar_asistencia
)


def _parsear_fecha(texto):
    try:
        return datetime.strptime(texto, '%d-%m-%Y').date()
    except ValueError:
        return None


def mostrar_listado_asistencias():
    try:
        tabla = procesar_listado_asistencias(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay asistencias registradas.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def mostrar_asistencias_estudiante():
    id_estudiante = pedir_entero('Ingrese ID del estudiante: ')
    try:
        tabla = procesar_asistencias_estudiante(PrettyTable(), id_estudiante)
        if tabla:
            print(tabla)
        else:
            print(f'No hay asistencias para el estudiante {id_estudiante}.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def mostrar_asistencias_curso():
    id_curso = pedir_entero('Ingrese ID del curso: ')
    while True:
        fecha_str = pedir_texto('Ingrese fecha (DD-MM-AAAA): ', 10)
        fecha = _parsear_fecha(fecha_str)
        if fecha:
            break
        print('Fecha inválida. Use DD-MM-AAAA.')
    try:
        tabla = procesar_asistencias_curso(PrettyTable(), id_curso, fecha)
        if tabla:
            print(tabla)
        else:
            print(f'No hay asistencias para el curso {id_curso} en {fecha}.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_asistencia():
    print('\n--- Registrar Nueva Asistencia ---')
    estudiante = pedir_entero('Ingrese ID del estudiante: ')
    curso = pedir_entero('Ingrese ID del curso: ')
    while True:
        fecha_str = pedir_texto('Ingrese fecha (DD-MM-AAAA): ', 10)
        fecha = _parsear_fecha(fecha_str)
        if fecha:
            break
        print('Fecha inválida. Use DD-MM-AAAA.')
    estado = pedir_entero('Ingrese ID del estado de asistencia: ')
    justificacion = pedir_texto('Ingrese Justificación (opcional): ', 255, opcional=True)
    registrar_nueva_asistencia(estudiante, curso, fecha, estado, justificacion)


def modificar_asistencia():
    print('\n--- Modificar Asistencia ---')
    mostrar_listado_asistencias()
    id_asistencia = pedir_entero('Ingrese ID de la asistencia a modificar: ')
    asistencia_obj = asistencia_por_id(id_asistencia)
    if asistencia_obj and asistencia_obj.habilitado == 1:
        print(f'\nAsistencia encontrada: Estudiante {asistencia_obj.estudiante}, Curso {asistencia_obj.curso}, Fecha {asistencia_obj.fecha}')
        estudiante = pedir_entero(f'Nuevo ID estudiante [{asistencia_obj.estudiante}] (ENTER para conservar): ', opcional=True) or asistencia_obj.estudiante
        curso = pedir_entero(f'Nuevo ID curso [{asistencia_obj.curso}] (ENTER para conservar): ', opcional=True) or asistencia_obj.curso
        fecha_str = pedir_texto(f'Nueva fecha [{asistencia_obj.fecha}] DD-MM-AAAA (ENTER para conservar): ', 10, opcional=True)
        fecha = _parsear_fecha(fecha_str) if fecha_str else asistencia_obj.fecha
        estado = pedir_entero(f'Nuevo ID estado [{asistencia_obj.estado_asistencia}] (ENTER para conservar): ', opcional=True) or asistencia_obj.estado_asistencia
        justificacion = pedir_texto(f'Nueva justificación [{asistencia_obj.justificacion or "N/A"}] (ENTER para conservar): ', 255, opcional=True) or asistencia_obj.justificacion
        modificar_datos_asistencia(asistencia_obj, estudiante, curso, fecha, estado, justificacion)
    else:
        print('Asistencia no encontrada o inactiva.')


def eliminar_asistencia():
    print('\n--- Eliminar Asistencia ---')
    mostrar_listado_asistencias()
    id_asistencia = pedir_entero('Ingrese ID de la asistencia a eliminar: ')
    asistencia_obj = asistencia_por_id(id_asistencia)
    if asistencia_obj and asistencia_obj.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja la asistencia {asistencia_obj.id_asistencia}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_asistencia(asistencia_obj.id_asistencia)
    else:
        print('Asistencia no encontrada.')