# Generated by Django 5.1.5 on 2025-01-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_boleta_remove_usuario_contraseña_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
