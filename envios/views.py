from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Empleado, Encomienda, HistorialEstado
from .serializers import EmpleadoSerializer, EncomiendaSerializer, HistorialEstadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class EncomiendaViewSet(viewsets.ModelViewSet):
    queryset = Encomienda.objects.all()
    serializer_class = EncomiendaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['codigo', 'descripcion']
    ordering_fields = ['fecha_registro', 'costo_envio']

    @action(detail=True, methods=['post'])
    def cambiar_estado(self, request, pk=None):
        encomienda = self.get_object()
        nuevo_estado = request.data.get('estado')
        empleado_id = request.data.get('empleado')
        observacion = request.data.get('observacion', "")

        if not nuevo_estado or not empleado_id:
            return Response(
                {"error": "Estado y empleado son requeridos."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            empleado = Empleado.objects.get(pk=empleado_id)
            encomienda.cambiar_estado(nuevo_estado, empleado, observacion)
            return Response({"status": "Estado actualizado correctamente."})
        except Empleado.DoesNotExist:
            return Response({"error": "Empleado no encontrado."}, status=status.HTTP_404_NOT_FOUND)

class HistorialEstadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistorialEstado.objects.all()
    serializer_class = HistorialEstadoSerializer
