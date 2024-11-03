from django.urls import path
from inicio import views



urlpatterns = [
    path ('', views.inicio, name= 'index'),
    path('crear-zapa', views.CrearZapa.as_view(), name='crear-zapa'),
    path('success', views.crear_success, name='crear_success'),
    path('buscar-zapa', views.buscar_zapa, name='buscar-zapa'),
    path('about', views.about, name='about'),
    path('ver-zapa/<int:id>', views.ver_zapa, name='ver-zapa'),
    path('eliminar-zapa/<int:id>', views.eliminar_zapa, name='eliminar-zapa'),
    path('<int:pk>/editar-zapa', views.EditarZapa.as_view(), name='editar-zapa')

]
