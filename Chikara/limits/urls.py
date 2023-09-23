from django.urls import path
from .views import EmissionCapViewList


urlpatterns = [
    path("limit/", EmissionCapViewList.as_view(), name="Limit List"),
    
]