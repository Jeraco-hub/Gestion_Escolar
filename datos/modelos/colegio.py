from peewee import SQL, AutoField, CharField, IntegerField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Colegio(ModelBase):
    id_colegio = AutoField()
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=15, null=True)
    direccion = IntegerField(index=True, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'colegios'

