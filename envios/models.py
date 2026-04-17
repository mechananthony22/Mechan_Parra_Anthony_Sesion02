from django.db import models

class Encomienda(models.Model):
    descripcion = models.CharField(max_length=255)
    peso = models.FloatField()
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion
