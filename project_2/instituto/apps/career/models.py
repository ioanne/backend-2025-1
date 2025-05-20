from django.db import models


class Career(models.Model): # Tabla
    name = models.CharField(max_length=100) # Campos
    description = models.TextField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
