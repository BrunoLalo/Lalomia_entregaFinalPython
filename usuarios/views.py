from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


from usuarios.forms import RegisterForm, EditarPerfilForm
from usuarios.models import ExtraPerfil


def login (req) :
    
    formulario = AuthenticationForm()
    
    if req.method == 'POST':
        formulario = AuthenticationForm(req, data = req.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            user = authenticate(username= usuario, password=password)
            
            django_login(req, user)
            
            ExtraPerfil.objects.get_or_create(user=user)
            
            return redirect ('index')
                
    return render(req, 'usuarios/login.html', {'form': formulario})

def register(req):
    
    formulario=RegisterForm()
    
    if req.method == 'POST':
        formulario = RegisterForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('usuarios:login')
    
    return render(req, 'usuarios/register.html', {'form': formulario})

@login_required
def editar_perfil(req):
    datos_extra = req.user.extraperfil 
    formulario= EditarPerfilForm(instance = req.user, initial={'profesion':datos_extra.profesion})
    
    if req.method == 'POST':
        formulario = EditarPerfilForm(req.POST, req.FILES, instance = req.user)
        if formulario.is_valid():
            new_avatar = formulario.cleaned_data.get('avatar')
            new_profesion = formulario.cleaned_data.get('profesion')
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar
            datos_extra.profesion = new_profesion if new_profesion else datos_extra.profesion
            
            datos_extra.save()
            
            formulario.save()
            
            return redirect('index')
        
    return render(req, 'usuarios/editarPerfil.html', {'form': formulario})

    
class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiarPass.html'
    success_url = reverse_lazy("index")
    
@login_required
def ver_perfil(req):
    return render(req, 'usuarios/verPerfil.html')