from rest_framework import serializers
from . import models
from users.serializers import UserDetailSerializer

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
    user = UserDetailSerializer(read_only=True)
    quotations = serializers.SerializerMethodField()
    class Meta:
        model = models.UserRequest
        fields = ["id", "title", "description", "location_of_property", "document_type", "document", "user", "quotations"]

    def get_quotations(self, obj):
        quotations = obj.quotations.all()
        serializer = QuotationDetaillSerializer(quotations, many=True)
        return serializer.data
class UserRequestDetaillSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = models.UserRequest
        fields = ["id", "title", "description", "location_of_property", "document_type", "document", "user"]


class QuotationCreateSerializer(serializers.Serializer):
    user_request_id = serializers.CharField(write_only=True, required=True)
    description = serializers.CharField(write_only=True, required=False)
    price = serializers.FloatField(write_only=True)
    status = serializers.ChoiceField(choices=models.Quotation.RESPONSE_CHOICES, write_only=True)

    def save(self, validated_data):
        user_request_id = validated_data["user_request_id"]
        user_request = models.UserRequest.objects.get(id=user_request_id)
        quotation = models.Quotation.objects.create(
            user_request=user_request,
            description=validated_data.get("description", ""),
            price=validated_data["price"],
            status=models.Quotation.RESPONSE_PENDING,
        )
        return quotation

class QuotationDetailSerializer(serializers.ModelSerializer):
    user_request = UserRequestDetaillSerializer(read_only=True)
    class Meta:
        model = models.Quotation
        fields = ["id", "user_request", "description", "price", "status"]
class QuotationDetaillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quotation
        fields = ["id", "description", "price", "status"]



