from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.query_utils import RegisterLookupMixin
from django.conf import settings

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=40)

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
    

class TotalLog(models.Model):
    type = models.CharField(max_length=100)
    register_ip = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)

    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='log', null=True)