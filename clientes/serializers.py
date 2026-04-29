from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ('fecha_registro',)

    def validate_nro_doc(self, value):
        if len(value) != 8:
            raise serializers.ValidationError("El documento debe tener 8 dígitos.")
        return value
