from peewee import SQL, AutoField, CharField, IntegerField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Direccion(ModelBase):
    id_direccion = AutoField()
    calle = CharField(max_length=50)
    numero = CharField(max_length=5)
    comuna = CharField(max_length=50)
    ciudad = CharField(max_length=50)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'direcciones'
