from django.contrib import admin

# Register your models here.
from . models import Membership


#1st Method
#admin.site.register(Membership)

#2nd Method
"""class MembershipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Membership, MembershipAdmin)"""

#3rd Method 
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass

#If I need to make any model invisible
from django.contrib.auth.models import User,Group
admin.site.unregister(User)
admin.site.unregister(Group)





