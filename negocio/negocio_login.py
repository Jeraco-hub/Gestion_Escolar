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

        guardada = (usuario.contrasena or '').encode('utf-8')
        if bcrypt.checkpw(contrasena.encode('utf-8'), guardada):
            return usuario
        return None
    except ValueError:
        # Hash inválido o contraseña demasiado larga: no se permite el acceso
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None