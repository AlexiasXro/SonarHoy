from django.db import models

class Integrante(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    foto = models.ImageField(upload_to='integrantes/', blank=True, null=True)

    def __str__(self):
        return self.nombre
