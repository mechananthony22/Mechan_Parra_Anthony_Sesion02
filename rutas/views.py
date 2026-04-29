from rest_framework import viewsets, filters
from .models import Ruta
from .serializers import RutaSerializer

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['codigo', 'origen', 'destino']
    ordering_fields = ['precio_base', 'dias_entrega']
