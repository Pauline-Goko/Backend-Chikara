from django.db import models


class Vehicle(models.Model):
    number_plate = models.CharField(max_length=32)
    engine_type = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return f"{self.number_plate} ({self.engine_type})"
