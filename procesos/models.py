from django.db import models

class Procesos(models.Model):
    numero_proceso = models.CharField(max_length=255)
    nombre_proceso = models.CharField(max_length=255)
    tipo_proceso = models.CharField(max_length=255)
    fecha_apertura = models.DateTimeField()
    unidad_ejecutora = models.IntegerField()


    def __str__(self) -> str:
        return self.nombre_proceso