from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'is_staff', 'date_joined')  # Add other fields as needed

class SignUpSerializer(serializers.Serializer):
    # username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
class SignInSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)