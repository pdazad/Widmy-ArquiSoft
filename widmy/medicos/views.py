from django.http import HttpResponse
from .models import Medicos
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole

@csfr_exempt
@login_required
def create_medico(request):
    role = getRole(request)
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