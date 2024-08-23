from django.db import models
from authentication.models import Perfil


class Seguimiento(models.Model):
    seguidor = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='seguidores'
    )
    seguido = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='seguidos'
    )
    fecha_seguimiento = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.seguidor} sigue a {self.seguido}"

    class Meta:
        verbose_name_plural = 'Seguimientos'
        unique_together = ('seguidor', 'seguido')


class Chat(models.Model):
    perfil1 = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='chats1'
    )
    perfil2 = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='chats2'
    )

    def __str__(self) -> str:
        return f"{self.perfil1} - {self.perfil2}"

    class Meta:
        verbose_name_plural = 'Chats'


class Mensaje(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    autor = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    texto = models.CharField(max_length=500)
    fecha_mensaje = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.autor}: {self.texto}"

    class Meta:
        verbose_name_plural = 'Mensajes'
