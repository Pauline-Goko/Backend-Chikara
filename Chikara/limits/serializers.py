from rest_framework import serializers
from limits.models import EmissionCap


class EmissionCapSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmissionCap
        fields = "__all__"