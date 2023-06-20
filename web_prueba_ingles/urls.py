from .views import *
from django.urls import path

urlpatterns = [
    path('', index,name='index'),
    path('crearCuenta/',crearCuenta,name='Crear cuenta.html'),
    path('dondeEstamos/',dondeEstamos,name='Donde Estamos.html'),
    path('formularioDeContacto/',formularioDeContacto,name='Formulario de contacto.html'),
    path('iniciarSesion/',iniciarSesion,name='Iniciar Sesion.html'),
    path('quienesSomos/',quienesSomos,name='Quienes somos.html'),
    path('trabajosRealizados/',trabajosRealizados,name='Trabajos realizados.html'),
    path('usuario/',usuario,name='Usuario.html'),
    path('registrarse/',registrarse, name='registrarse'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', cerrar_sesion, name='logout'),
    path('set-locale/<str:language_code>/', set_language, name='set-language'),
]