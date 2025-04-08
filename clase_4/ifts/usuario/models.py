from django.db import models


class Usuario(models.Model):
    email = models.EmailField()
    