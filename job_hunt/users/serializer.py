from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()        