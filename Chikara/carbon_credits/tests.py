# # tests.py
# from django.test import TestCase
# from .models import CarbonCredits
# # from emmisions.models import EmissionData
# # from trucks_api.models import EmissionLimit

# class CarbonCreditsTestCase(TestCase):
#     def setUp(self):
#         # Create a sample EmissionData instance
#         self.emission_data = EmissionData.objects.create(
#             CO2_emissions=100.0  # You can set the emissions value as needed
#         )

#         # Create a sample EmissionLimit instance
#         self.emission_limit = EmissionLimit.objects.create(
#             emission_limit=150.0  # You can set the limit value as needed
#         )

#         # Create a CarbonCredits instance with the above data
#         self.carbon_credits = CarbonCredits.objects.create(
#             emission_data=self.emission_data,
#             emission_limit=self.emission_limit,
#             credit_earned=0.0  # Set an initial value for credit_earned if needed
#         )