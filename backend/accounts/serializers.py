from .models import TotalLog, Department
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'is_access', 'is_eventer', 'is_producter', 'is_marketer', 'department']


class CMSUserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'is_superuser','is_access', 'is_logger','is_eventer', 'is_producter', 'is_marketer', 'department', 'last_login', 'employee_number']


class TotalLogSerializer(serializers.ModelSerializer):
    # cms_user = UserSerializer(read_only=True, required=False)
    class Meta:
        model = TotalLog
        fields = ['type', 'register_ip', 'create_date', 'cms_user']