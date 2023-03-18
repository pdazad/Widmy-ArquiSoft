from ..models import Paciente

def create_paciente(request):
    paciente = Paciente(
        nombre = request['nombre'], 
        edad = request['edad'], 
        identificacion = request['identificacion'],
        genero = request['genero'],
        tipoSangre = request['tipoSangre']
        )
    paciente.save()
    return paciente

