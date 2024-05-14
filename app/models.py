from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Estado = [
    ("Activo", "Activo"),
    ("Inactivo", "Inactivo")
]

class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    Activa = models.CharField(max_length=25, choices=Estado, default="Activo")
    # Dueño = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.titulo} --- {self.descripcion}"
