# Generated by Django 5.1.2 on 2024-11-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_extraperfil_profesion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraperfil',
            name='profesion',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
