# Generated by Django 5.1.1 on 2024-11-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Projetos2', '0002_doacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]
