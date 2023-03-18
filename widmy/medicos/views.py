from django.http import HttpResponse
from .models import Medicos
from django.http import HttpResponseBadRequest

def create_medico(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        identificacion = request.POST['identificacion']
        especialidad = request.POST['especialidad']
        medico = Medicos(
            nombre=nombre,
            identificacion=identificacion,
            especialidad=especialidad
        )
        medico.save()
        response_data = {'message': 'Medico created successfully.'}
        return HttpResponse(status=201, content=response_data)
    else:
        return HttpResponseBadRequest('Only POST requests are allowed.')


# Create your views here.
