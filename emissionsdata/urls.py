from django.urls import path
from .views import EmissionsDataListView

urlpatterns = [
    path('emissions-data/', EmissionsDataListView.as_view(), name='emissions_data'),
]