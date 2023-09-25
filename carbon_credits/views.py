from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import CarbonCredits
from .serializers import CarbonCreditsSerializer


class CarbonCreditsList(APIView):
    def get(self, request):
        carbon_credits = CarbonCredits.objects.all()
        serializer = CarbonCreditsSerializer(carbon_credits, many=True)
        return Response(serializer.data)


class CarbonCreditsDetail(APIView):
    def get_object(self, pk):
        try:
            return CarbonCredits.objects.get(pk=pk)
        except CarbonCredits.DoesNotExist:
            return Response({'error': 'No CarbonCredits found '}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        carbon_credit = self.get_object(pk)
        if carbon_credit is None:
            return Response({'error': 'CarbonCredits not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarbonCreditsSerializer(carbon_credit)
        return Response(serializer.data)
    
    
class CalculateLastCarbonCredit(APIView):
    def get(self, request):
        try:
           
            last_carbon_credit = CarbonCredits.objects.latest('id')
        except CarbonCredits.DoesNotExist:
            return Response({'error': 'No CarbonCredits  found '}, status=status.HTTP_404_NOT_FOUND)

        carbon_credit_value = last_carbon_credit.calculate_credits_earned()
        data = {
            'carbon_credit': carbon_credit_value
        }
        return Response(data)