from datos.modelos.usuario import Usuario

def listado_usuarios():
    usuarios = Usuario.select().where(Usuario.habilitado == 1)
    return list(usuarios)

def obtener_usuario(id_usuario):
    usuario = Usuario.get_or_none(Usuario.id_usuario == id_usuario)
    return usuario

def buscar_por_correo(correo):
    usuario = Usuario.get_or_none(Usuario.correo == correo)
    return usuario

def registrar_usuario(nombre, correo, contrasena, colegio):
    try:
        nuevo = Usuario.create(
            nombre=nombre,
            correo=correo,
            contrasena=contrasena,
            colegio=colegio,
            habilitado=1
        )
        return nuevo
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return None

def actualizar_usuario(id_usuario, nombre, correo, contrasena, colegio):
    try:
        consulta = Usuario.update(
            nombre=nombre,
            correo=correo,
            contrasena=contrasena,
            colegio=colegio
        ).where(Usuario.id_usuario == id_usuario)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")

def eliminar_usuario(id_usuario):
    consulta = Usuario.update(habilitado=0).where(Usuario.id_usuario == id_usuario)
    consulta.execute()
