import uuid
from django.db import models


class GrupoArticulo(models.Model):
    grupo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_grupo = models.CharField(max_length=100)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre_grupo


class LineaArticulo(models.Model):
    linea_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_linea = models.CharField(max_length=100)
    grupo = models.ForeignKey(GrupoArticulo, on_delete=models.CASCADE)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre_linea


class ListaPrecio(models.Model):
    articulo = models.OneToOneField('Articulo', on_delete=models.CASCADE)
    precio_1 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_2 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_3 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_4 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Precios de {self.articulo.descripcion}"


class Articulo(models.Model):
    articulo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_articulo = models.CharField(max_length=50, unique=True)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    presentacion = models.CharField(max_length=100, blank=True, null=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grupo = models.ForeignKey(GrupoArticulo, on_delete=models.CASCADE)
    linea = models.ForeignKey(LineaArticulo, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion
