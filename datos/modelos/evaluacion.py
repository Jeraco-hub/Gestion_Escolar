from peewee import SQL, AutoField, CharField, IntegerField, FloatField, DateField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Evaluacion(ModelBase):
    id_evaluacion = AutoField()
    nombre = CharField(max_length=100)
    ponderacion = FloatField()
    fecha = DateField()
    asignatura = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'evaluaciones'

