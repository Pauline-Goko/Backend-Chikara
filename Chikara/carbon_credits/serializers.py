# serializers.py
from rest_framework import serializers
# from .models import EmissionData, EmissionLimit, CarbonCredits
from .models import CarbonCredits




# class EmissionDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmissionData
#         fields = '__all__'

# class EmissionLimitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmissionLimit
#         fields = '__all__'

class CarbonCreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonCredits
        fields = '__all__'
