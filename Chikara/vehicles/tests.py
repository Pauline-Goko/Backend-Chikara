from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vehicle_data = {
            "number_plate": "ABC123",
            "engine_type": "Gasoline"
        }
        self.vehicle = Vehicle.objects.create(**self.vehicle_data)
        self.url_list = reverse("vehicle-list")
        self.url_detail = reverse("vehicle-detail", args=[self.vehicle.id])

    def test_create_vehicle(self):
        response = self.client.post(self.url_list, self.vehicle_data,
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_vehicle_list(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_vehicle_detail(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = VehicleSerializer(self.vehicle)
        self.assertEqual(response.data, serializer.data)

    def test_update_vehicle(self):
        updated_data = {
            "number_plate": "XYZ789",
            "engine_type": "Electric"
        }
        response = self.client.put(self.url_detail, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_vehicle = Vehicle.objects.get(id=self.vehicle.id)
        self.assertEqual(updated_vehicle.number_plate, updated_data["number_plate"])
        self.assertEqual(updated_vehicle.engine_type, updated_data["engine_type"])

    def test_delete_vehicle(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vehicle.objects.filter(id=self.vehicle.id).exists())

