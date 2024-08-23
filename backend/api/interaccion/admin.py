from django.contrib import admin
from .models import (
    Seguimiento,
    Chat,
    Mensaje
)

admin.site.register(Seguimiento)
admin.site.register(Chat)
admin.site.register(Mensaje)
