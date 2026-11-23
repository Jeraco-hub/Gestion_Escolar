import getpass
import bcrypt
from prettytable import PrettyTable
from auxiliares import mensaje_error
from auxiliares.validaciones import validar_largo_string, validar_correo, validar_contrasena
from negocio.negocio_usuario import (
    procesar_listado_usuarios,
    usuario_por_correo,
    registrar_nuevo_usuario,
    modificar_datos_usuario,
    deshabilitar_usuario
)


def solicitar_nombre(etiqueta, opcional=False):
    while True:
        valor = input(etiqueta).strip()
        if valor == '':
            if opcional:
                return ''
            print('Este dato es obligatorio, ingrese nuevamente...\n')
            continue
        valor, mensaje = validar_largo_string(valor, 100)
        if valor != '':
            return valor
        print(mensaje)


def solicitar_correo(etiqueta, opcional=False):
    while True:
        correo = input(etiqueta).strip()
        if correo == '' and opcional:
            return ''
        correo, mensaje = validar_correo(correo)
        if correo != '':
            return correo.lower()
        print(mensaje)


def solicitar_colegio(etiqueta):
    while True:
        entrada = input(etiqueta).strip()
        if entrada == '':
            return ''
        if entrada.isdecimal():
            return int(entrada)
        print('Ingrese un ID numérico.\n')


def solicitar_contrasena():
    print('Contraseña segura:')
    print('- Entre 8 y 15 caracteres')
    print('- Al menos una mayúscula, una minúscula y un número')
    print('- Al menos un símbolo: ! @ # $ % & /')
    while True:
        contrasena = getpass.getpass('Contraseña: ')
        contrasena, errores = validar_contrasena(contrasena)
        if errores:
            print('Contraseña inválida:')
            for error in errores:
                print('-', error)
            print()
            continue
        repetida = getpass.getpass('Repita la contraseña: ')
        if repetida != contrasena:
            print('Las contraseñas no coinciden, ingrese nuevamente...\n')
            continue
        return contrasena


def mostrar_listado_usuarios():
    try:
        tabla = procesar_listado_usuarios(PrettyTable())
        if tabla:
            print(tabla)
        else:
            print('No hay usuarios registrados o habilitados.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def crear_usuario():
    print('\n--- Registrar Nuevo Usuario ---')
    nombre = solicitar_nombre('Nombre: ')
    correo = solicitar_correo('Correo: ')
    colegio = solicitar_colegio('ID del colegio (opcional): ')
    contrasena = solicitar_contrasena()
    hash_contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    registrar_nuevo_usuario(nombre, correo, hash_contrasena, colegio if colegio != '' else None)


def modificar_usuario():
    print('\n--- Modificar Usuario ---')
    correo_actual = solicitar_correo('Correo del usuario a modificar: ')
    usuario = usuario_por_correo(correo_actual)
    if not usuario or usuario.habilitado != 1:
        print('Usuario no encontrado o inactivo.')
        return

    print(f'\nUsuario encontrado: {usuario.nombre} ({usuario.correo})')
    nombre = solicitar_nombre(f'Nuevo nombre [{usuario.nombre}] (ENTER para conservar): ', opcional=True) or usuario.nombre
    correo = solicitar_correo(f'Nuevo correo [{usuario.correo}] (ENTER para conservar): ', opcional=True) or usuario.correo
    colegio = solicitar_colegio(f'Nuevo ID de colegio [{usuario.colegio}] (ENTER para conservar): ')
    if colegio == '':
        colegio = usuario.colegio

    modificar_datos_usuario(usuario, nombre, correo, colegio)


def eliminar_usuario():
    print('\n--- Eliminar Usuario ---')
    correo = solicitar_correo('Correo del usuario a eliminar: ')
    usuario = usuario_por_correo(correo)
    if usuario and usuario.habilitado == 1:
        confirmacion = input(f'¿Está seguro de dar de baja a {usuario.nombre}? (s/n): ')
        if confirmacion.lower() == 's':
            deshabilitar_usuario(usuario.id_usuario)
    else:
        print('Usuario no encontrado.')