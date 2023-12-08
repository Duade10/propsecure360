from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status, response
from . import models, serializers

class CreateUserRequest(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = serializers.UserRequestCreateSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():

            data = serializer.save(validated_data=serializer.validated_data)

            serializer = serializers.UserRequestDetailSerializer(data)

            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserRequest(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_request_id):
        try:
            user_request = models.UserRequest.objects.get(id=user_request_id)
            serializer = serializers.UserRequestDetailSerializer(user_request)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
            
        except models.UserRequest.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        