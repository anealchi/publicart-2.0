from rest_framework import serializers
from .models import (
    Seguimiento,
    Chat,
    Mensaje
)


class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = '__all__'


class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'

    def validate(self, attrs):
        chat = attrs['chat']
        autor = attrs['autor']

        if chat.difusion and autor != chat.creador:
            raise serializers.ValidationError('Solo el creador del grupo de difusión puede enviar mensaje')

        return attrs


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

    def validate_participantes(self, value):
        if len(value):
            raise serializers.ValidationError('Un chat debe tener al menos dos participantes')
        return value
