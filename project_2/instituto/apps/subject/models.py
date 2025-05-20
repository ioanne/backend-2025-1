from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)  # Campos
    description = models.TextField()
    credits = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    career = models.ForeignKey(
        'career.Career', on_delete=models.CASCADE, related_name='subjects'
    )

    def __str__(self):
        return self.name
