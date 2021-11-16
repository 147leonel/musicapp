from django.db import models

class Album(models.Model):
    nombre_album = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_album
class Music(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.TextField()
    artista = models.TextField()
    imagen_album = models.TextField()
    album = models.ForeignKey(
        Album, related_name="music", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre