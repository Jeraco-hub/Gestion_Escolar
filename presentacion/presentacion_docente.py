from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.validaciones import (
    validar_rut,
    validar_largo_string,
    validar_correo,
    validar_fecha_nacimiento
)
from negocio.negocio_docente import (
    procesar_listado_docentes,
    docente_por_rut,
    registrar_nuevo_docente,
    modificar_datos_docente,
    deshabilitar_docente
)


def pedir_rut():
    rut = ''
    while rut == '':
        rut, mensaje = validar_rut(input('Ingrese RUT (ej: 11.111.111-1): ').strip())
        if rut == '':
            print(mensaje)
    return rut


def pedir_texto(etiqueta, largo, opcional=False):
    while True:
        ingresado = input(etiqueta).strip()
        if ingresado == '':
            if opcional:
                return ''
            print('Este dato es obligatorio, ingrese nuevamente...\n')
            continue
        valor, mensaje = validar_largo_string(ingresado, largo)
        if valor != '':
            return valor
        print(mensaje)


def pedir_correo(etiqueta, opcional=False):
    while True:
        correo = input(etiqueta).strip()
        if correo == '' and opcional:
            return ''
        correo, mensaje = validar_correo(correo)
        if correo != '':
            return correo.lower()
        print(mensaje)


def pedir_fecha(etiqueta):
    while True:
        ingresada = input(etiqueta).strip()
        if ingresada == '':
            return None
        fecha, mensaje = validar_fecha_nacimiento(ingresada)
        if fecha != '':
            return fecha
        print(mensaje)


def pedir_colegio(etiqueta, opcional=False):
    while True:
        entrada = input(etiqueta).strip()
        if entrada == '' and opcional:
            return None
        if entrada.isdecimal():
            return int(entrada)
        print('Ingrese un ID numérico.\n')


def mostrar_listado_docentes():
    try:
        tabla = procesar_listado_docentes(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay docentes registrados o habilitados.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_docente():
    print('\n--- Registrar Nuevo Docente ---')
    rut = pedir_rut()
    nombre = pedir_texto('Ingrese Nombre: ', 50)
    apellido = pedir_texto('Ingrese Apellido: ', 50)
    especialidad = pedir_texto('Ingrese Especialidad (opcional): ', 50, opcional=True)
    fecha = pedir_fecha('Fecha de nacimiento [dd/mm/aaaa] (opcional): ')
    correo = pedir_correo('Ingrese Correo electrónico: ')
    telefono = pedir_texto('Ingrese Teléfono (opcional): ', 15, opcional=True)
    colegio = pedir_colegio('Ingrese ID del colegio: ')

    registrar_nuevo_docente(nombre, apellido, rut, especialidad or None, fecha, correo, telefono or None, colegio)


def modificar_docente():
    print('\n--- Modificar Docente ---')
    rut = input('Ingrese RUT del docente a modificar: ').strip()
    docente = docente_por_rut(rut)
    if docente and docente.habilitado == 1:
        print(f'\nDocente encontrado: {docente.nombre} {docente.apellido} ({docente.correo})')
        nombre = pedir_texto(f'Nuevo nombre [{docente.nombre}] (ENTER para conservar): ', 50, opcional=True) or docente.nombre
        apellido = pedir_texto(f'Nuevo apellido [{docente.apellido}] (ENTER para conservar): ', 50, opcional=True) or docente.apellido
        especialidad = pedir_texto(f'Nueva especialidad [{docente.especialidad}] (ENTER para conservar): ', 50, opcional=True) or docente.especialidad
        fecha = pedir_fecha(f'Nueva fecha de nacimiento [dd/mm/aaaa] [{docente.fecha_nacimiento}] (ENTER para conservar): ') or docente.fecha_nacimiento
        correo = pedir_correo(f'Nuevo correo [{docente.correo}] (ENTER para conservar): ', opcional=True) or docente.correo
        telefono = pedir_texto(f'Nuevo teléfono [{docente.telefono}] (ENTER para conservar): ', 15, opcional=True) or docente.telefono
        colegio = pedir_colegio(f'Nuevo ID de colegio [{docente.colegio}] (ENTER para conservar): ', opcional=True) or docente.colegio

        modificar_datos_docente(docente, nombre, apellido, especialidad, fecha, correo, telefono, colegio)
    else:
        print('Docente no encontrado o inactivo.')


def eliminar_docente():
    print('\n--- Eliminar Docente ---')
    rut = input('Ingrese RUT del docente a eliminar: ').strip()
    docente = docente_por_rut(rut)
    if docente and docente.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja a {docente.nombre} {docente.apellido}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_docente(docente.id_docente)
    else:
        print('Docente no encontrado.')