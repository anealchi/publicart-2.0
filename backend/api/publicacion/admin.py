from django.contrib import admin
from .models import (
    Publicacion,
    Like,
    Comentario
)

admin.site.register(Publicacion)
admin.site.register(Like)
admin.site.register(Comentario)
