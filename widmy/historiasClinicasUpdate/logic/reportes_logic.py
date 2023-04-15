from ..models import ReporteHistoria
from datetime import datetime

def add_report(request):
    fechafinal = datetime.strptime(request['fecha'], '%Y-%m-%d')
    reporte = ReporteHistoria(
        fechafinal,
        descripcion = request['descripcion'],
        HistoriaClinica = request['historiaClinica']
    )
    reporte.save()
    return reporte
