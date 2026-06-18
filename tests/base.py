"""
Base test class for dj-doom-panel tests.
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model


User = get_user_model()


class PanelTestCase(TestCase):
    """
    Base test case for dj-doom-panel tests.
    Sets up an authenticated superuser for testing.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="testpass123",
            is_staff=True,
            is_superuser=True,
        )
        self.client = Client()
        self.client.force_login(self.user)

    def tearDown(self):
        pass
