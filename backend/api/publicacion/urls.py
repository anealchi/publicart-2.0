from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PublicacionViewSet,
    LikeViewSet,
    ComentarioViewSet
)


router = DefaultRouter()
router.register(
    r'publicaciones/publicaciones',
    PublicacionViewSet,
    basename='publicaciones')
router.register(
    r'publicaciones/likes',
    LikeViewSet,
    basename='likes')
router.register(
    r'publicaciones/comentarios',
    ComentarioViewSet,
    basename='comentarios')

urlpatterns = [
    path('', include(router.urls))
]
