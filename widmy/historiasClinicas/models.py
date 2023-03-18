from django.db import models

class HistoriaClinica(models.Model):
    fecha_nacimiento = models.DateField()
    fecha_ultima_actualizacion: models.DateField()


class Reporte(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length = 50)
    
