from django.db import models
from datetime import date, timedelta
from django.core.validators import MinLengthValidator, RegexValidator,EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User (AbstractUser):
    username = models.CharField(unique=True, max_length=100,null=False, blank=True)
    email_address = models.EmailField(unique=True) 
    marketing_preferences = models.BooleanField(default = False,null=True, blank=True)
    otp = models.CharField(max_length=100, null=True, blank=True)
    refresh_token = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = "email_address"
    REQUIRED_FIELDS = ["username"]
    
    def save(self, *args, **kwargs):
        self.ensure_username()
        super(User, self).save(*args, **kwargs)
    
    def ensure_username(self):
        if not self.username:
            self.username = self.extract_username_from_email()
    
    def extract_username_from_email(self):
        return self.email_address.split('@')[0]

    class Meta:
        verbose_name_plural  = "users"

class Student (models.Model):
    first_name = models.CharField(max_length=50)
    family_name = models.CharField(max_length=75)
    date_of_birth =models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='dependants')
    date_added = models.DateTimeField(auto_now_add =True)

    class Meta:
        verbose_name_plural  = "Students"
        ordering = ['family_name']

class Profile(models.Model):
    TITLES_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms'),
        ('Mx', 'Mx'),
        ('None', 'None'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=5, choices=TITLES_CHOICES,null=True, blank=True)
    full_name = models.CharField(max_length=125)
    image = models.FileField(upload_to='user_folder', default='default_user.jpg', null=True, blank=True)
  
    def __str__(self):
        return self.user.username

# standalone functions for Django Signals
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


