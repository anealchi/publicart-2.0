from django.contrib import admin
from .models import (
    Estilo,
    Tecnica,
    Obra,
    Foto
)

admin.site.register(Estilo)
admin.site.register(Tecnica)
admin.site.register(Obra)
admin.site.register(Foto)