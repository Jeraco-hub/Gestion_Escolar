from peewee import SQL, Model, AutoField, CharField, IntegerField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Asignatura(BaseModel):
    id_asignatura = AutoField()
    nombre = CharField(max_length=100)
    horas_semanales = IntegerField()
    docente = IntegerField(index=True, null=True)
    curso = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'asignaturas'

