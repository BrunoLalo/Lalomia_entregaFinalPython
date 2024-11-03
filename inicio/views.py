from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Zapatilla
from .forms import CrearZapasForm, BuscarZapasForm, EditarZapasForm

def inicio (request):
    return render(request, 'index.html')


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


def ver_zapa(request, id):
    zapa = Zapatilla.objects.get(id=id) 
    return render(request, 'verZapa.html', {'zapa': zapa})

@login_required
def eliminar_zapa(request, id):
    zapa = Zapatilla.objects.get(id=id) 
    zapa.delete()
    return redirect('buscar-zapa')

class CrearZapa (LoginRequiredMixin, CreateView): 
    model = Zapatilla        
    template_name = 'crearZapa.html'
    success_url= reverse_lazy('crear_success')
    fields = ['marca', 'color', 'talle', 'precio', 'fecha', 'imagen'] 
    
class EditarZapa(LoginRequiredMixin, UpdateView):
    model = Zapatilla
    template_name = "editarZapa.html"
    success_url = reverse_lazy("buscar-zapa")
    fields = ['marca', 'color', 'talle', 'precio', 'fecha', 'imagen'] 


# def crear_zapa(request):
#     formulario = CrearZapasForm()
    
#     if request.method == 'POST':
#         formulario = CrearZapasForm(request.POST)
#         if formulario.is_valid():
#             data = formulario.cleaned_data
#             zapatilla = Zapatilla(marca=data.get('marca'), color=data.get('color'), talle=data.get('talle'), precio=data.get('precio'), fecha=data.get('fecha') )
#             zapatilla.save()
#             return redirect('crear_success')
        
#     return render(request, 'crearZapa.html', {'form': formulario})

# def editar_zapa(request, id):
#     zapa = Zapatilla.objects.get(id = id) 
    
#     formulario = EditarZapasForm(initial={'marca': zapa.marca, 'color': zapa.color, 'talle': zapa.talle, 'precio': zapa.precio, 'fecha': zapa.fecha})
    
#     if request.method == "POST":
#         if formulario.is_valid():
#             zapa.marca = formulario.cleaned_data.get('marca'), 
#             zapa.color = formulario.cleaned_data.get('color'), 
#             zapa.talle = formulario.cleaned_data.get('talle'), 
#             zapa.precio = formulario.cleaned_data.get('precio'),
#             zapa.fecha = formulario.cleaned_data.get('fecha')
            
            
#             zapa.save()
            
#             return redirect('buscar-zapa')
    
#     return render(request, 'editarZapa.html', {'zapa': zapa, 'form': formulario})




            

