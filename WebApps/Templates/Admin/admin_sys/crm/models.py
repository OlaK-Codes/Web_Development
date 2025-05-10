from django.db import models

# Create your models here.
class Membership (models.Model):
     name = models.CharField(max_length =500)
     #constant 
     MEMBERSHIP_CHOICES = (
        ('s','Standart'),
        ('p','Premium'),
        ('ux','Ultimate Delux')
     )

     membership_plan = models.CharField(max_length =2, choices = MEMBERSHIP_CHOICES)
     membership_active = models.BooleanField(default=True)
     unique_code = models.CharField(max_length =250)
