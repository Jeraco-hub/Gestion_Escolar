from peewee import SQL, AutoField, CharField, IntegerField, DateField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Estudiante(ModelBase):
    id_estudiante = AutoField()
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    rut = CharField(max_length=20, unique=True)
    matricula = CharField(max_length=20, unique=True)
    fecha_nacimiento = DateField(null=True)
    correo = CharField(max_length=100, null=True)
    telefono = CharField(max_length=15, null=True)
    curso = IntegerField(index=True, null=True)
    direccion = IntegerField(index=True, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'estudiantes'

