from django.urls import path
from .views import LimitViewList


urlpatterns = [
    path("limit/", LimitViewList.as_view(), name="Limit List"),
    
]