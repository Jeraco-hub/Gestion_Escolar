import getpass
from auxiliares import mensaje_error
from negocio.negocio_login import validar_credenciales


def iniciar_sesion():
    print('\n=== Inicio de Sesión ===\n')
    intentos = 0
    max_intentos = 3
    while intentos < max_intentos:
        correo = input('Correo: ').strip()
        try:
            contrasena = getpass.getpass('Contraseña: ')
        except Exception:
            contrasena = ''
        usuario = validar_credenciales(correo, contrasena)
        if usuario:
            print(f'\nBienvenido/a, {usuario.nombre}.\n')
            return usuario
        intentos += 1
        print(f'Credenciales inválidas. Intento {intentos} de {max_intentos}.\n')
    print('Demasiados intentos fallidos. Cerrando el sistema.\n')
    return None