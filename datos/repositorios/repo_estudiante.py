from datos.modelos.estudiante import Estudiante

def listado_estudiantes():
    estudiantes = Estudiante.select().where(Estudiante.habilitado == 1)
    return list(estudiantes)

def obtener_estudiante(id_estudiante):
    estudiante = Estudiante.get_or_none(Estudiante.id_estudiante == id_estudiante)
    return estudiante

def buscar_por_rut(rut):
    estudiante = Estudiante.get_or_none(Estudiante.rut == rut)
    return estudiante

def buscar_por_matricula(matricula):
    estudiante = Estudiante.get_or_none(Estudiante.matricula == matricula)
    return estudiante

def registrar_estudiante(nombre, apellido, rut, matricula, fecha_nacimiento, correo, telefono, curso, direccion):
    try:
        nuevo = Estudiante.create(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            matricula=matricula,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            curso=curso,
            direccion=direccion,
            habilitado=1
        )
        return nuevo
    except Exception as e:
        print(f"Error al registrar estudiante: {e}")
        return None

def actualizar_estudiante(id_estudiante, nombre, apellido, rut, matricula, fecha_nacimiento, correo, telefono, curso, direccion):
    try:
        consulta = Estudiante.update(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            matricula=matricula,
            fecha_nacimiento=fecha_nacimiento,
            correo=correo,
            telefono=telefono,
            curso=curso,
            direccion=direccion
        ).where(Estudiante.id_estudiante == id_estudiante)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar estudiante: {e}")

def eliminar_estudiante(id_estudiante):
    consulta = Estudiante.update(habilitado=0).where(Estudiante.id_estudiante == id_estudiante)
    consulta.execute()
