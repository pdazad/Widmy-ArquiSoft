from django.db import models

from historiasClinicas.models import historiaClinica #Toca importarlo para definir la relación de Many to One

class Pacientes(models.Model):
    historiaClinica = models.ForeignKey(historiaClinica, on_delete=models.CASCADE, default=None, null = True, blank = True) #llave foránea, relación many to one entre los modelos de Measurement y Variable.
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=3)
    identificacion = models.CharField(max_length=15)
    genero = models.CharField(max_length=1)
    tipoSangre = models.CharField(max_length=3)
    
    def __str__(self):
        return f'{self.nombre} ({self.identificacion})'
    
        

# Create your models here.
#Cada vez que se haga un cambio en los models se debe crear las migraciones de la base de datos con el comando:
# python manage.py makemigrations
# python manage.py migrate