from django.shortcuts import get_object_or_404
from medicos.models import Medicos
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from .logic import pacientes_logic as pl
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole

@csrf_exempt
@login_required
def create_patient(request):
    role = getRole(request)
    if role in ['Personal Administrativo', 'Administrador']:
    #doctor = get_object_or_404(Medicos, id=doctor_id)
        if request.method == 'POST':
            patient_dto = pl.create_patient(json.loads(request.body))
            patient = serializers.serialize('json', [patient_dto,])
            return HttpResponse(patient, 'application/json')
        else:
            return HttpResponseBadRequest('Only POST requests are allowed.')
    else:
        return HttpResponseBadRequest('Unauthorized user')
