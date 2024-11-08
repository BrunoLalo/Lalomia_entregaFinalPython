from django.db import models
from django.contrib.auth.models import User

class ExtraPerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    profesion = models.CharField(max_length=30) 