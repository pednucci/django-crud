from django.db import models
import uuid

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.TextField(null=True, blank=True)
    prazo = models.DateField(null=True, blank=True)
    finalizado = models.BooleanField(null=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)