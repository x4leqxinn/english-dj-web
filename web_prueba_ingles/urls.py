from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
    path('set-photo/', set_photo, name='set-photo'),
    path('send-message/', send_message, name='send-message'),
]

# Configuración para servir archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)