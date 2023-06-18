# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Contacto(models.Model):
    nombre = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=600)

    def str(self):
        return self.nombre

class Usuario(models.Model):
    usuario = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=600)  # Puedes usar CharField para la contraseña
    
    def __str__(self):
        return self.usuario

