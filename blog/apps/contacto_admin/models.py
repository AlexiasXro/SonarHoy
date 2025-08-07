from django.db import models

class Contacto(models.Model):
    TIPOS_CONSULTA = [
        ('agradecimiento', 'Agradecimiento'),
        ('reclamo', 'Reclamo'),
        ('opinion', 'Opinión libre'),
        ('bloqueado', 'Usuario bloqueado'),
        ('colaborador', 'Quiero ser colaborador'),
        ('reporte', 'Reporte de usuario'),
    ]

    nombre_apellido = models.CharField(max_length=100)
    es_usuario = models.BooleanField(default=False)
    correo = models.EmailField()
    tipo_consulta = models.CharField(max_length=20, choices=TIPOS_CONSULTA)
    mensaje = models.TextField(max_length=400)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre_apellido} - {self.tipo_consulta}'
