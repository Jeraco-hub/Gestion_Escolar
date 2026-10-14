from peewee import SQL, Model, AutoField, CharField, IntegerField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Colegio(BaseModel):
    id_colegio = AutoField()
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=15, null=True)
    direccion = IntegerField(index=True, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'colegios'

