from unittest.util import _MAX_LENGTH
from django.db import models
import random
import string

# Create your models here.

genero_choices=(
    (1, 'Hombre'),
    (2, 'Mujeres'),
)
hotel_choise=(
    (1,'Hotel Santiago'),
    (2,'Hotel Valparaiso'),
)

ninos_choise=(
    (1,'0'),
    (2,'1'),
    (3,'2'),
    (4,'3'),
    (5,'4'),
    (6,'5+'),
)

adultos_choise=(
    (1,'0'),
    (2,'1'),
    (3,'2'),
    (4,'3'),
    (5,'4'),
    (6,'5+'),
)


def random_id():
    return ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(32)]) 


class Registro(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    genero=models.IntegerField(choices=genero_choices)
    fecha_nacimiento=models.DateField()
    correo=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=30)
    termino_condiciones=models.BooleanField(default=False)

class Habitacion(models.Model):
    nombre_habitacion=models.CharField(max_length=30)
    hotel=models.IntegerField(choices=hotel_choise)
    habitaciones=models.CharField(max_length=30)
    camas=models.CharField(max_length=30)
    banos=models.CharField(max_length=30)
    foto=models.ImageField(upload_to="media")
    wifi=models.BooleanField(default=False)
    fumar=models.BooleanField(default=False)
    tv=models.BooleanField(default=False)
    jacuzzi=models.BooleanField(default=False)
    descripcion=models.CharField(max_length=150)
    precio=models.CharField(max_length=30)
    oferta=models.BooleanField(default=False)

class Reserva(models.Model):
    id=models.CharField(primary_key=True, max_length=9, default=random_id, editable=False)
    ida=models.CharField(max_length=30)
    vuelta=models.CharField(max_length=30)
    ninos=models.IntegerField(choices=ninos_choise)
    adultos=models.IntegerField(choices=adultos_choise)
    hotel=models.IntegerField(choices=hotel_choise)
    piscina=models.BooleanField(default=False)
    gimnasio=models.BooleanField(default=False)
    spa=models.BooleanField(default=False)
    cacha_tenis=models.BooleanField(default=False)

class Trabajador(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    genero=models.IntegerField(choices=genero_choices)
    fecha_nacimiento=models.DateField()
    edad=models.CharField(max_length=30)
    correo=models.CharField(max_length=30)
    cargo=models.CharField(max_length=30)
    vigente=models.BooleanField(default=True)

    


