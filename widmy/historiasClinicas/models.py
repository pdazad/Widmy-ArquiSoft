from django.db import models

class HistoriaClinica(models.Model):
    fecha_nacimiento = models.DateField()
    fecha_ultima_actualizacion = models.DateField()
