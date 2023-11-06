from .models import Procesos 
from rest_framework import viewsets, permissions
from .serializers import ProcesosSerializer  

class ProcesosViewSet(viewsets.ModelViewSet):
    queryset = Procesos.objects.all()
    permission_classes = [permissions.AllowAny]  # Debería ser "permission_classes" en lugar de "permissions_classes"
    serializer_class = ProcesosSerializer  # Debería ser "serializer_class" en lugar de "serializers_class"
