from rest_framework import viewsets
from .models import (
    Seguimiento,
    Chat,
    Mensaje
)
from .serializers import (
    SeguimientoSerializer,
    ChatSerializer,
    MensajeSerializer
)


class SeguimientoViewSet(viewsets.ModelViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
