from rest_framework import serializers
from .models import Ruta

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

    def validate_distancia_km(self, value):
        if value <= 0:
            raise serializers.ValidationError("La distancia debe ser mayor a 0.")
        return value
