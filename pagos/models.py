from django.db import models
from config.choices import MetodoPago, EstadoPago
from envios.models import Encomienda


class Pago(models.Model):
    encomienda = models.OneToOneField(
        Encomienda, on_delete=models.CASCADE,
        related_name='pago'
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(
        max_length=2,
        choices=MetodoPago.choices,
        default=MetodoPago.EFECTIVO
    )
    referencia = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(
        max_length=2,
        choices=EstadoPago.choices,
        default=EstadoPago.PENDIENTE
    )
    comprobante = models.CharField(max_length=50, blank=True, null=True)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pago {self.id} - {self.encomienda.codigo} - {self.monto}'

    class Meta:
        db_table = 'pagos'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['-fecha_pago']