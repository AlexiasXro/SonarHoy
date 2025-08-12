from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    localidad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['fecha']

    def __str__(self):
        return f"{self.titulo} - {self.fecha.strftime('%d/%m/%Y')}"

