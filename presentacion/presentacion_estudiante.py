from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.validaciones import validar_rut, validar_largo_string, validar_correo
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

def pedir_rut():
    rut = ''
    while rut == '':
        rut, mensaje = validar_rut(input('Ingrese RUT (ej: 12.345.678-5): ').strip())
        if rut == '':
            print(mensaje)
    return rut

def pedir_texto(etiqueta, largo):
    valor = ''
    while valor == '':
        ingresado = input(etiqueta).strip()
        valor, mensaje = validar_largo_string(ingresado, largo)
        if valor == '':
            if ingresado == '':
                print('Este dato es obligatorio, ingrese nuevamente...\n')
            else:
                print(mensaje)
    return valor

def pedir_correo():
    while True:
        correo = input('Ingrese Correo electrónico (opcional): ').strip()
        if correo == '':
            return ''
        correo, mensaje = validar_correo(correo)
        if correo != '':
            return correo
        print(mensaje)

def pedir_telefono():
    while True:
        telefono = input('Ingrese Teléfono (opcional): ').strip()
        if telefono == '':
            return ''
        telefono, mensaje = validar_largo_string(telefono, 15)
        if telefono != '':
            return telefono
        print(mensaje)

def crear_estudiante():
    print("\n--- Registrar Nuevo Estudiante ---")
    rut = pedir_rut()
    nombre = pedir_texto('Ingrese Nombre: ', 50)
    apellido = pedir_texto('Ingrese Apellido: ', 50)
    matricula = pedir_texto('Ingrese Matrícula (ej: MAT-2026-001): ', 20)
    correo = pedir_correo()
    telefono = pedir_telefono()

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