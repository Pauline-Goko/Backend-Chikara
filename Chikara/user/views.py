from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import FileUploadParser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
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
    users = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            image = request.data.get('image')
            if image:
                user.account.image = image
                user.account.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Invalid credentials', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        if user:
            user.delete()
            return Response('User deleted successfully', status=status.HTTP_204_NO_CONTENT)
        return Response('You do not have permission to delete this user', status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = None
    user = authenticate(username=username, password=password)
    if user is None and '@' in username:
        try:
            user_profile = User.objects.get(email=username)
            user = user_profile
        except User.DoesNotExist:
            pass
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
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


class ProfileImageView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request):
        user = request.user
        image = request.data['image']
        if image:
            user.account.image = image
            user.account.save()
            return Response({'message': 'Profile image updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Image data is missing'}, status=status.HTTP_400_BAD_REQUEST)

































# class UserListView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)


# class UserDetailView(APIView):
#     def get(self, request, id, format=None):
#         try:
#             user = User.objects.get(id=id)
#         except User.DoesNotExist:
#             return Response(
#                 {"message": f"User with id {id} does not exist."},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, id, format=None):
#         try:
#             user = User.objects.get(id=id)
#         except User.DoesNotExist:
#             return Response(
#                 {"message": f"User with id {id} does not exist."},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id, format=None):
#         try:
#             user = User.objects.get(id=id)
#         except User.DoesNotExist:
#             return Response(
#                 {"message": f"User with id {id} does not exist."},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         user.delete()
#         return Response("User deleted successfully", status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST'])
# def user_login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return Response({'error': 'User with this username does not exist'},
#                         status=status.HTTP_401_UNAUTHORIZED)
#     if user.check_password(password):
#         return Response({'message': 'Successfully logged in.'},
#                         status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid credentials'},
#                         status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def user_registration_view(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         login(request, user)
#         return Response({'message': 'Successfully registered'},
#                         status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
