# Generated by Django 5.1.1 on 2024-10-13 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Projetos2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_doador', models.CharField(max_length=100)),
                ('email_doador', models.EmailField(max_length=254)),
                ('telefone_doador', models.CharField(blank=True, max_length=15)),
                ('tipo_doacao', models.CharField(max_length=100)),
                ('descricao', models.TextField(help_text='Descreva o estado do brinquedo ou material têxtil')),
                ('data_doacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]