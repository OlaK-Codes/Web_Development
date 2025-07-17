from django.test import TestCase
from DBMS.models import User, Profile
from django.contrib import admin

class TestUserUtils(TestCase):
    def test_save_sets_username_if_missing(self):
        user = User(email_address='jane.smith@example.com', username=None)
        user.save()
        self.assertEqual(user.username, 'jane.smith')

    def test_save_preserves_existing_username(self):
        user = User(email_address='jane.smith@example.com', username='custom_name')
        user.save()
        self.assertEqual(user.username, 'custom_name')
        
    def test_ensure_username_sets_username_when_missing(self):
        user = User(email_address='john.smith@example.com', username=None)
        user.ensure_username()
        self.assertEqual(user.username, 'john.smith')

    def test_ensure_new_username_not_override_existing_username(self):
        user = User(email_address='john.smith@example.com', username='jsmith')
        user.ensure_username()
        self.assertEqual(user.username, 'jsmith')

    def test_extract_username_from_email(self):
        user = User(email_address="test@gmail.com")
        expected_username = "test"
        actual_username = user.extract_username_from_email()
        self.assertEqual(actual_username, expected_username)

class UserProfileSignalTest(TestCase):
    def test_profile_created_after_user_saved(self):
        # Create a user using .create_user() — this triggers post_save
        user = User.objects.create_user(
            username='jane.smith',
            email_address='jane.smith@example.com',
            password='testpassword123'
        )

        # Check that the profile was created and linked
        profile_exists = Profile.objects.filter(user=user).exists()
        self.assertTrue(profile_exists)

        # Optional: Check the user's email via profile
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.user.email_address, 'jane.smith@example.com')

class SaveUserProfileSignalTest(TestCase):
    def test_save_user_triggers_profile_save(self):
        # Step 1: Create a user (and profile via signal)
        user = User.objects.create_user(
            username='john.smith',
            email_address='john.smith@example.com',
            password='secure123'
        )

        # Step 2: Create profile field with value
        user.profile.full_name = 'John Smith'
        user.profile.save()

        # Capture updated timestamp or version
        original_name = user.profile.full_name

        # Step 3: Change something in user and save it
        user.username = 'john.smith.new'
        user.save()  # This triggers save_user_profile signal

        # Step 4: Refresh profile from DB and confirm it’s still saved correctly
        user.profile.refresh_from_db()
        self.assertEqual(user.profile.full_name, original_name)
        self.assertEqual(user.username, "john.smith.new")

