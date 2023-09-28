from django.db import models

class Vehicle(models.Model):
    year = models.PositiveIntegerField(null=True, blank=True)
    vehicle_model = models.CharField(max_length=32,null=True)
    chassis_number = models.CharField(max_length=32,null=True)
    engine_type = models.CharField(max_length=32,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"{self.number_plate} ({self.engine_type})"
