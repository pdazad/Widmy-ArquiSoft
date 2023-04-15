from ..models import HistoriaClinica
from datetime import datetime

def create_history(request):
    fecha_nacimiento = datetime.strptime(request['fecha_nacimiento'], '%Y-%m-%d').date()
    fecha_ultima_actualizacion = datetime.strptime(request['fecha_ultima_actualizacion'], '%Y-%m-%d').date()
    historia = HistoriaClinica(fecha_nacimiento=fecha_nacimiento, fecha_ultima_actualizacion=fecha_ultima_actualizacion)
    historia.save()
    return historia

def delete_history(request):
    historia = HistoriaClinica.objects.get(id=request['id'])
    historia.delete()
    return 1

