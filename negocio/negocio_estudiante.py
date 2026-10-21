from prettytable import PrettyTable
from datos import (
    listado_estudiantes,
    buscar_por_rut,
    registrar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante
)
from auxiliares import mensaje_error

def procesar_listado_estudiantes(tabla: PrettyTable):
    if tabla:
        tabla.field_names = ['ID', 'RUT', 'Nombre', 'Apellido', 'Matrícula', 'Correo', 'Teléfono']
        alumnos = listado_estudiantes()
        if alumnos:
            for al in alumnos:
                tabla.add_row([
                    al.id_estudiante,
                    al.rut,
                    al.nombre,
                    al.apellido,
                    al.matricula,
                    al.correo if al.correo else 'N/A',
                    al.telefono if al.telefono else 'N/A'
                ])
            return tabla
        return None

def registrar_nuevo_estudiante(nombre: str, apellido: str, rut: str, matricula: str, correo: str, telefono: str):
    try:
        # Validación de duplicados antes de insertar
        existente = buscar_por_rut(rut)
        if existente and existente.habilitado == 1:
            print(f'Error: Ya existe un estudiante registrado con el RUT {rut}.')
            return None
        
        nuevo = registrar_estudiante(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            matricula=matricula,
            fecha_nacimiento=None,
            correo=correo if correo != '' else None,
            telefono=telefono if telefono != '' else None,
            curso=None,
            direccion=None
        )
        if nuevo:
            print(f'Estudiante {nombre} {apellido} registrado con éxito.')
            return nuevo
    except Exception as error:
        print(f'{mensaje_error}{error}')
        return None

def modificar_datos_estudiante(id_estudiante: int, nombre: str, apellido: str, rut: str, matricula: str, correo: str, telefono: str):
    try:
        actualizar_estudiante(
            id_estudiante=id_estudiante,
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            matricula=matricula,
            fecha_nacimiento=None,
            correo=correo,
            telefono=telefono,
            curso=None,
            direccion=None
        )
        print("Datos del estudiante actualizados correctamente.")
    except Exception as error:
        print(f'{mensaje_error}{error}')

def deshabilitar_estudiante(id_estudiante: int):
    try:
        eliminar_estudiante(id_estudiante)
        print("Estudiante deshabilitado con éxito (Borrado lógico).")
    except Exception as error:
        print(f'{mensaje_error}{error}')