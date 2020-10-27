from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.db import models
from django.conf import settings
from accounts.models import Department

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    priorty = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='category', null=True)


class CategoryDescription(models.Model):
    name = models.CharField(max_length=200)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='description', null=True)


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    is_temp = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)


class ItemImage(models.Model):
    item_image = models.ImageField()
    is_thumbnail = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='image', null=True)


class ItemDescription(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='description', null=True)
    category_description = models.ForeignKey(CategoryDescription, on_delete=models.SET_NULL, related_name='description', null=True)
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)


class CustomerItemLog(models.Model):
    view_date = models.DateTimeField(auto_now_add=True)
    register_ip = models.CharField(max_length=150)

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='itemlog', null=True)
