from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer,LoginSerializer

# Create your views here.
class UserView(APIView):
    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer()
        return Response
    
class LoginView(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(
               {
                    "status" : False,
                    "data" : serializer.data
               }
            )
        return Response(
            data
        )





