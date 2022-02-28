from django.test import TestCase
from django.congtrib.auth import get_user_model
from django.test import Client
# from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@frmodel.com',
            password='Test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='admin@frmodel.co',
            passsword='Test123',
            name='test user full name'
        )
