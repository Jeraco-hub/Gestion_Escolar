import bcrypt
from datos.modelos.usuario import Usuario
from auxiliares import mensaje_error


def validar_credenciales(correo: str, contrasena: str):
    try:
        usuario = Usuario.get_or_none(
            (Usuario.correo == correo) & (Usuario.habilitado == 1)
        )
        if not usuario:
            return None

        guardada = usuario.contrasena or ''
        if guardada.startswith('$2b$') or guardada.startswith('$2a$'):
            if bcrypt.checkpw(contrasena.encode('utf-8'), guardada.encode('utf-8')):
                return usuario
            return None
        else:
            if guardada == contrasena:
                return usuario
            return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None