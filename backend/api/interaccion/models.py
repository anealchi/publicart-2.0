from django.core.exceptions import ValidationError
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
    nombre = models.CharField(max_length=100, blank=True)
    participantes = models.ManyToManyField(
        Perfil,
        related_name='chats'
    )
    creacion = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if self.pk and self.participantes.count() < 2:
            raise ValidationError('Un chat debe tener al menos dos participantes')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        if self.nombre:
            return self.nombre

        return f"Chat con {', '.join([str(p) for p in self.participantes.all()])}"

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
