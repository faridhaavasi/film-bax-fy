from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    def setUp(self):
        self.user = get_user_model()

    def test_create_user_by_valid_data(self):
        self.user.objects.create_user(
            phone_number='09901234567',
            password='123'
        )
        user = self.user
        user_fond = user.objects.filter(phone_number='09901234567').exists()

        self.assertTrue(user_fond)


