from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','usuario', 'nome', 'senha', 'confirmesenha')
        model = models.Usuario
