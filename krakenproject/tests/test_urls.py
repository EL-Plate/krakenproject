from django.test import SimpleTestCase
from django.urls import reverse


class TestUrls(SimpleTestCase):

    # test to see if request for admin url resolves
    def test_admin_url(self):
        url = reverse("admin:index")
        self.assertEqual(url, "/admin/")

