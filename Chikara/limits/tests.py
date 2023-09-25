from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Limit
from .serializers import LimitSerializers
from django.urls import reverse

class LimitViewListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('Limit List')  
    
    def test_list_limits(self):
        limit1 = Limit.objects.create(emission_limit=100, duration="2023-09-21T08:31:49.508380Z")
        limit2 = Limit.objects.create(emission_limit=200, duration="2023-09-22T08:31:49.508381Z")
        
       
        response = self.client.get(self.url)
        
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
     
        expected_data = LimitSerializers([limit1, limit2], many=True).data
        self.assertEqual(response.data, expected_data)
    
    def test_create_limit(self):
        new_limit_data = {
            "emission_limit": 300,
            "duration": "2023-09-23T08:31:49.508382Z"
        }
        
    
        response = self.client.post(self.url, data=new_limit_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Limit.objects.filter(emission_limit=300).exists())


