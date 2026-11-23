from peewee import SQL, AutoField, CharField, IntegerField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class EstadoAsistencia(ModelBase):
    id_estado_asistencia = AutoField()
    estado = CharField(max_length=50, unique=True)
    descripcion = CharField(max_length=255, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'estados_asistencia'

