from django.contrib import admin

# Register your models here.
from . models import Membership, Client
#captcha
from django.contrib.auth.models import Group

#for user account and profile auth
from DBMS.models import User, Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]
admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)


#import csv
import data_wizard
data_wizard.register(Client)
admin.site.register(Client)
# Ensure Group is registered (this avoids the NotRegistered error)
try:
    admin.site.register(Group)
except admin.sites.AlreadyRegistered:
    pass

#1st Method
#admin.site.register(Membership)

#2nd Method
"""class MembershipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Membership, MembershipAdmin)"""

#3rd Method 
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    # Implement Search function
    search_fields = ('name','unique_code',)

    #make  all table fields visible for admin
    #pass

    #change admin options eg swich off unique code field
    # Method1
    """fields = (
        'name',
        'membership_plan',
        'membership_active',
        #'unique_code',
    )"""
    #Method 2
    """exclude = (
        'unique_code',
    )"""

    # place some fields in one line
    """fields = (
        ('name','membership_plan'),
        'membership_active',  
    )"""
    
    # make values from db fields visible via admin
    list_display = ['name','membership_plan','membership_active', 'unique_code']
    # Add filters in the particulat field
    list_filter = ['membership_plan']
    #make objects clickable in the admin 
    list_display_links = ['name', 'unique_code']
    #make objects editable via admin (!!excl all linked columns!! )
    list_editable = ('membership_plan',)

    # Add additional functions into Action list eg. set membership active 
    actions = ('set_membership_to_active',)
    def set_membership_to_active(self, request,queryset):
        queryset.update(membership_active = True)
         #add message to functions
        self.message_user(request,'membership(s) activated')
    set_membership_to_active.short_description = 'Mark selected membership as active'
  
  #=====NB! I CAN ADD PERMISSION VIA ADMIN WITHOUT CODDING TOO  ============
    #mannually change permission in admin
    def has_add_permission(self,request):
        # if i want manually remove any functionality from admin profile
        #return False
        return True
    
    def has_change_permission(self,request,obj=None):
        #return False
        return True

    def has_delete_permission(self,request,obj=None):
        #return False
        #return True
        if obj !=None and request.POST.get('actiion') == 'delete_selected':
            messages.add_message(request,messages.ERROR,(
                "Are you sure you want to delete this object?"
            )
            )
        return True


#If I need to make any model invisible
from django.contrib.auth.models import User,Group
#admin.site.unregister(User)
admin.site.unregister(Group)

#Change admin titles
admin.site.site_header = "Elevate administration"

#Change index titles
admin.site.index_title = "Admin"

#Change website titles
admin.site.site_title = "My site"














