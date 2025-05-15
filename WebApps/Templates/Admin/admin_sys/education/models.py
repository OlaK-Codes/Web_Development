from django.db import models

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=100)
    course_description = models.TextField(max_length = 1000)

    slug = models.SlugField(max_length = 100)


class Module (models.Model):
    module_name = models.CharField(max_length = 100)
    #create foreign key and delete all relatives records if delete module name
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    
    #slugs are used for creating clean SEO friendly URL
    slug = models.SlugField(max_length = 100)

