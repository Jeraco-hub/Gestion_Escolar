from peewee import SQL, Model, AutoField, CharField, IntegerField, FloatField, DateField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Evaluacion(BaseModel):
    id_evaluacion = AutoField()
    nombre = CharField(max_length=100)
    ponderacion = FloatField()
    fecha = DateField()
    asignatura = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'evaluaciones'

