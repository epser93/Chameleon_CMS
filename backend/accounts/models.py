from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.query_utils import RegisterLookupMixin
from django.conf import settings

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.name

class User(AbstractUser):
    is_access = models.BooleanField(default=False)
    employee_number = models.IntegerField(default=0)
    is_logger = models.BooleanField(default=False)
    is_eventer = models.BooleanField(default=False)
    is_producter = models.BooleanField(default=False)
    is_marketer = models.BooleanField(default=False)
    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='users', null=True)

    def __str__(self):
        return self.username

    def update(self, department, employee_number, is_logger, is_eventer, is_producter, is_marketer):
        self.department = department
        self.employee_number = employee_number
        self.is_logger = is_logger
        self.is_eventer = is_eventer
        self.is_producter = is_producter
        self.is_marketer = is_marketer
        self.save()
    

class TotalLog(models.Model):
    type = models.CharField(max_length=100)
    register_ip = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='log', null=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.cms_user.username, self.type)

    def update(self, type, data, user):
        self.type = type
        self.register_ip = '0.0.0.0'
        self.cms_user = user
        self.department = user.department
        self.save()