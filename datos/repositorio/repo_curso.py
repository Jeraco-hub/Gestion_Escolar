from datos.modelos.curso import Curso

def listado_cursos():
    cursos = Curso.select().where(Curso.habilitado == 1)
    return list(cursos)

def obtener_curso(id_curso):
    curso = Curso.get_or_none(Curso.id_curso == id_curso)
    return curso

def guardar_curso(curso: Curso):
    return curso.save()

def registrar_curso(nivel, letra, periodo, colegio):
    try:
        nuevo = Curso(
            nivel=nivel,
            letra=letra,
            periodo=periodo,
            colegio=colegio,
            habilitado=1
        )
        guardar_curso(nuevo)
        return nuevo
    except Exception as e:
        print(f"Error al registrar curso: {e}")
        return None

def actualizar_curso(id_curso, nivel, letra, periodo, colegio):
    try:
        curso = obtener_curso(id_curso)
        if not curso:
            return
        curso.nivel = nivel
        curso.letra = letra
        curso.periodo = periodo
        curso.colegio = colegio
        guardar_curso(curso)
    except Exception as e:
        print(f"Error al actualizar curso: {e}")

def eliminar_curso(id_curso):
    consulta = Curso.update(habilitado=0).where(Curso.id_curso == id_curso)
    consulta.execute()


def buscar_curso(nivel, letra, periodo, colegio):
    return Curso.get_or_none(
        (Curso.nivel == nivel) & (Curso.letra == letra) &
        (Curso.periodo == periodo) & (Curso.colegio == colegio)
    )