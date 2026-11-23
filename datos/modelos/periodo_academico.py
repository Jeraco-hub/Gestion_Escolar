from peewee import SQL, AutoField, IntegerField, DateField
from datos.model_base import ModelBase
from auxiliares.datos_app import defecto

class PeriodoAcademico(ModelBase):
    id_periodo = AutoField()
    ano = IntegerField()
    semestre = IntegerField()
    fecha_inicio = DateField()
    fecha_fin = DateField()
    colegio = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'periodos_academicos'

