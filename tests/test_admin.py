"""
Tests for Django Admin integration with dj-doom-panel.

When dj-control-room is installed, the panel's placeholder admin is replaced by
a proxy model registered under the "DJ Control Room" app in the admin sidebar.
The panel itself is accessible directly via its own URL namespace.
"""

from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from .base import PanelTestCase


User = get_user_model()


class TestAdminIntegration(PanelTestCase):
    """Test cases for Django Admin integration."""

    def test_doom_panel_appears_in_admin_index(self):
        """Test that the DOOM panel entry appears in the Django admin index."""
        response = self.client.get("/admin/")

        self.assertEqual(response.status_code, 200)
        # The hub registers DOOM as a community panel under dj_control_room
        self.assertContains(response, "DOOM")

    def test_doom_panel_hub_proxy_redirects_to_panel(self):
        """Test that the hub's proxy admin entry redirects to the DOOM panel."""
        changelist_url = reverse(
            "admin:dj_control_room_djdoompanelpanelproxy_changelist"
        )
        response = self.client.get(changelist_url)

        self.assertEqual(response.status_code, 302)
        expected_url = reverse("dj_doom_panel:index")
        self.assertRedirects(response, expected_url)

    def test_doom_panel_index_renders(self):
        """Test that the DOOM panel index page renders successfully."""
        response = self.client.get(reverse("dj_doom_panel:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DOOM")

    def test_doom_panel_index_contains_js_dos(self):
        """Test that the DOOM panel embeds the js-dos player."""
        response = self.client.get(reverse("dj_doom_panel:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "js-dos.com")
        self.assertContains(response, "doom-shareware.jsdos")

    def test_unauthenticated_user_redirected_to_login(self):
        """Test that unauthenticated users are redirected to login."""
        client = Client()
        response = client.get(reverse("dj_doom_panel:index"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_unauthenticated_user_cannot_access_hub_proxy(self):
        """Test that unauthenticated users cannot reach the hub admin entry."""
        client = Client()
        changelist_url = reverse(
            "admin:dj_control_room_djdoompanelpanelproxy_changelist"
        )
        response = client.get(changelist_url)

        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)

    def test_non_staff_user_cannot_access_doom_panel(self):
        """Test that non-staff users cannot access the panel."""
        user = User.objects.create_user(
            username="regular_user", password="testpass123", is_staff=False
        )
        client = Client()
        client.force_login(user)

        changelist_url = reverse(
            "admin:dj_control_room_djdoompanelpanelproxy_changelist"
        )
        response = client.get(changelist_url)

        self.assertIn(response.status_code, [302, 403])
