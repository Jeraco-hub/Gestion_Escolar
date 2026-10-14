from peewee import SQL, Model, AutoField, CharField, IntegerField, FloatField, DateField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Calificacion(BaseModel):
    id_calificacion = AutoField()
    estudiante = IntegerField(index=True)
    evaluacion = IntegerField(index=True)
    nota = FloatField()
    fecha_registro = DateField()
    observacion = CharField(max_length=255, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'calificaciones'

