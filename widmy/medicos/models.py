from django.db import models

class Medicos(models.Model):
    nombre = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} ({self.especialidad})'
