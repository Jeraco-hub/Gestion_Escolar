from peewee import SQL, Model, AutoField, CharField, IntegerField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class EstadoAsistencia(BaseModel):
    id_estado_asistencia = AutoField()
    estado = CharField(max_length=50, unique=True)
    descripcion = CharField(max_length=255, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'estados_asistencia'

