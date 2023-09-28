from rest_framework import serializers
from user.models import User
from django.contrib.auth.models import Group,Permission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","description", 'username', 'location', 'email', 'phone_number','password']
        extra_kwargs = {'password': {'write_only': True}}


class LogoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['image',]

class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['home_image',]