import unittest
from django.test.client import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/robots.txt')
        
        # Check that the response is 200 OK.
        self.failUnlessEqual(response.status_code, 200)

        # Check that the robots.txt template is being used.
        TestCase.assertTemplateUsed(response, 'robots.txt', msg_prefix='')