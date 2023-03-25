from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=180)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.titulo}"

 