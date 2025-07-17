from django.contrib import admin 
from django.contrib.auth.models import User, Group
from .models import Student,Profile
import data_wizard
from DBMS.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
data_wizard.register(User)

#token implementation
class UserAdmin(BaseUserAdmin):
     # make values from db fields visible via admin
    list_display = ('username', 'email_address','marketing_preferences', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email_address', 'username')
    ordering = ('email_address',)
    #make profile_objectects clickable in the admin 
    list_display_links = ['email_address']
    #make profile_objectects editable via admin (!!excl all linked columns!! )
    list_editable = ('marketing_preferences',)
    fieldsets = (
        (None, {'fields': ('email_address', 'username', 'password', 'otp', 'refresh_token')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email_address', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
admin.site.register(User, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    # make values from db fields visible via admin
    list_display = ['display_title','display_account_owner_name','display_dependants','display_user_email']
    #make profile_objectects clickable in the admin 
    list_display_links = ['display_account_owner_name']

    def display_title(self, profile_object):
        if profile_object.title:
            return profile_object.title     
        return "None"
    display_title.short_description = 'Title'

    def display_account_owner_name(self, profile_object):
        return profile_object.full_name
    display_account_owner_name.short_description = 'Account Owner'

    def display_dependants(self, profile_object):
        dependants = profile_object.user.dependants.all()
        if dependants:
            return ", ".join([f"{d.first_name} {d.family_name}" for d in dependants])
        #return profile_object.dependants.full_name if profile_object.dependants else 'No dependant'
        return "None"
    display_dependants.short_description = 'Students'

    #display email_address from User model in Profile 
    def display_user_email(self, profile_object):
        return profile_object.user.email_address
    display_user_email.short_description = 'User Email'

admin.site.register(Profile, ProfileAdmin)
  
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'family_name', 'date_of_birth', 'date_added']
    list_display_links = ['first_name']
    list_editable = ['family_name']
admin.site.register(Student, StudentAdmin)


##Change admin titles
admin.site.site_header = "My administration"
#Change index titles
admin.site.index_title = "Admin"
#Change website titles
admin.site.site_title = "My Admin"


