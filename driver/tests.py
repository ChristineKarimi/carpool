from django.test import TestCase

from .models import Profile, Rider, Passenger

from django.contrib.auth.models import User





class ProfileTestClass(TestCase):

    """test class for Profile model"""



    def setUp(self):

        self.user = User.objects.create_user("testuser", "karimikim3@gmail.com", "secret")



        self.new_profile_test = Profile(

            profile_photo='profiles/profile.jpg', profile_owner=self.user)



    def test_instance_true(self):

        self.new_profile_test.save()

        self.assertTrue(isinstance(self.new_profile_test, Profile))



    def test_save_profile_method_true(self):

        self.new_profile_test.save_profile()

        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) == 1)



    def test_delete_profile_method_true(self):

        self.new_profile_test.save_profile()

        self.new_profile_test.delete_profile()

        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) == 0)

