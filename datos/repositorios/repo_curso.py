from datos.modelos.curso import Curso

def listado_cursos():
    cursos = Curso.select().where(Curso.habilitado == 1)
    return list(cursos)

def obtener_curso(id_curso):
    curso = Curso.get_or_none(Curso.id_curso == id_curso)
    return curso

def registrar_curso(nivel, letra, periodo, colegio):
    try:
        nuevo = Curso.create(
            nivel=nivel,
            letra=letra,
            periodo=periodo,
            colegio=colegio,
            habilitado=1
        )
        return nuevo
    except Exception as e:
        print(f"Error al registrar curso: {e}")
        return None

def actualizar_curso(id_curso, nivel, letra, periodo, colegio):
    try:
        consulta = Curso.update(
            nivel=nivel,
            letra=letra,
            periodo=periodo,
            colegio=colegio
        ).where(Curso.id_curso == id_curso)
        consulta.execute()
    except Exception as e:
        print(f"Error al actualizar curso: {e}")

def eliminar_curso(id_curso):
    consulta = Curso.update(habilitado=0).where(Curso.id_curso == id_curso)
    consulta.execute()
