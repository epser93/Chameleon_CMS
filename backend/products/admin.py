from django.contrib import admin
from .models import Category, CategoryDescription, Item, ItemImage, ItemDescription, CustomerItemLog, Template
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'priority', 'created_date', 'update_date', 'cms_user', 'template']
    fields = ['name', 'is_active', 'priority', 'cms_user', 'template']


class CategoryDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    fields = ['name', 'category']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'title', 'is_temp', 'is_active', 'created_date', 'update_date', 'cms_user', 'template', 'category']
    fields = ['name', 'price', 'title', 'is_temp', 'is_active', 'cms_user', 'template', 'category']


class ItemImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_image', 'is_thumbnail', 'priority', 'is_active', 'created_date', 'update_date', 'item']
    fields = ['item_image', 'is_thumbnail', 'priority', 'is_active', 'item']


class ItemDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'item', 'category_description', 'cms_user']
    fields = ['title', 'content', 'item', 'category_description', 'cms_user']


class CustomerItemLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'view_date', 'register_ip', 'item']
    fields = ['register_ip', 'item']


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']
    fields = ['name', 'type']


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryDescription, CategoryDescriptionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
admin.site.register(ItemDescription, ItemDescriptionAdmin)
admin.site.register(CustomerItemLog, CustomerItemLogAdmin)
admin.site.register(Template, TemplateAdmin)