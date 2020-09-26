from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from .models import CustomUser

# Create your tests here.

class CustomUserTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            email='user@gmail.com',
            password='password'
        )

        self.user1 = get_user_model().objects.create_user(
            username='user1',
            email='user1@gmail.com',
            password='password'
        )

    def test_the_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)