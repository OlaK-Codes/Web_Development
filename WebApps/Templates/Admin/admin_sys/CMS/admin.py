from django.contrib import admin

# Register your models here.
from . models import Course, Module
#create own admn for cms
class CMSAdminSite(admin.AdminSite):
    site_header = "CMS ADMIN"
cms_site = CMSAdminSite(name = 'cms-site')
cms_site.register(Course)
cms_site.register(Module)

class AdminLoginArea(admin.AdminSite):
  login_template = 'admin/login.html'

#share  admn for cms with DBMS
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
     #Method 1- if I want to hide some field and see any particular fields
     #fields = ('module_name', 'slug',)
     
     #Method 2 using tuples - if I want to hide some field and see any particular fields
     #Additionaly it lets us to add discription (optional)
     fieldsets = (
      #(None, {
       ('Module', {

         'fields': ('module_name','slug',),
         #add description 
         'description':'Module Details',

      }),

      ('Course', {

         'fields': ('course',),# Do not use slug twice!
         #add description 
         'description':'Course Details',

      }),

    )
     # connect slug with admin
     prepopulated_fields = {'slug':('module_name',)}

admin.site.register(Module, ModuleAdmin)

