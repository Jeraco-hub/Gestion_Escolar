from peewee import SQL, Model, AutoField, IntegerField, DateField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class PeriodoAcademico(BaseModel):
    id_periodo = AutoField()
    ano = IntegerField()
    semestre = IntegerField()
    fecha_inicio = DateField()
    fecha_fin = DateField()
    colegio = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'periodos_academicos'

