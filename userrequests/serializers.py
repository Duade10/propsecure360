from rest_framework import serializers
from . import models

class UserRequestCreateSerializer(serializers.Serializer):
    title = serializers.CharField(write_only=True, required=True)
    description = serializers.CharField(write_only=True)
    location_of_property = serializers.CharField(write_only=True)
    document_type = serializers.CharField(write_only=True)
    document = serializers.CharField(write_only=True)

    def save(self, validated_data):
        request = self.context["request"]
        
        user = request.user
        user_request = models.UserRequest.objects.create(
            title=validated_data["title"],
            description=validated_data.get("description", ""),
            location_of_property=validated_data["location_of_property"],
            document_type=validated_data["document_type"],
            document=validated_data["document"],
            user=user,
        )

        return user_request


class UserRequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRequest
        fields = ["id", "title", "description", "location_of_property", "document_type", "document"]
