from prettytable import PrettyTable
from auxiliares import mensaje_error
from datos import buscar_por_rut
from negocio import (
    procesar_listado_estudiantes,
    registrar_nuevo_estudiante,
    modificar_datos_estudiante,
    deshabilitar_estudiante
)

def mostrar_listado_estudiantes():
    try:
        tabla = PrettyTable()
        tabla = procesar_listado_estudiantes(tabla)
        if tabla:
            print(tabla)
        else:
            print("No hay estudiantes registrados o habilitados.")
    except Exception as error:
        print(f'{mensaje_error}{error}')

def crear_estudiante():
    print("\n--- Registrar Nuevo Estudiante ---")
    rut = ''
    while rut == '':
        rut = input('Ingrese RUT (ej: 23.456.789-1): ')
    nombre = ''
    while nombre == '':
        nombre = input('Ingrese Nombre: ')
    apellido = ''
    while apellido == '':
        apellido = input('Ingrese Apellido: ')
    matricula = ''
    while matricula == '':
        matricula = input('Ingrese Matrícula (ej: MAT-2026-001): ')
    correo = input('Ingrese Correo electrónico (opcional): ')
    telefono = input('Ingrese Teléfono (opcional): ')

    registrar_nuevo_estudiante(nombre, apellido, rut, matricula, correo, telefono)

def modificar_estudiante():
    print("\n--- Modificar Estudiante ---")
    rut = input('Ingrese RUT del estudiante a modificar: ')
    estudiante = buscar_por_rut(rut)
    if estudiante and estudiante.habilitado == 1:
        print(f'\nEstudiante encontrado: {estudiante.nombre} {estudiante.apellido} (Matrícula: {estudiante.matricula})')
        nuevo_nombre = input(f'Nuevo nombre [{estudiante.nombre}]: ') or estudiante.nombre
        nuevo_apellido = input(f'Nuevo apellido [{estudiante.apellido}]: ') or estudiante.apellido
        nueva_matricula = input(f'Nueva matrícula [{estudiante.matricula}]: ') or estudiante.matricula
        nuevo_correo = input(f'Nuevo correo [{estudiante.correo}]: ') or estudiante.correo
        nuevo_telefono = input(f'Nuevo teléfono [{estudiante.telefono}]: ') or estudiante.telefono

        modificar_datos_estudiante(
            estudiante.id_estudiante,
            nuevo_nombre,
            nuevo_apellido,
            estudiante.rut,
            nueva_matricula,
            nuevo_correo,
            nuevo_telefono
        )
    else:
        print('Estudiante no encontrado o inactivo.')

def eliminar_estudiante():
    print("\n--- Eliminar Estudiante ---")
    rut = input('Ingrese RUT del estudiante a eliminar: ')
    estudiante = buscar_por_rut(rut)
    if estudiante and estudiante.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja a {estudiante.nombre} {estudiante.apellido}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_estudiante(estudiante.id_estudiante)
    else:
        print('Estudiante no encontrado.')