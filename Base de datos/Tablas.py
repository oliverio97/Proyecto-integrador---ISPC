from Configuración_BD import db
from peewee import AutoField, CharField, DateField, DateTimeField, ForeignKeyField, Model, IntegerField, TextField, Field, fn, JOIN
from playhouse.hybrid import hybrid_property
import datetime

class Ubicación(Model):
    Ciudad = CharField(30)
    Provincia = CharField (30)
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) #Fecha de inserción del registro
    Fecha_actualización = DateTimeField() #Fecha de actualización del registro
    Estado = CharField (default="A") #Estado del registro (A=activo, B=baja)

    class Meta:
        database = db

class Libros(Model):
    Costo = IntegerField
    Nombre = CharField(45)
    Autor = CharField(80)
    Páginas = IntegerField 
    Fecha_inserción= DateTimeField (default=datetime.datetime.now())
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A") 

    class Meta:
        database = db

class Género(Model):
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")
    Tipo = CharField(20)

    class Meta:
        database = db

class Cursos(Model):
    Costo = IntegerField
    Fecha_inicio = DateField()
    Fecha_finalización = DateField()
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")

    class Meta:
        database = db

    @hybrid_property
    def duración(self):
        inicio= datetime.date(self.Fecha_inicio.year,self.Fecha_inicio.month,self.Fecha_inicio.day)
        fin= datetime.date(self.Fecha_finalización.year,self.Fecha_finalización.month,self.Fecha_finalización.day)
        duración = fin-inicio
        return duración.days

class Clientes(Model):
    DNI = IntegerField (primary_key=True, unique=True)
    Nombre = CharField(50)
    Apellido = CharField(50)    
    Contraseña_hash= CharField(100)
    Fecha_nacimiento = DateField()
    Email = CharField(unique=True)
    Dirección = CharField(60)
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")
    Ubicación = ForeignKeyField(Ubicación, backref="Ubicación_clientes")
    Género = ForeignKeyField(Género, backref="Género_clientes")


    class Meta:
        database = db

    @hybrid_property
    def edad(self):
        today = datetime.date.today()
        edad = today.year - self.Fecha_nacimiento.year
        if (today.year, today.month, today.day) < (today.year, self.Fecha_nacimiento.month, self.Fecha_nacimiento.day):
            edad -= 1
        return edad

class Clientes_cursos(Model):
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")
    Clientes_dni = ForeignKeyField(Clientes, backref="Clientes_DNI")
    Charlas_talleres_id = ForeignKeyField(Cursos, backref="Charlas_talleres_id")

    class Meta:
        database = db

class Libros_Clientes(Model):
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")
    Libros_id = ForeignKeyField(Libros, backref="Libros_id")
    Clientes_dni = ForeignKeyField(Clientes,backref="Clientes_dni")
    
    class Meta:
        database = db

class Orientación(Model):
    Nombre = CharField(40)
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")

    class Meta:
        database = db

class Obra_social(Model):
    Nombre = CharField(30)
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")

    class Meta:
        database = db

class Especialidad(Model):
    Nombre = CharField(20)
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")

    class Meta:
        database = db


class Modalidad(Model):
    Tipo = CharField(20)
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")

    class Meta:
        database = db

class Psicólogos(Model):
    DNI = IntegerField (primary_key=True, unique=True)
    Nombre = CharField(50)
    Apellido = CharField(50)    
    Contraseña_hash= CharField(100)
    Fecha_nacimiento = DateField()
    Email = CharField(unique=True)
    Dirección_Consultorio = CharField(40)
    Teléfono = CharField(40)
    Matrícula = CharField(40)
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")
    Ubicación = ForeignKeyField(Ubicación, backref="Ubicación_psicólogos")
    Género = ForeignKeyField(Género, backref="Género_psicólogos")
    Modalidad = ForeignKeyField(Modalidad, backref="Modalidad_psicólogos")
    Especialidad = ForeignKeyField(Especialidad, backref="Especialidad_psicólogos")
    Orientación = ForeignKeyField(Orientación, backref="Psicólogos_orientación")
    
    class Meta:
        database = db

    
    @hybrid_property
    def edad(self):
        today = datetime.date.today()
        edad = today.year - self.Fecha_nacimiento.year
        if (today.year, today.month, today.day) < (today.year, self.Fecha_nacimiento.month, self.Fecha_nacimiento.day):
            edad -= 1
        return edad

class Psicólogos_obrasocial(Model):
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Estado = CharField (default="A")
    Psicólogos_dni = ForeignKeyField(Psicólogos,backref="Psicólogos_dni")
    Obra_social_id= ForeignKeyField(Obra_social,backref="Obra_social_id")

    class Meta:
        database = db

class Clientes_psicólogos(Model):    
    Fecha_inserción= DateTimeField (default=datetime.datetime.now()) 
    Fecha_actualización = DateTimeField()
    Honorarios = IntegerField ()
    Estado = CharField (default="A")
    Psicólogos_dni = ForeignKeyField(Psicólogos,backref="Psicólogos_dni")
    Clientes_dni= ForeignKeyField(Clientes,backref="Clientes_dni")

    class Meta:
        database = db


db.connect() #conexión a la base de datos

db.create_tables([Ubicación,Libros,Libros_Clientes,Cursos,Clientes_cursos, Orientación,
Clientes,Psicólogos,Psicólogos_obrasocial,Obra_social,Modalidad,Especialidad,Género,Clientes_psicólogos]) #creación de las tablas
