from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
