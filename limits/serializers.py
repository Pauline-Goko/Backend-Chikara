from rest_framework import serializers
from .models import Limit


class LimitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Limit
        fields = "__all__"
