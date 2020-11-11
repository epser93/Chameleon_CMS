from accounts.models import User
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

extentions = ['jpg', 'png', 'jpeg']
fs = FileSystemStorage()
message = "message"

def get_imagefile(image):
    extention = image.name.split('.')[-1].lower()
    if extention not in extentions:
        return False, {message: "잘못된 확장자 입니다."}
    image_file = fs.save(image.name, image)
    return True, image_file

class Template(models.Model):
    name = models.CharField(max_length=100)
    type = models.IntegerField()

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(default=None, null=True)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, related_name='category', null=True)
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    def create(self, data, user, template, image):
        if image != None:
            is_success, answer = get_imagefile(image)
            if is_success == False:
                return False, answer
            self.image = answer
        self.name = data.get('name', '')
        is_active = data.get('is_active', 'False') == 'True'
        self.is_active = is_active
        self.priority = int(data.get('priority', self.priority))
        self.cms_user = user
        self.template = template
        self.save()

    def update(self, data, user,template, image):
        if image != None:
            is_success, answer = get_imagefile(image)
            if is_success == False:
                return False, answer
            self.image = answer
        self.name = data.get('name', self.name)
        self.priority = data.get('priority', self.priority)
        self.template = template
        self.cms_user = user
        self.save()

    def delete(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()

    
    # 카테고리 우선순위 변경 로직 추가


class CategoryDescription(models.Model):
    name = models.CharField(max_length=200)   
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='description', null=True)

    def __str__(self) -> str:
        return self.name

    def create(self, description, category):
        self.name = description
        self.category = category
        self.save()

    def update(self, description):
        self.name = description
        self.save()


class AbstractItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    is_temp = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

    def create(self, data, user, category, template):
        self.name = data.get('name', "")
        self.price = int(data.get('price', self.price))
        self.is_temp = data.get('is_temp', False)
        self.cms_user = user
        self.category = category
        self.template = template
        self.save()

    def copy(self, item):
        self.name = item.name
        self.price = item.price
        self.is_temp = item.is_temp
        self.created_date = item.created_date
        self.update_date = item.update_date
        self.cms_user = User.objects.using('master').get(pk=item.cms_user.pk) 
        self.category = Category.objects.using('master').get(pk=item.category.pk) 
        self.template = Template.objects.using('master').get(pk=item.template.pk) 

    def delete(self):
        self.is_active = False
        items = self.main.all()
        for item in items:
            item.delete()
        self.save()

    def activate(self):
        self.is_active = True
        self.save()

    class Meta:
        abstract = True

class Item(AbstractItem):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='items', null=True)


class AbstractItemImage(models.Model):
    item_image = models.ImageField()
    is_thumbnail = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images', null=True)

    def create(self, image, item, is_thumbnail, priority):
        is_success, answer = get_imagefile(image)
        if is_success == False:
            return False, answer
        self.item_image = answer
        self.is_thumbnail = is_thumbnail
        self.priority = priority
        self.item = item
        self.save()
        return True, None

    def copy(self, item_image, item):
        self.item_image = item_image.item_image
        self.is_thumbnail = item_image.is_thumbnail
        self.created_date = item_image.created_date
        self.update_date = item_image.update_date
        self.item = item
        self.save()

    class Meta:
        abstract = True

class ItemImage(AbstractItemImage):
    pass


class AbstractItemDescription(models.Model):
    content = models.TextField()

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='descriptions', null=True)
    category_description = models.ForeignKey(CategoryDescription, on_delete=models.CASCADE, null=True)
    cms_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.content

    def create(self, name, user, item, category_description):
        self.content = name
        self.item = item
        self.category_description = category_description
        self.cms_user = user
        self.save()
    
    def copy(self, item_description, item):
        self.content = item_description.content
        self.category_description = CategoryDescription.objects.using('master').get(pk=item_description.category_description.pk)
        self.cms_user =  User.objects.using('master').get(pk=item_description.cms_user.pk)
        self.item = item
        self.save()

    class Meta:
        abstract = True


class ItemDescription(AbstractItemDescription):
    pass


class CopyOfItem(AbstractItem):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='historys')


    def copy_create(self, data, user, category, template, item):
        self.item = item
        super().create(data, user,category, template)
        self.save()


class CopyOfItemImage(AbstractItemImage):
    item = models.ForeignKey(CopyOfItem, on_delete=models.CASCADE, related_name='copy_images', null=True)


class CopyOfItemDescription(AbstractItemDescription):
    item = models.ForeignKey(CopyOfItem, on_delete=models.CASCADE, related_name='copy_descriptions', null=True)