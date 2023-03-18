from django.shortcuts import get_object_or_404
from .models import Pacientes
from medicos.models import Medicos
from django.http import HttpResponse, HttpResponseBadRequest

def create_patient(request, doctor_id):
    doctor = get_object_or_404(Medicos, id=doctor_id)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        identificacion = request.POST['identificacion']
        genero = request.POST['genero']
        tipoSangre = request.POST['tipoSangre']
        paciente = Pacientes(
            historiaClinica=doctor.historiaClinica,
            nombre=nombre,
            edad=edad,
            identificacion=identificacion,
            genero=genero,
            tipoSangre=tipoSangre
        )
        paciente.save()
        response_data = {'message': 'Paciente created successfully.'}
        return HttpResponse(status=201, content=response_data)
    else:
        return HttpResponseBadRequest('Only POST requests are allowed.')
