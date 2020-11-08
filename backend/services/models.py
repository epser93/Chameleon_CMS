from django.db import models
from django.conf import settings
from accounts.models import Department
from products.models import Item, get_imagefile
from datetime import datetime, timezone, timedelta


date_type = '%Y-%m-%d %H:%M:%S'
KST = timezone(timedelta(hours=9))

class Event(models.Model):
    title = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    thumbnail_image = models.ImageField()
    content = models.TextField(default=None, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)
    url = models.TextField(default=None, null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.title

    def create(self, data, user, image):
        self.title = data['title']
        self.content = data['content']
        self.user = user
        self.start_date = datetime.strptime(data['start_date'], date_type).replace(tzinfo=KST)
        self.end_date = datetime.strptime(data['end_date'], date_type).replace(tzinfo=KST)
        self.url = data.get('url', self.url)
        is_success, answer = get_imagefile(image)
        if is_success == False:
            return False, answer
        self.thumbnail_image = answer
        self.save()
        return True, None

    def activate(self):
        self.is_active = True
        self.save()
    
    def update(self, data, user, image):
        self.title = data.get('title', self.title)
        self.content = data.get('content', self.content)
        self.user = user
        self.url = data.get('url', self.url)
        if data.get('start_date', None):
            self.start_date = datetime.strptime(data['start_date'], date_type).replace(tzinfo=KST)
        if data.get('end_date', None):
            self.end_date = datetime.strptime(data['end_date'], date_type).replace(tzinfo=KST)
        if image != None:
            is_success, answer = get_imagefile(image)
            if is_success == False:
                return False, answer
        self.save()
        return True, None

    def delete(self):
        self.is_active = False
        self.save()


class EventDetail(models.Model):
    image = models.ImageField()
    priority = models.IntegerField(default=1)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, related_name='detail', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def create(self, image, priority, event, user):
        is_success, answer = get_imagefile(image)
        if is_success == False:
            return False, answer
        self.image = answer
        self.priority = priority
        self.event = event
        self.user = user
        self.save()


class Notices(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    start_date = models.DateTimeField(default=None, null=True)
    end_date = models.DateTimeField(default=None, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_temp = models.BooleanField(default=True)
    image = models.ImageField(default=None, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def create(self, data, user, image):
        self.title = data['title']
        self.content = data['content']
        self.user = user
        self.is_temp = data.get('is_temp', 'True') == 'True'
        if self.is_temp == False:
            self.start_date = datetime.now().replace(tzinfo=KST)
        is_success, answer = get_imagefile(image)
        if is_success == False:
            return False, answer
        self.image = answer
        self.save()
        return True, None

    def update(self, data, user, image):
        self.title = data.get('title', self.title)
        self.content = data.get('content', self.content)
        self.user = user
        self.is_temp = data.get('is_temp', self.is_temp)
        if image != None:
            is_success, answer = get_imagefile(image)
            if is_success == False:
                return False, answer
            self.image = answer
        self.save()
        return True, None

    def start(self):
        self.is_active = True
        self.is_temp = False
        self.start_date = datetime.now().replace(tzinfo=KST)
        self.end_date = None
        self.save()

    def delete(self):
        if self.is_temp == True:
            super().delete()
            return
        self.is_active = False
        self.end_date = datetime.now().replace(tzinfo=KST)
        self.save()


class MainItem(models.Model):
    priority = models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='main', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='main', null=True)


class MainCarouselItem(models.Model):
    image = models.ImageField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='maincarousel', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name='maincarousel', null=True)

