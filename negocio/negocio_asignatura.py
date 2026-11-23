from prettytable import PrettyTable
from datos.repositorio.repo_asignatura import (
    listado_asignaturas,
    obtener_asignatura,
    buscar_asignatura,
    registrar_asignatura,
    actualizar_asignatura,
    eliminar_asignatura
)
from datos.repositorio.repo_curso import obtener_curso
from datos.repositorio.repo_docente import obtener_docente
from auxiliares import mensaje_error


def procesar_listado_asignaturas(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Nombre', 'Horas semanales', 'Docente', 'Curso']
    asignaturas = listado_asignaturas()
    if not asignaturas:
        return None
    for a in asignaturas:
        tabla.add_row([
            a.id_asignatura,
            a.nombre,
            a.horas_semanales,
            a.docente if a.docente else 'N/A',
            a.curso
        ])
    return tabla


def asignatura_por_id(id_asignatura: int):
    try:
        return obtener_asignatura(id_asignatura)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def _validar_referencias(docente, curso):
    curso_obj = obtener_curso(curso)
    if not curso_obj or curso_obj.habilitado != 1:
        print('El curso indicado no existe o está deshabilitado.')
        return False
    if docente is not None:
        docente_obj = obtener_docente(docente)
        if not docente_obj or docente_obj.habilitado != 1:
            print('El docente indicado no existe o está deshabilitado.')
            return False
    return True


def registrar_nueva_asignatura(nombre, horas_semanales, docente, curso):
    try:
        if not _validar_referencias(docente, curso):
            return None

        existente = buscar_asignatura(nombre, curso)
        if existente:
            if existente.habilitado == 1:
                print('Ya existe una asignatura activa con ese nombre en ese curso.')
            else:
                print('Ya existe una asignatura deshabilitada con ese nombre en ese curso.')
            return None

        nueva = registrar_asignatura(nombre, horas_semanales, docente, curso)
        if nueva:
            print(f'Asignatura {nombre} registrada con éxito.')
            return nueva
        print('No se pudo registrar la asignatura.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_asignatura(asignatura, nombre, horas_semanales, docente, curso):
    try:
        if not _validar_referencias(docente, curso):
            return
        otra = buscar_asignatura(nombre, curso)
        if otra and otra.id_asignatura != asignatura.id_asignatura:
            print('Ya existe otra asignatura con ese nombre en ese curso.')
            return
        actualizar_asignatura(asignatura.id_asignatura, nombre, horas_semanales, docente, curso)
        print('Datos de la asignatura actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_asignatura(id_asignatura: int):
    try:
        eliminar_asignatura(id_asignatura)
        print('Asignatura deshabilitada con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')