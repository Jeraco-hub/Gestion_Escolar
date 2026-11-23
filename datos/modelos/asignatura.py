from peewee import SQL, AutoField, CharField, IntegerField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Asignatura(ModelBase):
    id_asignatura = AutoField()
    nombre = CharField(max_length=100)
    horas_semanales = IntegerField()
    docente = IntegerField(index=True, null=True)
    curso = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'asignaturas'

