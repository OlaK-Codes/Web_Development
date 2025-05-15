from django.contrib import admin

# Register your models here.
from . models import Course, Module

# make visible inherited categories
"""class InlineLecture(admin.StackedInline):
    model = Module
    # if i want add only one record 
      extra = 1
    # if i want limit max
      max = 2
"""
#tabular variant
class InlineLecture(admin.TabularInline):
    model = Module
#NB! IN INLINE SLUG IS NOT WORKING, have to add manualy or fom the category 

# 1. Create Categories in Admin
class CourseAdmin (admin.ModelAdmin):
     inlines = [InlineLecture]
     #pass
     # connect slug with admin
     prepopulated_fields = {'slug':('course_title',)}
     #dbms
     list_display = ['course_title', 'course_description', 'course_heading']
     
     # create field in the previwe without models
     def course_heading(self, obj):
        return obj.course_title + " - " + obj.course_description

admin.site.register(Course, CourseAdmin)

class ModuleAdmin (admin.ModelAdmin):
     #pass
     # connect slug with admin
     prepopulated_fields = {'slug':('module_name',)}
admin.site.register(Module, ModuleAdmin)

