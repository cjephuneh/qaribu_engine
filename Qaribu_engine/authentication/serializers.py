from rest_framework import serializers
from .models import UserLogin, UserRegister

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = '__all__'
        
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'
        
# class ForgotPasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ForgotPassword
#         fields = '__all__'
        
# class UserRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRegister
#         fields = '__all__'