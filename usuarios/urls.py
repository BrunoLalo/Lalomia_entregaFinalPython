from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/pass', views.CambiarPass.as_view(), name='cambiar-pass'),
    path('perfil', views.ver_perfil, name='ver-perfil')

]
