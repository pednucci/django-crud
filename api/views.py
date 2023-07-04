from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_tarefas(request):
    tarefas = Tarefa.objects.all()
    serializer = TarefaSerializer(tarefas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_one_tarefa(request, pk):
    try:
        tarefa = Tarefa.objects.get(pk=pk)
    except Tarefa.DoesNotExist:
        return Response({'error': 'Tarefa não encontrada.'}, status=404)
    serializer = TarefaSerializer(tarefa)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_tarefa(request):
    serializer = TarefaSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as e:
        return Response({'error': str(e)}, status=400)
    
    serializer.save()
    return Response(serializer.data, status=201)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_tarefa(request, pk):
    try:
        tarefa = Tarefa.objects.get(pk=pk)
    except Tarefa.DoesNotExist:
        return Response({'error': 'Tarefa não encontrada.'}, status=404)

    serializer = TarefaSerializer(tarefa, data=request.data, partial=True)
    try:
        serializer.is_valid(raise_exception=True)
    except ValidationError as e:
        return Response({'error': str(e)}, status=400)

    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_tarefa(request, pk):
    try:
        tarefa = Tarefa.objects.get(pk=pk)
    except Tarefa.DoesNotExist:
        return Response({'error': 'Tarefa não encontrada.'}, status=404)

    tarefa.delete()
    return Response(status=204)

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'Informe um nome de usuário e senha.'}, status=400)
    
    try:
        user = User.objects.create_user(username=username, password=password)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
    
    refresh = RefreshToken.for_user(user)
    tokens = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
    return Response(tokens, status=201)