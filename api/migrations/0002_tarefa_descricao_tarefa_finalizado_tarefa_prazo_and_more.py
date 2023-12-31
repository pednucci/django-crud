# Generated by Django 4.2.3 on 2023-07-04 02:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='descricao',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='prazo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
