from django.contrib import admin
from .models import Plant, Region, ActiveCompound

admin.site.register(Plant)
admin.site.register(Region)

@admin.register(ActiveCompound)
class ActiveCompoundAdmin(admin.ModelAdmin):
    list_display = ("name", "get_plants")  # Prikazivanje povezanih biljaka

    # Dodaj metodu koja će prikazati povezane biljke
    def get_plants(self, obj):
        return ", ".join([plant.name for plant in obj.plants.all()])
    get_plants.short_description = 'Biljke'  # Prikazivanje kao 'Biljke' u admin panelu
