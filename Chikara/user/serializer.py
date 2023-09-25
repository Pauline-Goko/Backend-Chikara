from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", 'username', 'email', 'phone_number', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        confirm_password = validated_data.pop('confirm_password', None)
        if confirm_password and validated_data['password'] != confirm_password:
            raise serializers.ValidationError("Passwords do not match")
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
