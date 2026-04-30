from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    perfil_nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.perfil_nombre

class Usuario(User):
    class Meta:
        proxy = True
        verbose_name = 'Usuario POS'

    @property
    def full_name(self):
        return self.get_full_name() or self.username

    @property
    def mobile(self):
        return getattr(self, '_mobile', '')
