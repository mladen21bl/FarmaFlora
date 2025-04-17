from django.contrib import admin
from .models import Plant, Region, ActiveCompound

admin.site.register(Plant)
admin.site.register(Region)

@admin.register(ActiveCompound)
class ActiveCompoundAdmin(admin.ModelAdmin):
    list_display = ("name", "plant")
