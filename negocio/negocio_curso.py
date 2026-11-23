from prettytable import PrettyTable
from datos.repositorios.repo_curso import (
    listado_cursos,
    obtener_curso,
    buscar_curso,
    registrar_curso,
    actualizar_curso,
    eliminar_curso
)
from auxiliares import mensaje_error


def procesar_listado_cursos(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Nivel', 'Letra', 'Período', 'Colegio']
    cursos = listado_cursos()
    if not cursos:
        return None
    for c in cursos:
        tabla.add_row([c.id_curso, c.nivel, c.letra, c.periodo, c.colegio])
    return tabla


def curso_por_id(id_curso: int):
    try:
        return obtener_curso(id_curso)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_nuevo_curso(nivel, letra, periodo, colegio):
    try:
        existente = buscar_curso(nivel, letra, periodo, colegio)
        if existente:
            if existente.habilitado == 1:
                print('Ya existe un curso activo con ese nivel, letra, período y colegio.')
            else:
                print('Ya existe un curso deshabilitado con ese nivel, letra, período y colegio.')
            return None

        nuevo = registrar_curso(nivel, letra, periodo, colegio)
        if nuevo:
            print(f'Curso {nivel} {letra} registrado con éxito.')
            return nuevo
        print('No se pudo registrar el curso. Verifique que el período y el colegio existan.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_curso(curso, nivel, letra, periodo, colegio):
    try:
        otro = buscar_curso(nivel, letra, periodo, colegio)
        if otro and otro.id_curso != curso.id_curso:
            print('Ya existe otro curso con esos datos.')
            return
        actualizar_curso(curso.id_curso, nivel, letra, periodo, colegio)
        print('Datos del curso actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_curso(id_curso: int):
    try:
        eliminar_curso(id_curso)
        print('Curso deshabilitado con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')