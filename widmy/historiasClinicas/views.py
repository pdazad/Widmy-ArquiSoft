
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_historyCD as lh
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole
 
@csrf_exempt
@login_required
def create_history(request):
    role = getRole(request)
    if role in ['Administrador', 'Doctor']:
        if request.method == 'POST':
            history_dto = lh.create_history(json.loads(request.body))
            history = serializers.serialize('json', [history_dto,])
            return HttpResponse(history, 'application/json')
        else:
            return HttpResponseBadRequest('Only POST requests are allowed.')
    else:
        return HttpResponseBadRequest('Unauthorized user')