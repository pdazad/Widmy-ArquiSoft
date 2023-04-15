from django.shortcuts import get_object_or_404
from historiasClinicas.models import HistoriaClinica
from django.http import HttpResponse, HttpResponseBadRequest
from .logic import reportes_logic as rl
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update_history(request):
    if request.method == 'POST':
        report_dto = rl.add_report(json.loads(request.body))
        report = serializers.serialize('json', [report_dto,])
        return HttpResponse(report, 'application/json')
    else:
        return HttpResponseBadRequest('Only PUT requests are allowed.')