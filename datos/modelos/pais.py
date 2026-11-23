from peewee import SQL, AutoField, CharField, IntegerField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Pais(ModelBase):
    id_pais = AutoField()
    pais = CharField(max_length=50)
    nacionalidad = CharField(max_length=50, null=True)
    iso2 = CharField(max_length=2)
    iso3 = CharField(max_length=3)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'paises'