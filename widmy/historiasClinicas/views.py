
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_historyCD as lh
 
@csrf_exempt
def create_history(request):
    if request.method == 'POST':
        history_dto = lh.create_history(json.loads(request.body))
        history = serializers.serialize('json', [history_dto,])
        return HttpResponse(history, 'application/json')
    else:
        return HttpResponseBadRequest('Only POST requests are allowed.')