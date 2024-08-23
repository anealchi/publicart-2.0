from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SeguimientoViewSet,
    ChatViewSet,
    MensajeViewSet
)


router = DefaultRouter()
router.register(
    r'interacciones/seguimientos',
    SeguimientoViewSet,
    basename='seguimientos')
router.register(
    r'interacciones/chats',
    ChatViewSet,
    basename='chats')
router.register(
    r'interacciones/mensajes',
    MensajeViewSet,
    basename='mensajes')

urlpatterns = [
    path('', include(router.urls))
]
