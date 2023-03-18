from django.http import HttpResponse
from .models import Medicos
from django.http import HttpResponseBadRequest

def create_medico(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        nombre = request.POST['nombre']
        identificacion = request.POST['identificacion']
        especialidad = request.POST['especialidad']
        # Create new Medico instance and save to database
        medico = Medicos(
            nombre=nombre,
            identificacion=identificacion,
            especialidad=especialidad
        )
        medico.save()
        # Redirect to list of medicos
        response_data = {'message': 'Medico created successfully.'}
        return HttpResponse(status=201, content=response_data)
    else:
        # Render the template for creating a new medico
        return HttpResponseBadRequest('Only POST requests are allowed.')


# Create your views here.
