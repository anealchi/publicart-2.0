from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CompraViewSet
)


patata = DefaultRouter()
patata.register(
    r"transacciones/compras",
    CompraViewSet,
    basename='compras')

urlpatterns = [
    path('', include(patata.urls))
]
