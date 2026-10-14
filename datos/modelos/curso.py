from peewee import SQL, Model, AutoField, CharField, IntegerField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Curso(BaseModel):
    id_curso = AutoField()
    nivel = CharField(max_length=50)
    letra = CharField(max_length=10)
    periodo = IntegerField(index=True)
    colegio = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'cursos'

