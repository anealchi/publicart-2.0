from rest_framework import viewsets

from .models import (
    Estilo,
    Tecnica,
    Obra,
    Foto
)
from .serializers import (
    EstiloSerializer,
    TecnicaSerializer,
    ObraSerializer,
    FotoSerializer
)


class EstiloViewSet(viewsets.ModelViewSet):
    queryset = Estilo.objects.all()
    serializer_class = EstiloSerializer


class TecnicaViewSet(viewsets.ModelViewSet):
    queryset = Tecnica.objects.all()
    serializer_class = TecnicaSerializer


class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer


class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
