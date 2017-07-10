from django.db import models

class Format(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    imagen = models.ImageField(blank=True)
    artista = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    formato = models.ForeignKey(Format, on_delete = models.CASCADE)
    precio = models.IntegerField()
    apartado = models.BooleanField(default=False)
    vendido = models.BooleanField(default=False)
    info = models.TextField(blank=True)

    def __str__(self):
        return "%s. %s - %s (Precio: ¢%s / Apartado: %s / Vendido: %s)" % (self.id, self.artista, self.nombre, self.precio, self.apartado, self.vendido)
    
