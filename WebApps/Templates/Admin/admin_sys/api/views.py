from django.shortcuts import render
from api import serializer as api_serializer
from api import models as api_models
from DBMS.models import User, Profile
from rest_framework_simplejwt.views import TokenObtainPairView
#REGISTER FORM VIA API
from rest_framework import generics
from rest_framework.permissions import AllowAny
#REFRESH TOKEN
import random
from rest_framework_simplejwt.tokens import RefreshToken

#LOGIN TOKEN
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer
#REGISTER FORM VIA API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer

#ONE TIME PASSOWRD AUTO GENERATION AND RESET TOKEN VIA API
class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    lookup_field = 'email' 
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = api_serializer.UserSerializer
    
    # extract data from the database using email parameter in the URL 
    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.filter(email=email).first()

        if user:
            #uuidb64 means:"User ID encoded in Base64 format"
            uuidb64 = user.pk
            #refresh token
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh.access_token)
            user.refresh_token = refresh_token
            #one time code auto generation
            user.otp = generate_random_otp() 
            user.save() 
            #5173 is the port your local application is running on. This specific port is commonly used by Vite, a fast frontend build tool (like Webpack, but faster), often used in modern JavaScript frameworks like React
            #React (with Vite)
            link = f"http://localhost:5173/create-new-password/?otp={user.otp}&uuidb64={uuidb64}&refresh_token={refresh_token}"
            print ("link =====",link)
        else:
            raise Http404("User not found")
        return user

# auto generator one time password (otp)
def generate_random_otp(Length = 7):
    otp = ''.join([str(random.randint(0,9)) for _ in range(Length)])
    return otp