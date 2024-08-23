from rest_framework import viewsets
from .models import Perfil, Usuario
from .serializers import PerfilSerializer, UsuarioSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
