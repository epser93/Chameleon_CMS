import re
from typing import ClassVar
from django.http import response
from django.http import request
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView, LogoutView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Department, User, TotalLog
from .serializers import CMSUserSerializer, DepartmentSerializer, TotalLogSerializer

message = 'message'
number = set('1234567890')
en = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
s_chr = set('~`!@#$%^&*()-_=+\\|/?.>,<;:\'\"')
email_check = set('@.')

class UserAPI(APIView):
    
    def get(self, request):
        serializer = CMSUserSerializer(request.user)
        return Response(serializer.data)



class Signup(RegisterView):
    def create(self, request, *args, **kwargs):
        if len(request.data.get('first_name', '')) == 0:
            answer = {message: '이름이 없습니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['username']) < 3:
            answer = {message: '너무 짧은 아이디 입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=request.data['username']).exists():
            answer = {message: '존재하는 아이디 입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        if request.data['password1'] != request.data['password2']:
            answer = {message: '비밀번호가 일치하지 않습니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        email = request.data.get('email', '')
        if len(email) < 5 or len(set(email)&email_check) != 2:
            answer = {message: '잘못된 이메일 입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            answer = {message: '존재하는 이메일 입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        # 비밀번호 조건 체크
        password = set(request.data['password1'])
        length = len(password)
        if length < 8 or length > 12 or not (password & number and password & en and password & s_chr) :
            answer = {message: '비밀번호가 조건에 부합하지 않습니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        department = Department.objects.get(name=request.data['department'])
        
        super().create(request, *args, **kwargs)
        user = User.objects.get(username=request.data['username'])
        user.update(department, request.data)
        log = TotalLog()
        log.update('회원가입', request.data, user)
        answer = {message: '회원가입이 완료되었습니다. 관리자 승인 후 로그인 해주세요.'}
        return Response(answer)


class Login(LoginView):

    def post(self, request, *args, **kwargs):
        if not User.objects.filter(username=request.data['username']).exists():
            answer = {message: '존재하지 않는 아이디 입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        if not self.serializer.is_valid(raise_exception=False):
            answer = {message: '잘못된 비밀번호 입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        self.login()
        answer = self.get_response()
        user = User.objects.get(username=request.data['username'])
        if user.is_access == False:
            answer = {message: '관리자 승인이 필요합니다.'}
            return Response(answer, status=status.HTTP_403_FORBIDDEN)
        log = TotalLog()
        log.update('로그인', request.data, user)
        return answer


class Logout(LogoutView):
    
    def post(self, request, *args, **kwargs):
        user = request.user
        print(user)
        if user.is_anonymous:
            answer = {message: '로그인되지 않은 유저입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        super().post(request, *args, **kwargs)
        log = TotalLog()
        log.update('로그아웃', request.data, user)
        answer = {message: '로그아웃 되었습니다.'}
        return Response(answer)


class ManagementAPI(APIView):

    def post(self, request, pk):
        if request.user.is_superuser:
            user = User.objects.get(pk=pk)
            user.access_ok()
            answer = {message : '승인이 완료되었습니다.'}
            return Response(answer)
        else:
            answer = {message : '권한이 없습니다.'}
            return Response(answer, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        if request.user.is_superuser:
            user = User.objects.get(pk=pk)
            user.update(None, request.data)
            serializer = CMSUserSerializer(user)
            return Response(serializer.data)
        else:
            answer = {message: '권한이 없습니다.'}
            return Response(answer, status=status.HTTP_403_FORBIDDEN)


class DepartmentAPI(APIView):

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        if Department.objects.filter(name=request.data['name']).exists():
            answer = {message: '존재하는 부서입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        department = Department()
        department.create(request.data['name'])
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
        

class USerSearchAPI(APIView):   
    def get(self, request):
        if request.user.is_superuser == False:
            answer = {message: "권한이 없습니다."}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        _type = request.GET.get('type', 'all')
        print(_type)
        content = request.GET.get('content', '')
        print(content)
        if _type == 'all':
            users = User.objects.exclude(is_superuser=True)
        elif _type == 'is_access':
            if content == 'False':
                content = False
            else:
                content = True
            users = User.objects.filter(is_access=content).exclude(is_superuser=True)
        elif _type == 'name':
            users = User.objects.filter(first_name__contains=content).exclude(is_superuser=True)
        elif _type == 'department':
            department = Department.objects.get(name=content)
            users = User.objects.filter(department=department).exclude(is_superuser=True)
        else:
            answer = {message: '잘못된 요청입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        serializer = CMSUserSerializer(users, many=True)
        return Response(serializer.data)


class TotalLogAPI(APIView):
    def get(self, request):
        if not request.user.is_superuser and not request.user.is_logger:
            answer = {message: '권한이 없습니다.'}
            return Response(answer, status=status.HTTP_403_FORBIDDEN)
        logs = TotalLog.objects.all()
        serializer = TotalLogSerializer(logs, many=True)
        return Response(serializer.data)

class ValidationAPI(APIView):
    def get(self, request):
        _type = request.GET.get('type', 'id')
        content = request.GET.get('content', '')
        if len(content) < 3:
            answer = {message: '너무 짧은 아이디 입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        if _type == 'id':
            if User.objects.filter(username=content).exists():
                answer = {message: '존재하는 아이디 입니다.'}
                return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        else:
            if User.objects.filter(email=content).exists():
                answer = {message: '존재하는 이메일 입니다.'}
                return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        answer = {message: '사용이 가능합니다.'}
        return Response(answer)