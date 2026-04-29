from rest_framework import serializers
from .models import Empleado, Encomienda, HistorialEstado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class HistorialEstadoSerializer(serializers.ModelSerializer):
    empleado_nombre = serializers.CharField(source='empleado.nombre_completo', read_only=True)

    class Meta:
        model = HistorialEstado
        fields = '__all__'
        read_only_fields = ('fecha_cambio',)

class EncomiendaSerializer(serializers.ModelSerializer):
    historial = HistorialEstadoSerializer(many=True, read_only=True)
    remitente_nombre = serializers.CharField(source='remitente.nombre_completo', read_only=True)
    destinatario_nombre = serializers.CharField(source='destinatario.nombre_completo', read_only=True)

    class Meta:
        model = Encomienda
        fields = '__all__'
        read_only_fields = ('fecha_envio', 'fecha_entrega_real')

    def validate(self, data):
        if data.get('remitente') == data.get('destinatario'):
            raise serializers.ValidationError("Remitente y destinatario no pueden ser iguales.")
        return data
