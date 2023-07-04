from rest_framework import serializers
from .models import Tarefa
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'prazo', 'finalizado', 'id']