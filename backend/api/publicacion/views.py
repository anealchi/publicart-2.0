from rest_framework import viewsets
from .models import (
    Publicacion,
    Like,
    Comentario
)
from .serializers import (
    PublicacionSerializer,
    LikeSerializer,
    ComentarioSerializer
)


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
