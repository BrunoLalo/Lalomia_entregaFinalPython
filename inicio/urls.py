from django.urls import path
from inicio.views import inicio, crear_zapa, buscar_zapa, crear_success, about


urlpatterns = [
    path ('', inicio, name= 'index'),
    path('crear-zapa', crear_zapa, name='crear-zapa'),
    path('success', crear_success, name='crear_success'),
    path('buscar-zapa', buscar_zapa, name='buscar-zapa'),
    path('about', about, name='about')
]
