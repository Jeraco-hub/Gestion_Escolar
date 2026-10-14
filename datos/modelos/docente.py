from peewee import SQL, Model, AutoField, CharField, IntegerField, DateField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Docente(BaseModel):
    id_docente = AutoField()
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    rut = CharField(max_length=20, unique=True)
    especialidad = CharField(max_length=50, null=True)
    fecha_nacimiento = DateField(null=True)
    correo = CharField(max_length=100, unique=True)
    telefono = CharField(max_length=15, null=True)
    direccion = IntegerField(index=True, null=True)
    colegio = IntegerField(index=True)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'docentes'
