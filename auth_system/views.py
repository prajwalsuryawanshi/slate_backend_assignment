from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny 
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
import jwt
from django.conf import settings
import datetime
import random
import string
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        role = request.data.get('role')

        user = authenticate(email=email, password=password)

        if user is not None and user.role == role:
            payload = {
                'id': user.id,
                'email': user.email,
                'role': user.role,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            response_data = {
                'token': token,
                'user_id': user.id,
                'email': user.email,
                'role': user.role,
                'dashboard': f'/{user.role.lower()}_dashboard'
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED) 

class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        def make_random_password(N=10):
            return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
        try:
            user = User.objects.get(email=email)
            new_password = make_random_password() 
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password reset. Check your email for the new password.' , 'new password': new_password}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from auth_system.authentication import JWTAuthentication

class ParentDashboardView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'PARENT':
            return Response({'success': True, 'message': 'Parent dashboard access granted'})
        return Response({'success': False, 'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)

class SchoolDashboardView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'SCHOOL':
            return Response({'success': True, 'message': 'School dashboard access granted'})
        return Response({'success': False, 'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)

class StudentDashboardView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'STUDENT':
            return Response({'success': True, 'message': 'Student dashboard access granted'})
        return Response({'success': False, 'error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
