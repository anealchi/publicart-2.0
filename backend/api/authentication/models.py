from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name"]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    class Meta:
        db_table = 'usuario'


class Perfil(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.PROTECT,
        related_name='perfil',
        blank=False,
        null=True
    )
    biografia = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    foto = models.ImageField(
        upload_to='img/perfil',
        max_length=250,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.usuario.username}"

    class Meta:
        verbose_name_plural = 'Perfiles'
