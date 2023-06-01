from django.http import HttpResponse
from .models import Medicos
from django.http import HttpResponseBadRequest
from widmy.auth import getRole
import logging

def create_medico(request):
    role = getRole(request)

    logging.warning(role)

    if role in ['Administrador']:
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
    else:
        return HttpResponseBadRequest('Unauthorized user')