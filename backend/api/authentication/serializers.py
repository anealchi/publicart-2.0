from rest_framework import serializers
from drf_extra_fields.fields import HybridImageField
from .models import Perfil, Usuario
from interaccion.models import Seguimiento


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_superuser',
            'is_active',
            'password',
            'perfil'
        ]
        extra_kwargs = {'password': {'write_only': True}}
        depth = 1

    def create(self, validated_data):
        usuario = Usuario(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario


class PerfilSerializer(serializers.ModelSerializer):
    foto = HybridImageField(
        max_length=None,
        required=False,
        allow_null=True,
        represent_in_base64=True
    )

    num_seguidores = serializers.SerializerMethodField()
    num_seguidos = serializers.SerializerMethodField()

    class Meta:
        model = Perfil
        fields = '__all__'

    def get_num_seguidores(self, obj):
        return Seguimiento.objects.filter(seguido=obj).count()

    def get_num_seguidos(self, obj):
        return Seguimiento.objects.filter(seguidor=obj).count()
