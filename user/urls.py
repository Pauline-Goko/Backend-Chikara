from django.urls import path
from .views import login, logout, UserListView, UserDetailView
# user_logout_view,

urlpatterns = [
    path('login/', login, name='user-login'),
    path('logout/', logout, name='user-logout'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('register/', UserListView.as_view(), name='register'),
    path('details/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('upload-image/', UserImageUploadView.as_view(), name='user-image-upload'),
    # path('upload-image/', UserImageUploadView.as_view(), name='user-image-upload'),

    # path('upload-logo/', LogoImageUploadView.as_view(), name='logo-upload'),
    # path("upload-profile-image/", ProfileImageView.as_view(), name="upload-profile-image"),

]
