from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from .models import User

def index(request):
    return render(request, 'Index.html')


def crearCuenta(request):
    return render(request, 'Crear cuenta.html')


def dondeEstamos(request):
    return render(request, 'Donde Estamos.html')


def formularioDeContacto(request):
    return render(request, 'Formulario de contacto.html')


def iniciarSesion(request):
    return render(request, 'Iniciar Sesion.html')


def quienesSomos(request):
    return render(request, 'Quienes somos.html')


def trabajosRealizados(request):
    return render(request, 'Trabajos realizados.html')


def usuario(request):
    return render(request, 'Usuario.html')


def registrarse(request):
    contexto = {"mensaje": ""}
    if request.method == 'POST':
        usuario = request.POST.get("user")
        correo = request.POST.get("email")
        passw = request.POST.get("password")
        confirm_passw = request.POST.get("confirm-password")

        if passw != confirm_passw:
            contexto = {"mensaje": "Las contraseñas no coinciden"}
            return render(request, 'Crear cuenta.html', contexto)

        if User.objects.filter(email=correo).exists():
            contexto = {"mensaje": "El usuario ya se encuentra registrado"}
            return render(request, 'Crear cuenta.html', contexto)

        nuevo_usuario = User(username=usuario, email=correo, password=make_password(passw),is_staff= False)
        nuevo_usuario.save()
        contexto = {"mensaje": "Se creó la cuenta correctamente"}

    return render(request, 'Crear cuenta.html', contexto)





@login_required
def obtener_usuario(request):
    usuario = request.user
    return usuario


def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = User.objects.get(email=email)
            if check_password(password, usuario.password):
                return render(request, 'Index.html')
            else:
                mensaje = 'Credenciales inválidas. Inténtalo de nuevo.'
        except User.DoesNotExist:
            mensaje = 'Credenciales inválidas. Inténtalo de nuevo.'
    else:
        mensaje = ''

    return render(request, 'Iniciar Sesion.html', {'mensaje': mensaje})


def cerrar_sesion(request):
    logout(request)
    return redirect('index')
