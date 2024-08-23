from rest_framework import serializers
from .models import (
    Publicacion,
    Like,
    Comentario
)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PublicacionSerializer(serializers.ModelSerializer):
    num_likes = serializers.SerializerMethodField()

    class Meta:
        model = Publicacion
        fields = '__all__'
        extra_field = ['num_likes']

    def get_num_likes(self, obj):
        return Like.objects.filter(publicacion=obj).count()


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
