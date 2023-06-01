from django.shortcuts import get_object_or_404
from medicos.models import Medicos
from django.http import HttpResponse, HttpResponseBadRequest
from .logic import pacientes_logic as pl
from django.core import serializers
from widmy.auth import getRole
import json
import logging

def create_patient(request):

    role = getRole(request)

    logging.warning('Role found: ' + role)

    logging.warning('Role found: ' + role == 'Medico')

    if role in ['Personal Administrativo', 'Administrador', 'Enfermero', 'Medico']:
    #doctor = get_object_or_404(Medicos, id=doctor_id)
        if request.method == 'POST':
            patient_dto = pl.create_patient(json.loads(request.body))
            patient = serializers.serialize('json', [patient_dto,])
            return HttpResponse(patient, 'application/json')
        else:
            return HttpResponseBadRequest('Only POST requests are allowed.')
    else:
        return HttpResponseBadRequest('Unauthorized user')