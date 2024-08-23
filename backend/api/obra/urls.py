from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    EstiloViewSet,
    TecnicaViewSet,
    ObraViewSet,
    FotoViewSet
)


router = DefaultRouter()
router.register(
    r'obras/estilos',
    EstiloViewSet,
    basename='estilos')
router.register(
    r'obras/tecnicas',
    TecnicaViewSet,
    basename='tecnicas')
router.register(
    r'obras/obras',
    ObraViewSet,
    basename='obras')
router.register(
    r'obras/fotos',
    FotoViewSet,
    basename='fotos')

urlpatterns = [
    path('', include(router.urls))
]
