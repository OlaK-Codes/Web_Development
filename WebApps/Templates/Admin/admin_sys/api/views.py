from django.shortcuts import render
from api import serializer as api_serializer
from api import models as api_models
from DBMS.models import User, Profile
from rest_framework_simplejwt.views import TokenObtainPairView
#REGISTER FORM VIA API
from rest_framework import generics
from rest_framework.permissions import AllowAny

#LOGIN TOKEN
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer
#REGISTER FORM VIA API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer