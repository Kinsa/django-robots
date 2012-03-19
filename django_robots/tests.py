from django.test import TestCase
from django.test.client import Client


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_urls(self):
        # Issue a GET request.
        response = self.client.get('/robots.txt')
        
        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the robots.txt template is being used.
        self.assertTemplateUsed(response, 'robots/robots.txt')