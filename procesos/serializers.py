from rest_framework import serializers
from .models import Procesos

class ProcesosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procesos
        fields = '__all__'