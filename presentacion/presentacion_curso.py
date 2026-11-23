from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.entradas import pedir_texto, pedir_entero
from negocio.negocio_curso import (
    procesar_listado_cursos,
    curso_por_id,
    registrar_nuevo_curso,
    modificar_datos_curso,
    deshabilitar_curso
)


def mostrar_listado_cursos():
    try:
        tabla = procesar_listado_cursos(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay cursos registrados o habilitados.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_curso():
    print('\n--- Registrar Nuevo Curso ---')
    nivel = pedir_texto('Ingrese Nivel (ej: 1° Medio): ', 50)
    letra = pedir_texto('Ingrese Letra (ej: A): ', 10)
    periodo = pedir_entero('Ingrese ID del período académico: ')
    colegio = pedir_entero('Ingrese ID del colegio: ')

    registrar_nuevo_curso(nivel, letra, periodo, colegio)


def modificar_curso():
    print('\n--- Modificar Curso ---')
    mostrar_listado_cursos()
    id_curso = pedir_entero('Ingrese ID del curso a modificar: ')
    curso = curso_por_id(id_curso)
    if curso and curso.habilitado == 1:
        print(f'\nCurso encontrado: {curso.nivel} {curso.letra}')
        nivel = pedir_texto(f'Nuevo nivel [{curso.nivel}] (ENTER para conservar): ', 50, opcional=True) or curso.nivel
        letra = pedir_texto(f'Nueva letra [{curso.letra}] (ENTER para conservar): ', 10, opcional=True) or curso.letra
        periodo = pedir_entero(f'Nuevo ID de período [{curso.periodo}] (ENTER para conservar): ', opcional=True) or curso.periodo
        colegio = pedir_entero(f'Nuevo ID de colegio [{curso.colegio}] (ENTER para conservar): ', opcional=True) or curso.colegio

        modificar_datos_curso(curso, nivel, letra, periodo, colegio)
    else:
        print('Curso no encontrado o inactivo.')


def eliminar_curso():
    print('\n--- Eliminar Curso ---')
    mostrar_listado_cursos()
    id_curso = pedir_entero('Ingrese ID del curso a eliminar: ')
    curso = curso_por_id(id_curso)
    if curso and curso.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja el curso {curso.nivel} {curso.letra}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_curso(curso.id_curso)
    else:
        print('Curso no encontrado.')