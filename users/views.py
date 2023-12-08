from django.conf import settings
from django.shortcuts import HttpResponse, redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken


from . import models, serializers

class UserRegistrationAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save(validated_data=serializer.validated_data)
            
            refresh = RefreshToken.for_user(data)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)


            return Response(
                {
                "message": "User registered successfully",
                "access_token": access_token,
                "refresh_token": str(refresh_token)
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.UserDetailSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = serializers.UserUpdateSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            data = serializer.save(validated_data=serializer.validated_data)
            user = models.User.objects.get(id=data)

            serializer = serializers.UserDetailSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDeactivateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = serializers.UserDeactivatePasswordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(validate_data=serializer.validated_data)

            return Response({"message": "Account deactivated successfully"}, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    



