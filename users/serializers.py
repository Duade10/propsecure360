from rest_framework import serializers
from django.contrib.auth import authenticate
from . import models


class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data["email"],
            
        )