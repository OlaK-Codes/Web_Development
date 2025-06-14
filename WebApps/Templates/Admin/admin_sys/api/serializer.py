
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from DBMS.models import Profile, User
# Token refresh
from django.contrib.auth.password_validation import validate_password

# Acces to token via login
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

# CREATE REGISTRATION FORM FOR NEW USER
class RegisterSerializer(serializers.ModelSerializer):
     # create additional one time password fields via serializer
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        # include fields name from model
        fields = ['username', 'email', 'password', 'password2']
    def validate(self, attr):
        if attr['password'] != attr['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attr
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        email_username, _ = user.email.split("@")
        user.username = email_username
        user.set_password(validated_data['password'])
        user.save()
        return user
    
#ONE TIME PASSOWRD AUTO GENERATION AND RESET TOKEN VIA API INTERFACE
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

"""class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile"""
       # fields = '__all__'
