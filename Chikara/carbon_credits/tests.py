# tests.py
from django.test import TestCase
from .models import CarbonCredits
from emmisions.models import EmissionData
from limits.models import Limit

class CarbonCreditsTestCase(TestCase):
    def setUp(self):
        
        self.emission_data = EmissionData.objects.create(
            CO2_emissions=100.0  
        )

        
        self.emission_limit = Limit.objects.create(
            emission_limit=150.0  
        )

       
        self.carbon_credits = CarbonCredits.objects.create(
            emission_data=self.emission_data,
            emission_limit=self.emission_limit,
            credit_earned=0.0  
        )