from django.urls import path
from .views import login, logout, UserListView, UserDetailView, ProfileImageView
# user_logout_view,

urlpatterns = [
    path('login/', login, name='user-login'),
    path('logout/', logout, name='user-logout'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('details/', UserDetailView.as_view(), name='user_detail'),
    path("upload-profile-image/", ProfileImageView.as_view(), name="upload-profile-image"),

]
