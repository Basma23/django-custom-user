from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):

    # def test_create_user(self):
    #     User = get_user_model()
    #     user = User.objects.create_user(email='normal@user.com', username='foo')
    #     self.assertEqual(user.email, 'normal@user.com')
    #     self.assertTrue(user.is_active)
    #     self.assertFalse(user.is_staff)
    #     self.assertFalse(user.is_superuser)
    #     try:
    #         # username is None for the AbstractUser option
    #         # username does not exist for the AbstractBaseUser option
    #         self.assertIsNone(user.username)
    #     except AttributeError:
    #         pass
    #     with self.assertRaises(TypeError):
    #         User.objects.create_user()
    #     with self.assertRaises(TypeError):
    #         User.objects.create_user(email='')
    #     with self.assertRaises(ValueError):
    #         User.objects.create_user(email='', username="foo")