# # views.py
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # from .models import EmissionData, EmissionLimit, CarbonCredits
# from .serializers import EmissionDataSerializer, EmissionLimitSerializer, CarbonCreditsSerializer

# @api_view(['POST'])
# def create_carbon_credits(request):
#     try:
#         # Deserialize the request data
#         emission_data_serializer = EmissionDataSerializer(data=request.data.get('emission_data'))
#         emission_limit_serializer = EmissionLimitSerializer(data=request.data.get('emission_limit'))

#         if not emission_data_serializer.is_valid() or not emission_limit_serializer.is_valid():
#             return Response({'error': 'Invalid input data.'}, status=status.HTTP_400_BAD_REQUEST)

#         emission_data = emission_data_serializer.save()
#         emission_limit = emission_limit_serializer.save()

#         # Calculate credits
#         total_emissions = emission_data.CO2_emissions
#         total_limit = emission_limit.emission_limit
#         total_carbon = total_limit - total_emissions
#         credit_earned = total_carbon / 1000

#         # Create CarbonCredits instance
#         carbon_credits = CarbonCredits.objects.create(
#             emission_data=emission_data,
#             emission_limit=emission_limit,
#             credit_earned=credit_earned
#         )

#         # Serialize the CarbonCredits instance for the response
#         serializer = CarbonCreditsSerializer(carbon_credits)

#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_carbon_credits_list(request):
#     try:
#         carbon_credits = CarbonCredits.objects.all()
#         serializer = CarbonCreditsSerializer(carbon_credits, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
