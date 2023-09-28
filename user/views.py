from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer, ImageUploadSerializer, LogoUploadSerializer
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.decorators import login_required
# logout


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            phone_number = serializer.validated_data['phone_number']
            user = User.objects.create_user(username=username, email=email, password=password, phone_number=phone_number)
            return Response('Your account has been created successfully', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            image = request.data.get('image')
            if image:
                user.account.image = image
                user.account.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response('User deleted successfully', status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is None and '@' in username:
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            pass

    if user:
        # Successful authentication
        return Response({'message': 'Authentication successful'}, status=status.HTTP_200_OK)

    # Authentication failed
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @login_required
# class UserImageUploadView(generics.UpdateAPIView):
#     serializer_class = ImageUploadSerializer
#     parser_classes = (MultiPartParser, FormParser)

#     def get_object(self):
#         return self.request.user

#     def put(self, request, *args, **kwargs):
#         user = self.get_object()
#         serializer = self.get_serializer(user, data=request.data)
#         if serializer.is_valid():
#             image = serializer.validated_data['image']
#             user.image = image
#             user.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class UserImageUploadView(APIView):
#     parser_classes = (MultiPartParser,)

#     def put(self, request, *args, **kwargs):
#         user = self.request.user  
#         serializer = ImageUploadSerializer(user, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoImageUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self, request, *args, **kwargs):
        user = self.request.user  
        serializer = LogoUploadSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProfileImageView(APIView):
#     parser_classes = [FileUploadParser]

#     def post(self, request):
#         user = request.user
#         image = request.data['image']
#         if image:
#             user.account.image = image
#             user.account.save()
#             return Response({'message': 'Profile image updated successfully'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Image data is missing'}, status=status.HTTP_400_BAD_REQUEST)
