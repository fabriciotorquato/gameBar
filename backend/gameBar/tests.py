import json
from django.urls import reverse

from rest_framework.test import APITestCase
from gameBar.models import Bar
from gameBar.serializers import BarSerializer

# Create your tests here.

class BarViewTestCase(APITestCase):
    url = '/api/bars/'
    def setUp(self):
        pass

    def test_create_bar(self):
        response = self.client.post(self.url, {'name':'teste', 'description': 'Bar muito bom', 'address':'Endereco xxyy' })
        self.assertEqual(201, response.status_code)

    
    def test_delete_bar(self):
        response = self.client.post(self.url, {'name':'Bar para deletar', 'description': 'Bar muito bom', 'address':'Endereco xxyy' })
        response_data = json.loads(response.content)

        response = self.client.delete(self.url + str(response_data['id']) + '/' )
        self.assertEqual(204, response.status_code)

        response = self.client.get(self.url + str(response_data['id']) + '/')
        response_data = json.loads(response.content)
        self.assertEqual(False, response_data['status'])





