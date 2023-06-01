from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json
from .logic import logic_historyCD as lh
from widmy.auth import getRole
import logging

def create_history(request):
    role = getRole(request)

    logging.warning(role)
    
    if role in ['Administrador', 'Doctor']:
        if request.method == 'POST':
            history_dto = lh.create_history(json.loads(request.body))
            history = serializers.serialize('json', [history_dto,])
            return HttpResponse(history, 'application/json')
        else:
            return HttpResponseBadRequest('Only POST requests are allowed.')
    else:
        return HttpResponseBadRequest('Unauthorized user')