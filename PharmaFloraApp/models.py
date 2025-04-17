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


class ActiveCompound(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="active_compounds")
    name = models.CharField(max_length=100, verbose_name="Naziv supstance")
    mol_file = models.FileField(upload_to='molecules/', verbose_name="MOL fajl")
    description = models.TextField(blank=True, verbose_name="Opis supstance")

    class Meta:
        verbose_name = "Aktivna supstanca"
        verbose_name_plural = "Aktivne supstance"

    def __str__(self):
        return f"{self.name} ({self.plant.name})"
