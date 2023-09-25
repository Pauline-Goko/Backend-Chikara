from rest_framework import serializers
from .models import EmissionsData

class EmissionsDataSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EmissionsData
        fields = "__all__"