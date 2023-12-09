from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status, response, generics
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
        

class ListUserRequest(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.UserRequest.objects.all()
    serializer_class = serializers.UserRequestDetailSerializer

    def get_queryset(self):
        return self.request.user.requests.all()
class ListAllUserRequest(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.UserRequest.objects.all()
    serializer_class = serializers.UserRequestDetailSerializer


class CreateQuotation(APIView):
    def post(self, request):
        serializer = serializers.QuotationCreateSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save(validated_data=serializer.validated_data)
            print(data)
            serializer = serializers.QuotationDetailSerializer(data)
            
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
       
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetQuotation(APIView):
    def get(self, request, quotation_id):
        try:
            quotation = models.Quotation.objects.get(id=quotation_id)
            serializer = serializers.QuotationDetailSerializer(quotation)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except models.Quotation.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)