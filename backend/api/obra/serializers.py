from rest_framework import serializers
from drf_extra_fields.fields import HybridImageField
from .models import (
    Estilo,
    Tecnica,
    Obra,
    Foto
)


class EstiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estilo
        fields = '__all__'


class TecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnica
        fields = '__all__'


class FotoSerializer(serializers.ModelSerializer):
    foto = HybridImageField(
        max_length=None,
        required=True,
        allow_null=False,
        represent_in_base64=True
    )

    class Meta:
        model = Foto
        fields = '__all__'


class ObraSerializer(serializers.ModelSerializer):
    fotos = FotoSerializer(many=True, read_only=True, source='foto_set')

    class Meta:
        model = Obra
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['estilo_text'] = instance.estilo.descripcion
        representation['tecnica_text'] = instance.tecnica.descripcion

        return representation
