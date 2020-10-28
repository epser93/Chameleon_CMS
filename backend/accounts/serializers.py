from .models import TotalLog
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_access', 'is_eventer', 'is_producter', 'is_marketer', 'department']


class CMSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_access', 'is_eventer', 'is_producter', 'is_marketer', 'department', 'last_login', 'employee_number']


class TotalLogSerializer(serializers.ModelSerializer):
    # cms_user = UserSerializer(read_only=True, required=False)
    class Meta:
        model = TotalLog
        fields = ['type', 'register_ip', 'create_date', 'cms_user']