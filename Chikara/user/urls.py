from django.urls import path
from .views import user_login_view, user_registration_view, UserListView, UserDetailView
# user_logout_view,

urlpatterns = [
    path('login/', user_login_view, name='user-login'),
    path('register/', user_registration_view, name='user-registration'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('detail/<int:id>/', UserDetailView.as_view(), name='user_detail')
]
