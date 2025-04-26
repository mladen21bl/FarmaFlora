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


from django.db import models

from django.db import models

class ActiveCompound(models.Model):
    plant = models.ForeignKey(
        'Plant',
        on_delete=models.CASCADE,
        related_name="active_compounds"
    )
    name = models.CharField(max_length=100, verbose_name="Naziv supstance")
    mol_file = models.FileField(upload_to='molecules/', verbose_name="MOL fajl")
    description = models.TextField(blank=True, verbose_name="Opis supstance")

    molecular_formula = models.CharField(
        max_length=50,
        verbose_name="Molekulska formula",
        blank=True
    )
    solubility = models.TextField(
        verbose_name="Rastvorljivost",
        blank=True,
        help_text="Unesite detaljan opis rastvorljivosti supstance, npr. u vodi, mastima, alkoholu, itd."
    )
    structure_class = models.TextField(
        verbose_name="Strukturna klasa",
        blank=True,
        help_text="Unesite detaljan opis strukturne klase supstance."
    )
    log_p = models.FloatField(
        verbose_name="Log P",
        blank=True,
        null=True,
        help_text="Unesite vrednost Log P (može biti decimalni broj)."
    )
    iupac_name = models.CharField(
        max_length=255,
        verbose_name="IUPAC naziv",
        blank=True,
        help_text="Unesite IUPAC naziv supstance."
    )

    class Meta:
        verbose_name = "Aktivna supstanca"
        verbose_name_plural = "Aktivne supstance"

    def __str__(self):
        return f"{self.name} ({self.plant.name})"
