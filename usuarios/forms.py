from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm) :
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
        help_texts = {key:'' for key in fields }


class EditarPerfilForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    password = None
    profesion = forms.CharField(label = 'Profesion')
    avatar = forms.ImageField(required=False)
    
    
    class Meta():
        model = User
        fields = [ 'email', 'first_name', 'last_name', 'avatar']
    

