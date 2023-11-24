from django.shortcuts import render
from rest_framework import viewsets

from .models import UserRegister, UserLogin
from .serializers import UserRegisterSerializer, UserLoginSerializer

# Create your views here.
class UserRegisterView(viewsets.ModelViewSet):
    serializer_class = UserRegisterSerializer
    queryset = UserRegister.objects.all()
    
class UserLoginView(viewsets.ModelViewSet):
    serializer_class = UserLoginSerializer
    queryset = UserLogin.objects.all()

# class ForgotPasswordView(viewsets.ModelViewSet):
#     serializer_class = ForgotPasswordSerializer
#     queryset = ForgotPassword.objects.all()
    