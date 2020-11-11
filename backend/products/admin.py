from django.contrib import admin
from .models import Category, CategoryDescription, Item, ItemImage, ItemDescription, Template, CopyOfItem, CopyOfItemImage, CopyOfItemDescription
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'is_active', 'priority', 'created_date', 'update_date', 'cms_user', 'template']
    fields = ['name', 'image', 'is_active', 'priority', 'cms_user', 'template']


class CategoryDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    fields = ['name', 'category']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'is_temp', 'is_active', 'created_date', 'update_date', 'cms_user', 'template', 'category']
    fields = ['name', 'price', 'is_temp', 'is_active', 'cms_user', 'template', 'category']


class ItemImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_image', 'is_thumbnail', 'priority', 'created_date', 'update_date', 'item']
    fields = ['item_image', 'is_thumbnail', 'priority', 'item']


class ItemDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'item', 'category_description', 'cms_user']
    fields = ['content','item', 'category_description', 'cms_user']


class CopyOfItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'is_temp', 'is_active', 'created_date', 'update_date', 'cms_user', 'template', 'category']
    fields = ['name', 'price', 'is_temp', 'is_active', 'cms_user', 'template', 'category']


class CopyOfItemImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_image', 'is_thumbnail', 'priority', 'created_date', 'update_date', 'item']
    fields = ['item_image', 'is_thumbnail', 'priority', 'item']


class CopyOfItemDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'item', 'category_description', 'cms_user']
    fields = ['content','item', 'category_description', 'cms_user']


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']
    fields = ['name', 'type']


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryDescription, CategoryDescriptionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
admin.site.register(ItemDescription, ItemDescriptionAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(CopyOfItem, CopyOfItemAdmin)
admin.site.register(CopyOfItemImage, CopyOfItemImageAdmin)
admin.site.register(CopyOfItemDescription, CopyOfItemDescriptionAdmin)