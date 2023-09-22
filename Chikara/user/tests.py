from django.test import TestCase
from django.utils import timezone
from .models import User


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            phone_number='+1234567890',
            password='some_password',
            email='test@example.com',
            date_created=timezone.now())

    def test_username(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_phone_number(self):
        self.assertEqual(self.user.phone_number, '+1234567890')

    def test_email(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_date_created(self):
        self.assertIsNotNone(self.user.date_created)
