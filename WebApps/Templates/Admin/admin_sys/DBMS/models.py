from django.db import models
#create user account for login
from django.contrib.auth.models import AbstractUser
# profile via abstractuser autofill
from django.db.models.signals import post_save

#CREATE USER ACCOUNT MODEL FOR REGISTRATION   
class User (AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    #insert additional field in User table for password fields in serializer 
    otp = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"] 

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            email_username = self.email.split('@')[0]
            self.username = email_username
        super(User, self).save(*args, **kwargs)

# CREATE PROFILE FOR USER
class Profile (models.Model):
     #foreign key
     user = models.OneToOneField(User, on_delete = models.CASCADE)
     image = models.FileField(upload_to='user_folder',default='default_user.jpg', null =True, blank = True)

     def __str__(self):
        return self.user.username 

#AUTOFILL PROFILE VIA USER
def create_user_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance,**kwargs):
    instance.profile.save()
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile,sender =User)


# Create your models (tables) here.
class Membership (models.Model):
     # customise name of categories in admin
     class Meta:
          verbose_name_plural = "Gym Members"
          # implement ordering by column value
          ordering = ['unique_code']

   # Create Table fields
     name = models.CharField(max_length =500)
     
     #categor. value field 
     MEMBERSHIP_CHOICES = (
        ('s','Standart'),
        ('p','Premium'),
        ('ux','Ultimate Delux')
     )

     membership_plan = models.CharField(max_length =2, choices = MEMBERSHIP_CHOICES)
     
     # tick field
     membership_active = models.BooleanField(default=True)
     
     unique_code = models.CharField(max_length =250)
   
class Client (models.Model):

    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =100)
    job_title = models.CharField(max_length =150)







     
     # displays values of name fields via admin
     #def _str_(self):
     #return self.name + ' - record'

    


     
