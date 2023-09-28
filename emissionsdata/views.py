from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EmissionsData
from .serializers import EmissionsDataSerializer
from django.db.models import Sum
from datetime import date


class EmissionsDataListView(APIView):
    def get(self, request):
        emissions = EmissionsData.objects.all()
        serializer = EmissionsDataSerializer(emissions, many=True)
        # Calculate monthly totals for the current year
        year = date.today().year
        monthly_totals = {}
        for month in range(1, 13):
            total_emissions = emissions.filter(
                date_created__year=year,
                date_created__month=month
            ).aggregate(total_emissions=Sum('emission_value'))['total_emissions']
            monthly_totals[f"{year}-{month}"] = total_emissions
        response_data = {
            'emissions_data': serializer.data,
            'monthly_totals': monthly_totals
        }
        return Response(response_data)







