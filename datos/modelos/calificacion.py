from peewee import SQL, AutoField, CharField, IntegerField, FloatField, DateField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Calificacion(ModelBase):
    id_calificacion = AutoField()
    estudiante = IntegerField(index=True)
    evaluacion = IntegerField(index=True)
    nota = FloatField()
    fecha_registro = DateField()
    observacion = CharField(max_length=255, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'calificaciones'

