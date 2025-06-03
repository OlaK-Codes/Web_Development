from django.shortcuts import render
from api import serializer as api_serializer
from api import models as api_models
from DBMS.models import User, Profile
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer
