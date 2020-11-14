from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView, LogoutView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Department, User, TotalLog
from .serializers import CMSUserSerializer, DepartmentSerializer, TotalLogSerializer
from django.core.cache import cache
from cms_pjt.redis_key import RedisKey

message = 'message'
number = set('1234567890')
en = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
s_chr = set('~`!@#$%^&*()-_=+\\|/?.>,<;:\'\"')
email_check = set('@.')

forbidden_message = {message: '권한이 없습니다.'}

class UserAPI(APIView):
    
    def get(self, request):
        key = RedisKey.user_admin + request.user.username
        if cache.has_key(key):
            return Response(cache.get(key))
        serializer = CMSUserSerializer(request.user)
        cache.set(key, serializer.data)
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
        length = len(request.data['password1'])
        if length < 8 or length > 12 or not (password & number and password & en and password & s_chr) :
            answer = {message: '비밀번호가 조건에 부합하지 않습니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        department = Department.objects.using('master').get(name=request.data['department'])
        super().create(request, *args, **kwargs)
        user = User.objects.using('master').get(username=request.data['username'])
        user.update(department, request.data)
        log = TotalLog()
        log.update('\'{}({})\' 회원가입'.format(user.first_name, user.username), request.data, user)
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
        user = User.objects.using('master').get(username=request.data['username'])
        if user.is_access == False and user.is_superuser == False:
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        log = TotalLog()
        log.update('\'{}({})\' 로그인'.format(user.first_name, user.username), request.data, user)
        return answer


class Logout(LogoutView):
    
    def post(self, request, *args, **kwargs):
        user = User.objects.using('master').get(username=request.user.username)
        if user.is_anonymous:
            answer = {message: '로그인되지 않은 유저입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        super().post(request, *args, **kwargs)
        log = TotalLog()
        log.update('\'{}({})\' 로그아웃'.format(user.first_name, user.username), request.data, user)
        answer = {message: '로그아웃 되었습니다.'}
        return Response(answer)


class ManagementAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        if request.user.is_superuser == False:
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        admin_user = User.objects.using('master').get(pk=request.user.pk)
        user = User.objects.using('master').get(pk=pk)
        user.access_ok()
        log = TotalLog()
        log.update('\'{}({})\' 회원가입 승인'.format(user.first_name, user.username), None, admin_user)
        answer = {message : '승인이 완료되었습니다.'}
        RedisKey.remove_data()
        return Response(answer)

    def put(self, request, pk):
        if request.user.is_superuser == False:
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        admin_user = User.objects.using('master').get(pk=request.user.pk)
        user = User.objects.using('master').get(pk=pk)
        user.update(None, request.data)
        serializer = CMSUserSerializer(user)
        log = TotalLog()
        log.update('\'{}({})\' 권한 변경'.format(user.first_name, user.username), request.data, admin_user)
        RedisKey.remove_data()
        return Response(serializer.data)
            

class DepartmentAPI(APIView):
    def get(self, request):
        key = RedisKey.departemt
        if cache.has_key(key):
            return Response(cache.get(key))
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        cache.set(key, serializer.data)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_superuser == False:
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        if Department.objects.filter(name=request.data['name']).exists():
            answer = {message: '존재하는 부서입니다.'}
            return Response(answer, status=status.HTTP_400_BAD_REQUEST)
        department = Department()
        department.create(request.data['name'])
        serializer = DepartmentSerializer(department)
        cache.delete(RedisKey.departemt)
        return Response(serializer.data)
        

class UserSearchAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_superuser == False:
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        _type = request.GET.get('type', 'all')
        content = request.GET.get('content', '')
        key = '{}{}:{}'.format(RedisKey.user_search, _type, content) 
        if cache.has_key(key):
            return Response(cache.get(key))
        if _type == 'all':
            users = User.objects.filter(first_name__contains=content).filter(is_access=True).exclude(is_superuser=True)
        elif _type == 'is_access':
            users = User.objects.filter(is_access=False).exclude(is_superuser=True)
        else :
            department = Department.objects.filter(name=_type)
            if not department:
                answer = {message: '잘못된 요청입니다.'}
                return Response(answer, status=status.HTTP_400_BAD_REQUEST)
            department = department[0]
            users = User.objects.filter(department=department).filter(first_name__contains=content).exclude(is_superuser=True)
        serializer = CMSUserSerializer(users, many=True)
        cache.set(key, serializer.data)
        return Response(serializer.data)


class TotalLogAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_superuser == False and request.user.is_logger == False:
            return Response(forbidden_message, status=status.HTTP_403_FORBIDDEN)
        logs = TotalLog.objects.all().order_by('-pk')
        serializer = TotalLogSerializer(logs, many=True)
        return Response(serializer.data)


class ValidationAPI(APIView):
    def get(self, request):
        _type = request.GET.get('type', 'id')
        content = request.GET.get('content', '')
        if len(content) < 5:
            answer = {message: '너무 짧은 길이 입니다.'}
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