from django.db import models
from historiasClinicas.models import HistoriaClinica


class ReporteHistoria(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length = 50)
    HistoriaClinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    