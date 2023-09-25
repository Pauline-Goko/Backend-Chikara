from django.urls import path
from .views import LimitViewList


urlpatterns = [
    path("limits/", LimitViewList.as_view(), name="Limit List"),

]
