from peewee import SQL, Model, AutoField, CharField, IntegerField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Usuario(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length=100)
    correo = CharField(max_length=100, unique=True)
    contrasena = CharField(max_length=255)
    colegio = IntegerField(index=True, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'usuarios'

