from django.contrib import admin
from .models import EmissionCap

# Register your models here.


class EmissionCapAdmin(admin.ModelAdmin):
    list_display = ("emission_limit", "duration")
  
 

admin.site.register(EmissionCap, EmissionCapAdmin)