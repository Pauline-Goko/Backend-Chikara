from django.db import models
from emissionsdata.models import EmissionsData
from limits.models import Limit


class CarbonCredits(models.Model):
    emission_data = models.OneToOneField(EmissionsData, on_delete=models.CASCADE)
    emission_limit = models.OneToOneField(Limit, on_delete=models.CASCADE, null=True)
    credit_earned = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  

    def calculate_credits_earned(self):
        total_emissions = self.emission_data.emission_value
        total_limit = self.emission_limit.emission_limit if self.emission_limit else 0
        total_carbon_credit = total_limit - total_emissions
        return total_carbon_credit

    def save(self, *args, **kwargs):
        self.credit_earned = self.calculate_credits_earned()
        super().save(*args, **kwargs)
