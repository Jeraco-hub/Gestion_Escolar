from peewee import Model
from datos.conexion import conectar

base_datos = conectar()


class ModelBase(Model):
    """Clase base de todos los modelos ORM: centraliza la conexión a la base de datos."""

    class Meta:
        database = base_datos