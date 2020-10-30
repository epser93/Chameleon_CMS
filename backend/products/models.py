from django.db import models
from django.conf import settings
from accounts.models import Department
import os

class Template(models.Model):
    name = models.CharField(max_length=100)
    type = models.IntegerField()

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, related_name='category', null=True)
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    def create(self, data, user, template):
        self.name = data['name']
        self.is_active = True
        self.priority = data['priority']
        # 순서 변경 로직 호출
        self.cms_user = user
        self.template = template
        self.save()

    def update(self, data, template):
        self.name = data['name']
        self.priority = data['priority']
        # 순서 변경 로직 호출
        self.template = template
        self.save()

    def delete(self):
        self.is_active = False
        self.save()

    
    # 카테고리 우선순위 변경 로직 추가


class CategoryDescription(models.Model):
    name = models.CharField(max_length=200)   
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='description', null=True)

    def __str__(self) -> str:
        return self.name

    def create(self, description, category):
        self.name = description
        self.category = category
        self.save()

    def update(self, description):
        self.name = description
        self.save()


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    is_temp = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='items', null=True)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, related_name='items', null=True)

    def __str__(self) -> str:
        return self.name

    def create(self, data, user, category, template):
        self.name = data['name']
        self.price = data['price']
        self.title = data['title']
        self.is_temp = data['is_temp']
        self.is_active = data['is_active']
        self.cms_user = user
        self.category = category
        self.template = template
        self.save()

    def update(self, data, template):
        self.name = data['name']
        self.price = data['price']
        self.title = data['title']
        self.is_temp = data['is_temp']
        self.is_active = data['is_active']
        self.template = template
        self.save()


class ItemImage(models.Model):
    item_image = models.ImageField()
    is_thumbnail = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='image', null=True)

    def create(self, data, item):
        self.item_image = data['item_image']
        self.is_thumbnail = data['is_thumbnail']
        self.priority = data['priority']
        self.is_active = data['is_active']
        self.item = item
        self.save()

    def update(self, data):
        self.item_image = data['item_image']
        self.is_thumbnail = data['is_thumbnail']
        self.priority = data['priority']
        self.is_active = data['is_active']
        self.save()


class ItemDescription(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField()

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='description', null=True)
    category_description = models.ForeignKey(CategoryDescription, on_delete=models.SET_NULL, related_name='description', null=True)
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.content

    def create(self, data, user, item, category_description):
        self.title = data['title']
        self.content = data['content']
        self.item = item
        self.category_description = category_description
        self.cms_user = user
        self.save()

    def update(self, data):
        self.title = data['title']
        self.content = data['content']
        self.save()


class CustomerItemLog(models.Model):
    view_date = models.DateTimeField(auto_now_add=True)
    register_ip = models.CharField(max_length=150)

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='itemlog', null=True)

    def create(self, data, item):
        self.register_ip = data['register_ip']
        self.item = item
        self.save()
