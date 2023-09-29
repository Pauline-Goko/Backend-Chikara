from django.contrib import admin
from .models import Vehicle

# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('engine_type', 'year', 'vehicle_model','chassis_number')
    
    
admin.site.register(Vehicle, VehicleAdmin)

    
