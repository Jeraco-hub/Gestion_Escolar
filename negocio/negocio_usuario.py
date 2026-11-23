from prettytable import PrettyTable
from datos.repositorios.repo_usuario import (
    listado_usuarios,
    buscar_por_correo,
    registrar_usuario,
    actualizar_usuario,
    eliminar_usuario
)
from auxiliares import mensaje_error


def procesar_listado_usuarios(tabla: PrettyTable):
    tabla.field_names = ['ID', 'Nombre', 'Correo', 'Colegio']
    usuarios = listado_usuarios()
    if not usuarios:
        return None
    for u in usuarios:
        tabla.add_row([u.id_usuario, u.nombre, u.correo, u.colegio if u.colegio else 'N/A'])
    return tabla


def usuario_por_correo(correo: str):
    try:
        return buscar_por_correo(correo)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_nuevo_usuario(nombre: str, correo: str, contrasena_hash: str, colegio):
    try:
        existente = buscar_por_correo(correo)
        if existente:
            if existente.habilitado == 1:
                print('Ya existe un usuario activo con ese correo.')
            else:
                print('Ya existe un usuario deshabilitado con ese correo.')
            return None

        nuevo = registrar_usuario(nombre, correo, contrasena_hash, colegio)
        if nuevo:
            print(f'Usuario {nombre} registrado con éxito.')
            return nuevo
        print('No se pudo registrar el usuario.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_usuario(usuario, nombre: str, correo: str, colegio):
    try:
        if correo != usuario.correo and buscar_por_correo(correo):
            print('Ya existe otro usuario con ese correo.')
            return
        actualizar_usuario(usuario.id_usuario, nombre, correo, usuario.contrasena, colegio)
        print('Datos del usuario actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_usuario(id_usuario: int):
    try:
        eliminar_usuario(id_usuario)
        print('Usuario deshabilitado con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')