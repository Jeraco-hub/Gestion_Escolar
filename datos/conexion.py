from peewee import SQL, Model, AutoField, CharField, IntegerField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Direccion(BaseModel):
    id_direccion = AutoField()
    calle = CharField(max_length=50)
    numero = CharField(max_length=5)
    comuna = CharField(max_length=50)
    ciudad = CharField(max_length=50)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'direcciones'