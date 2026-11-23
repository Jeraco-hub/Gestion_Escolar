from prettytable import PrettyTable
from datos.repositorio.repo_docente import (
    listado_docentes,
    buscar_por_rut,
    buscar_por_correo,
    registrar_docente,
    actualizar_docente,
    eliminar_docente
)
from auxiliares import mensaje_error


def procesar_listado_docentes(tabla: PrettyTable):
    tabla.field_names = ['ID', 'RUT', 'Nombre', 'Apellido', 'Especialidad', 'Correo', 'Teléfono', 'Colegio']
    docentes = listado_docentes()
    if not docentes:
        return None
    for d in docentes:
        tabla.add_row([
            d.id_docente,
            d.rut,
            d.nombre,
            d.apellido,
            d.especialidad if d.especialidad else 'N/A',
            d.correo,
            d.telefono if d.telefono else 'N/A',
            d.colegio
        ])
    return tabla


def docente_por_rut(rut: str):
    try:
        return buscar_por_rut(rut)
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def registrar_nuevo_docente(nombre, apellido, rut, especialidad, fecha_nacimiento, correo, telefono, colegio):
    try:
        existente_rut = buscar_por_rut(rut)
        if existente_rut:
            if existente_rut.habilitado == 1:
                print('Ya existe un docente activo con ese RUT.')
            else:
                print('Ya existe un docente deshabilitado con ese RUT.')
            return None

        existente_correo = buscar_por_correo(correo)
        if existente_correo:
            if existente_correo.habilitado == 1:
                print('Ya existe un docente activo con ese correo.')
            else:
                print('Ya existe un docente deshabilitado con ese correo.')
            return None

        nuevo = registrar_docente(
            nombre, apellido, rut, especialidad, fecha_nacimiento,
            correo, telefono, None, colegio
        )
        if nuevo:
            print(f'Docente {nombre} {apellido} registrado con éxito.')
            return nuevo
        print('No se pudo registrar el docente.')
        return None
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None


def modificar_datos_docente(docente, nombre, apellido, especialidad, fecha_nacimiento, correo, telefono, colegio):
    try:
        if correo != docente.correo and buscar_por_correo(correo):
            print('Ya existe otro docente con ese correo.')
            return
        actualizar_docente(
            docente.id_docente, nombre, apellido, docente.rut, especialidad,
            fecha_nacimiento, correo, telefono, docente.direccion, colegio
        )
        print('Datos del docente actualizados correctamente.')
    except Exception as error:
        print(f'{mensaje_error}{error}')


def deshabilitar_docente(id_docente: int):
    try:
        eliminar_docente(id_docente)
        print('Docente deshabilitado con éxito (Borrado lógico).')
    except Exception as error:
        print(f'{mensaje_error}{error}')