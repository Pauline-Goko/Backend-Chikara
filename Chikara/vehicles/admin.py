from django.contrib import admin
from .models import Vehicle

# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('number_plate', 'engine_type')
    
    
admin.site.register(Vehicle, VehicleAdmin)

    
