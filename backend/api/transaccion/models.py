from django.db import models
from authentication.models import Perfil
from obra.models import Obra


class Compra(models.Model):
    comprador = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    obra = models.ForeignKey(
        Obra,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.obra} - {self.comprador}"

    class Meta:
        verbose_name_plural = 'Compras'
