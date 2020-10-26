from django.db import models
from django.contrib.auth.models import AbstractUser

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
    
    