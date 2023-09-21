from django.db import models

class CarbonCredits(models.Model):
    # emission_data = models.OneToOneField(EmissionData, on_delete=models.CASCADE)
    # emission_limit = models.OneToOneField(EmissionLimit, on_delete=models.CASCADE)
    credit_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def calculate_credits_earned(self):

        total_emissions = self.emission_data.CO2_emissions
        total_limit=self.emission_limit.CO2_emissions
        total_carbon=total_limit-total_emissions
        self.credit_earned = total_carbon / 1000
        self.save()

    def __str__(self):
        return f"Carbon Credits for {self.emission_data.vehicle_id}"