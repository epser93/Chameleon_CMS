from django.db import models
from django.conf import settings
from django.db.models.deletion import DO_NOTHING
from accounts.models import Department
from products.models import Item

class Event(models.Model):
    title = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    thumbnail_image = models.ImageField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)

    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='event', null=True)

    def __str__(self) -> str:
        return self.title


class EventDetail(models.Model):
    image = models.ImageField()
    content = models.TextField()
    priority = models.IntegerField(default=1)

    event = models.ForeignKey(Event, on_delete=models.SET_NULL, related_name='detail', null=True)
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)


class Notices(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='notice', null=True)


class FAQ(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    is_active = models.BooleanField(default=True)

    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='faq', null=True)


class CompanyData(models.Model):
    company_address = models.CharField(max_length=200)
    company_number = models.CharField(max_length=100)
    onner_name = models.CharField(max_length=50)
    company_logo_image = models.ImageField()
    company_name = models.CharField(max_length=50)
    company_email = models.CharField(max_length=100)
    contact_image = models.ImageField()
    about_auth_image = models.ImageField()


class MainItem(models.Model):
    priority = models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='main', null=True)
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='main', null=True)


class MainCarouselItem(models.Model):
    image = models.ImageField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='maincarousel', null=True)
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='maincarousel', null=True)



class Manual(models.Model):
    content = models.TextField()
    image = models.ImageField(null=True)


