from django.test import TestCase
from django.shortcuts import reverse


# this tests that the view for the landing page is going to test the Landingpageview and make sure it renders the right template and return a htt2 status code which is a succesful test run


class LandingPageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")