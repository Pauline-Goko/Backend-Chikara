from limit.models import Limit
from .serializers import LimitSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class LimitViewList(APIView):
    def get(self, request):
        limit = Limit.objects.all()
        serializer = LimitSerializers(limit, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LimitSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
