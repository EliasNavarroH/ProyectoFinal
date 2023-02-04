from django.db import models

# Create your models here.
class EntradaDeBlog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=500)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='blog_images/', blank=True)

    def __str__(self):
        return self.titulo