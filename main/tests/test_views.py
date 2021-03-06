from pdb import set_trace

from django.test import TestCase
from django.urls import reverse

from main.forms import ContactForm

# Create your tests here.
class TestPage(TestCase):
    
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
        self.assertContains(response, 'Book Time')
    
    def test_about_us_page_works(self):
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about_us.html')
        self.assertContains(response, 'Book Time')
        self.assertContains(response, 'About Us')
    
    def test_contact_us_page_works(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact_us.html')
        self.assertContains(response, 'Book Time')
        self.assertContains(response, 'Contact Us')
        self.assertIsInstance(response.context["form"], ContactForm)