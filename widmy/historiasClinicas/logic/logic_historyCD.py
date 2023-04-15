from ..models import HistoriaClinica

def create_history(request):
    historia = HistoriaClinica(
        fecha_nacimiento = request['fecha_nacimiento'],
        fecha_ultima_actualizacion = request['fecha_ultima_actualizacion']
        )
    historia.save()
    return historia

def delete_history(request):
    historia = HistoriaClinica.objects.get(id=request['id'])
    historia.delete()
    return 1

