from django.contrib import admin
from .models import EmissionsData
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('emission_value', 'date_created')
admin.site.register(EmissionsData,VehicleAdmin)


