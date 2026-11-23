from peewee import SQL, AutoField, CharField, IntegerField, DateField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Asistencia(ModelBase):
    id_asistencia = AutoField()
    estudiante = IntegerField(index=True)
    curso = IntegerField(index=True)
    fecha = DateField()
    estado_asistencia = IntegerField(index=True)
    justificacion = CharField(max_length=255, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'asistencias'

