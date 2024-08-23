from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PerfilViewSet, UsuarioViewSet


router = DefaultRouter()
router.register(
    r'auth/perfiles',
    PerfilViewSet,
    basename='perfiles')
router.register(
    r'auth/usuarios',
    UsuarioViewSet,
    basename='usuarios')

urlpatterns = [
    path('', include(router.urls))
]
