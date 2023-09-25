# serializers.py
# from rest_framework import serializers
from rest_framework import serializers
from .models import CarbonCredits

class CarbonCreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonCredits
        fields = ('id', 'emission_data', 'emission_limit', 'credit_earned')
