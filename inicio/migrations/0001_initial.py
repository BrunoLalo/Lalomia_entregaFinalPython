# Generated by Django 5.1.2 on 2024-10-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zapatilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=15)),
                ('color', models.CharField(max_length=15)),
                ('talle', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
