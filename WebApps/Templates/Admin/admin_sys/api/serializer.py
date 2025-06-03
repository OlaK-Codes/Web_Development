
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from DBMS.models import Profile, User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # name of model
        token = super().get_token(user)
        #fields names from model !NB THIS INFO WILL BE VISIBLE VIA JWT.IO SO INCLUDE THE MOST NESSEASRY
        token['email'] = user.email

        return token
    def validate(self, attrs):
        # allow using email to login
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
