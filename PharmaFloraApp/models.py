from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    geojson = models.FileField(upload_to='regions_geojson/')

    def __str__(self):
        return self.name


class Plant(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Naziv")
    latin_name = models.CharField(max_length=100, unique=True, verbose_name="Latinski naziv")
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True, verbose_name="Slika")
    description = models.TextField(verbose_name="Opis")
    drug = models.CharField(max_length=200, verbose_name="Droga")
    indications = models.TextField(verbose_name="Indikacije")
    regions = models.ManyToManyField(Region, blank=True, related_name='plants')

    class Meta:
        verbose_name = "Biljka"
        verbose_name_plural = "Biljke"
        ordering = ['name']

    def __str__(self):
        return self.name
