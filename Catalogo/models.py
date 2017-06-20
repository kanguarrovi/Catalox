from django.db import models

class Formato(models.Model):
    imagen = models.ImageField(blank=True)
    artista = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    apartado = models.BooleanField(default=False)
    vendido = models.BooleanField(default=False)
    info = models.TextField(blank=True)

    def __str__(self):
        return "%s. %s - %s (Precio: ¢%s / Apartado: %s / Vendido: %s)" % (self.id, self.artista, self.nombre, self.precio, self.apartado, self.vendido)

    class Meta:
        abstract = True

class Vinilo(Formato):
    id = models.AutoField(primary_key=True)

class CD(Formato):
    id = models.AutoField(primary_key=True)
    
