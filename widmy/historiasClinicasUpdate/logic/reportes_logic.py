from ..models import ReporteHistoria
from datetime import datetime
from historiasClinicas.models import HistoriaClinica

def add_report(request):
    fecha = datetime.strptime(request['fecha'], '%Y-%m-%d')
    reporte = ReporteHistoria(
        fecha = fecha,
        descripcion = request['descripcion'],
        HistoriaClinica = HistoriaClinica.objects.get(id=request['historiaClinica'])
    )
    reporte.save()
    return reporte