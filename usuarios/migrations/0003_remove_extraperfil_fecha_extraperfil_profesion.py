# Generated by Django 5.1.2 on 2024-11-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_extraperfil_fecha_alter_extraperfil_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extraperfil',
            name='fecha',
        ),
        migrations.AddField(
            model_name='extraperfil',
            name='profesion',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
