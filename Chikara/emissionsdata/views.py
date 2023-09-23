# from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmissionsDataSerializer
from rest_framework.response import Response
from .models import EmissionsData
# Create your views here.

class EmissionsDataListView(APIView):
    def get(self, request):
        emissions = EmissionsData.objects.all()
        serializer = EmissionsDataSerializer(emissions, many = True)
        return Response(serializer.data)
    
