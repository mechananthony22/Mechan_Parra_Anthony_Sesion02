from django.db import models

class EstadoEntidades(models.IntegerChoices):
    ACTIVO = 1, 'Activo'
    INACTIVO = 0, 'Inactivo'

class EstadoGeneral(models.IntegerChoices):
    ACTIVO = 1, 'Activo'
    INACTIVO = 0, 'Inactivo'

class EstadoEnvio(models.TextChoices):
    PENDIENTE = 'PE', 'Pendiente'
    EN_TRANSITO = 'ET', 'En Tránsito'
    EN_REPARTO = 'ER', 'En Reparto'
    ENTREGADO = 'EN', 'Entregado'
    CANCELADO = 'CA', 'Cancelado'
    DEVUELTO = 'DE', 'Devuelto'

class TipoDocumento(models.TextChoices):
    DNI = 'DNI', 'DNI'
    CE = 'CE', 'Carnet de Extranjería'
    RUC = 'RUC', 'RUC'

class MetodoPago(models.TextChoices):
    EFECTIVO = 'EF', 'Efectivo'
    TARJETA = 'TA', 'Tarjeta'
    TRANSFERENCIA = 'TR', 'Transferencia'
    YAPE = 'YP', 'Yape'
    PLIN = 'PL', 'Plin'

class EstadoPago(models.TextChoices):
    PENDIENTE = 'PE', 'Pendiente'
    PAGADO = 'PA', 'Pagado'
    ANULADO = 'AN', 'Anulado'
