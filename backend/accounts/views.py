from django.http import response
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView, LogoutView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Department, TotalLog, User
from .serializers import UserSerializer


class UserAPI(APIView):
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


    # def put(self, request):
    #     request.user.update(request.data)
    #     serializer = UserSerializer(request.user)
    #     return Response(serializer.data)


def string_to_boolean(n):
    if n == 'True':
        return True
    return False


class Signup(RegisterView):

    def create(self, request, *args, **kwargs):
        department = Department.objects.get(name=request.data['department'])
        employee_number = request.data['employee_number']
        is_logger = string_to_boolean(request.data.get('is_logger', 'False'))
        is_eventer = string_to_boolean(request.data.get('is_eventer', 'False'))
        is_producter = string_to_boolean(request.data.get('is_producter', 'False'))
        is_marketer = string_to_boolean(request.data.get('is_marketer', 'False'))
        answer = super(RegisterView, self).create(request, *args, **kwargs)  
        user = User.objects.get(username=request.data['username'])
        user.update(department, employee_number, is_logger, is_eventer, is_producter, is_marketer)
        return answer


class Login(LoginView):

    def post(self, request, *args, **kwargs):
        answer = super().post(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        log = TotalLog()
        log.update('로그인', request.data, user)        
        return answer


class Logout(LogoutView):
    
    def post(self, request, *args, **kwargs):
        user = request.user
        answer = super().post(request, *args, **kwargs)
        log = TotalLog()
        log.update('로그아웃', request.data, user)
        return answer