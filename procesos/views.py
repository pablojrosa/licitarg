from rest_framework import viewsets
from .serializers import ProcesosSerializer
from .models import Procesos


# Create your views here.
class ProcesosViews(viewsets.ModelViewSet):
    serializer_class = ProcesosSerializer
    queryset = Procesos.objects.all()
