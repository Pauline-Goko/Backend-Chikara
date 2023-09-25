from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  .models import Vehicle
from .serializers import VehicleSerializer

# Create your views here.

class VehicleList(APIView):
    
     def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

     def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VehicleDetail(APIView):
    try:
        def get_object(self, pk):
            return Vehicle.objects.get(pk=pk)

        def get(self, request, pk):
            vehicle = self.get_object(pk)
            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data)

        def put(self, request, pk):
            vehicle = self.get_object(pk)
            serializer = VehicleSerializer(vehicle, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk):
            vehicle = self.get_object(pk)
            vehicle.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except Vehicle.DoesNotExist:
        raise status.HTTP_404_NOT_FOUND





