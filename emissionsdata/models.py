from django.db import models
from vehicles.models import Vehicle
from decimal import Decimal


class EmissionsData(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    emission_value = models.DecimalField(decimal_places=2, max_digits=14, null=True)
    date_created = models.DateTimeField(auto_now=True)

    def convert_emissions(self):
        converted_emissions = (Decimal('44.01') * Decimal(str(self.emission_value))) / Decimal('24.45')
        gas_equivalent = converted_emissions / Decimal('1000000')
        return gas_equivalent
    
    def save(self, *args, **kwargs):
        self.emission_value = self.convert_emissions()
        super().save(*args, **kwargs)

    