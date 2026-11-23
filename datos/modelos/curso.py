from peewee import SQL, AutoField, CharField, IntegerField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Curso(ModelBase):
    id_curso = AutoField()
    nivel = CharField(max_length=50)
    letra = CharField(max_length=10)
    periodo = IntegerField(index=True)
    colegio = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'cursos'

