from django.db import models

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

    


     
