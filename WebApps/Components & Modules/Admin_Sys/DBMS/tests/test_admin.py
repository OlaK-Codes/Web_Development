#dry code
from django.test import TestCase
from DBMS.models import User, Profile, Student
from datetime import date 

# Mock admin class 
class MockAdminProfile:
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
        return "None"
    display_dependants.short_description = 'Students'

    def display_user_email(self, profile_object):
        return profile_object.user.email_address
    display_user_email.short_description = 'User Email'



class DisplayTitleTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jane.smith',
            email_address='jane.smith@example.com',
            password='testpassword123'
        )
        self.profile = Profile.objects.get(user=self.user)

        # Create dependant (Student)
        self.dependant = Student.objects.create(
            user=self.user,
            first_name='John',
            family_name='Smith',
            date_of_birth=date(2010, 5, 15)
        )


        self.admin = MockAdminProfile()

    def update_profile(self, full_name, title):
        self.profile.full_name = full_name
        self.profile.title = title
        self.profile.save()

    def test_display_title_returns_actual_title(self):
        self.update_profile("Jane Smith", "Ms")
        result = self.admin.display_title(self.profile)
        self.assertEqual(result, "Ms")  

    def test_display_title_with_none_title_value(self):
        self.update_profile("Jane Smith", None)
        result = self.admin.display_title(self.profile)
        self.assertEqual(result, "None")  

    def test_display_title_with_string_none_title_value(self):
        self.update_profile("Jane Smith", "None")
        result = self.admin.display_title(self.profile)
        self.assertEqual(result, "None")
    
    def test_display_account_owner_name(self):
        self.update_profile("Jane Smith", "Ms")
        result = self.admin.display_account_owner_name(self.profile)
        self.assertEqual(result, "Jane Smith")
    
    def test_display_user_email(self):
        result = self.admin.display_user_email(self.profile)
        self.assertEqual(result, "jane.smith@example.com")

    def test_display_dependants_return_name(self):
        result = self.admin.display_dependants(self.profile)
        self.assertEqual(result, "John Smith")

    def test_display_dependants_none(self):
        new_user = User.objects.create_user(
            username='no.children',
            email_address='nochild@example.com',
            password='securepass'
        )
        new_profile = Profile.objects.get(user=new_user)
        result = self.admin.display_dependants(new_profile)
        self.assertEqual(result, "None")
    

# wet code
"""from django.test import TestCase
from DBMS.models import User, Profile  

# Mock admin class 
class MockAdminProfile:
    def display_title(self, profile_object):
        if profile_object.title:
            return profile_object.title
        return "None"

    display_title.short_description = 'Title'

class DisplayTitleTest(TestCase):
    def test_display_title_returns_actual_title(self):
        # Create a user
        user = User.objects.create_user(
            username='jane.smith',
            email_address='jane.smith@example.com',
            password='testpassword123'
        )
         # Get the created profile 
        profile = Profile.objects.get(user=user)
        
        # Update profile with details (with title)
        profile.full_name = "Jane Smith"
        profile.title = "Ms"
        profile.save()

        admin = MockAdminProfile()
        result = admin.display_title(profile)

        self.assertEqual(result, "Ms")  
        
    def test_display_title_with_none_title_value(self):
        # Create a user
        user = User.objects.create_user(
            username='jane.smith',
            email_address='jane.smith@example.com',
            password='testpassword123'
        )
         # Get the created profile 
        profile = Profile.objects.get(user=user)
        
        # Update profile with details (with title)
        profile.full_name = "Jane Smith"
        profile.title = None
        profile.save()

        admin = MockAdminProfile()
        result = admin.display_title(profile)

        self.assertEqual(result, "None")  

    def test_display_title_with_string_none_title_value(self):
        # Create a user
        user = User.objects.create_user(
            username='jane.smith',
            email_address='jane.smith@example.com',
            password='testpassword123'
        )
         # Get the created profile 
        profile = Profile.objects.get(user=user)
        
        # Update profile with details (with title)
        profile.full_name = "Jane Smith"
        profile.title = "None"
        profile.save()

        admin = MockAdminProfile()
        result = admin.display_title(profile)

        self.assertEqual(result, "None")"""



