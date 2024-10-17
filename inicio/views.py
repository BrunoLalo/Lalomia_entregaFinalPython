from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

from .models import Zapatilla
from .forms import CrearZapasForm, BuscarZapasForm

def inicio (request):
    return render(request, 'index.html')

def crear_zapa(request):
    formulario = CrearZapasForm()
    
    if request.method == 'POST':
        formulario = CrearZapasForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            zapatilla = Zapatilla(marca=data.get('marca'), color=data.get('color'), talle=data.get('talle'), precio=data.get('precio'))
            zapatilla.save()
            return redirect('crear_success')
        
    return render(request, 'crearZapa.html', {'form': formulario})

def crear_success(req):
        return render(req, 'crearSuccess.html')

def buscar_zapa(request):
    
    formulario = BuscarZapasForm(request.GET)

    if formulario.is_valid():
        marca = formulario.cleaned_data.get('marca')
        color = formulario.cleaned_data.get('color')
        zapatillas = Zapatilla.objects.filter(marca__icontains = marca, color__icontains = color)
    
    return render(request, 'buscarZapa.html', {'zapas': zapatillas, 'form': formulario})

def about(request):
    return render(request, 'about.html')




