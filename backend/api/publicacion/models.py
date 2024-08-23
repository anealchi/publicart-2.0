from django.utils import timezone
from django.db import models
from obra.models import Obra
from authentication.models import Perfil


class Publicacion(models.Model):
    obra = models.ForeignKey(
        Obra,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.obra.descripcion} - {self.perfil.usuario.username}"

    class Meta:
        verbose_name_plural = 'Publicaciones'


class Like(models.Model):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    fecha_like = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"a {self.perfil} le ha gustado {self.publicacion}"

    class Meta:
        verbose_name_plural = 'Likes'


class Comentario(models.Model):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )
    texto = models.CharField(max_length=255)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.publicacion} - {self.perfil}"

    class Meta:
        verbose_name_plural = 'Comentarios'
