# Generated by Django 5.1.7 on 2025-03-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_barras', models.CharField(max_length=100, unique=True)),
                ('nome_paciente', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('ultima_consulta', models.DateTimeField(blank=True, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
