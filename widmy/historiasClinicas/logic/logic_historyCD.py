from ..models import HistoriaClinica
from datetime import datetime

def create_history(request):
    fechaNacimiento = request['fecha_nacimiento']
    fecha_nacimiento = datetime.strptime(fechaNacimiento, '%Y-%m-%d')
    fechaUltimaActualizacion = request['fecha_ultima_actualizacion']
    fecha_ultima_actualizacion = datetime.strptime(fechaUltimaActualizacion, '%Y-%m-%d')
    historia = HistoriaClinica(fecha_nacimiento,fecha_ultima_actualizacion)
    historia.save()
    return historia

def delete_history(request):
    historia = HistoriaClinica.objects.get(id=request['id'])
    historia.delete()
    return 1

