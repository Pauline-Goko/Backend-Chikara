from django.shortcuts import render
from limits.models import EmissionCap
from .serializers import EmissionCapSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class EmissionCapViewList(APIView):
    def get(self, request):
        limit = EmissionCap.objects.all()
        serializer = EmissionCapSerializers(limit, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmissionCapSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)