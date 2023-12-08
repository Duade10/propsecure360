from rest_framework import serializers
from django.contrib.auth import authenticate
from . import models


class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(write_only=True, required=True)
    phone_number = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    def save(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_active=True
        )
        return user



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "email", "first_name", "last_name", "phone_number", "password", "is_active"]
