from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.name

    def create(self, name):
        self.name = name
        self.save()


def string_to_boolean(n):
    if type(n) == type(''):
        return n == 'True'
    return n

class User(AbstractUser):
    is_access = models.BooleanField(default=False)
    employee_number = models.IntegerField(default=0)
    is_logger = models.BooleanField(default=False)
    is_eventer = models.BooleanField(default=False)
    is_producter = models.BooleanField(default=False)
    is_marketer = models.BooleanField(default=False)
    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='users', null=True)

    def __str__(self):
        return '{}({})'.format(self.username, self.first_name)

    def update(self, department, data):
        if department != None:
            self.department = department
        self.employee_number = data.get('employee_number', self.employee_number)
        self.is_logger = string_to_boolean(data.get('is_logger', self.is_logger))
        self.is_eventer = string_to_boolean(data.get('is_eventer', self.is_eventer))
        self.is_producter = string_to_boolean(data.get('is_producter', self.is_producter))
        self.is_marketer = string_to_boolean(data.get('is_marketer', self.is_marketer))
        self.first_name = data.get('first_name', self.first_name)
        self.save()

    def access_ok(self):
        if self.is_access == False:
            self.is_access = True
            self.save()

            

class TotalLog(models.Model):
    type = models.CharField(max_length=100)
    register_ip = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='log', null=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.cms_user.username, self.type)

    def update(self, type, ip_address, user):
        self.type = type
        self.register_ip = ip_address
        self.cms_user = user
        department = Department.objects.using('master').get(pk=user.department.pk)
        self.department = department
        self.save()