from peewee import SQL, Model, AutoField, CharField, IntegerField, DateField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Asistencia(BaseModel):
    id_asistencia = AutoField()
    estudiante = IntegerField(index=True)
    curso = IntegerField(index=True)
    fecha = DateField()
    estado_asistencia = IntegerField(index=True)
    justificacion = CharField(max_length=255, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'asistencias'

