from django.db import models


class Estilo(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descripcion}"

    class Meta:
        verbose_name_plural = 'Estilos'


class Tecnica(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descripcion}"

    class Meta:
        verbose_name_plural = 'Técnicas'


class Obra(models.Model):
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    disponible = models.BooleanField(default=False)
    estilo = models.ForeignKey(
        Estilo,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    tecnica = models.ForeignKey(
        Tecnica,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.descripcion}"

    class Meta:
        verbose_name_plural = 'Obras'


class Foto(models.Model):
    foto = models.ImageField(
        upload_to='imgs/fotos/',
        max_length=255,
        blank=False,
        null=False
    )
    obra = models.ForeignKey(
        Obra,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.obra.descripcion} - {self.foto}"

    class Meta:
        verbose_name_plural = 'Fotos'
