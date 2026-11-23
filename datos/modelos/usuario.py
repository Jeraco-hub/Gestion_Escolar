from peewee import SQL, AutoField, CharField, IntegerField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class Usuario(ModelBase):
    id_usuario = AutoField()
    nombre = CharField(max_length=100)
    correo = CharField(max_length=100, unique=True)
    contrasena = CharField(max_length=255)
    colegio = IntegerField(index=True, null=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'usuarios'

