from django.http import response
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView, LogoutView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Department, User, TotalLog
from .serializers import UserSerializer


class UserAPI(APIView):
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


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
        # 상황에 맞게 수정하기
        # user = User.objects.get(username=request.data['username'])
        # user.update(department, employee_number, is_logger, is_eventer, is_producter, is_marketer)
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


class ManagementAPI(APIView):

    def post(self, request):
        if request.user.is_superuser:
            users = request.data['users']
            for user_id in users:
                user = User.objects.get(pk=user_id)
                user.access_ok()
            return Response('승인 완료')
        else:
            return Response('권한 없음', status=status.HTTP_403_FORBIDDEN)