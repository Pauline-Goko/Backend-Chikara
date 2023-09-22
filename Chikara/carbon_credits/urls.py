from django.urls import path
from . import views

urlpatterns = [
    path('credits/', views.CarbonCreditsList.as_view(), name='carbon-credits-list'),
    path('carbon-credits/<int:pk>/', views.CarbonCreditsDetail.as_view(), name='carbon-credits-detail'),
    path('carbon-credit/', views.CalculateLastCarbonCredit.as_view(), name='calculate-last-carbon-credit'),
]
