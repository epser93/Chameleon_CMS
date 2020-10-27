from django.contrib import admin
from .models import Event, EventDetail, Notices, FAQ, CompanyData, MainItem, MainCarouselItem, Template, Manual
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date', 'is_active', 'thumbnail_image', 'create_date', 'update_date', 'priority', 'cms_user', 'department']
    fields = ['title', 'start_date', 'end_date', 'is_active', 'thumbnail_image', 'priority', 'cms_user', 'department']


class EventDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'content', 'priority', 'event', 'cms_user']
    fields = ['image', 'content', 'priority', 'event', 'cms_user']
    

class NoticesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'create_date', 'update_date', 'is_active', 'cms_user', 'department']
    fields = ['title', 'content', 'is_active', 'cms_user', 'department']
    

class FAQAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'create_date', 'update_date', 'image', 'is_active', 'cms_user', 'department']
    fields = ['title', 'content', 'image', 'is_active', 'cms_user', 'department']


class CompanyDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_address', 'company_number', 'onner_name', 'company_logo_image', 'company_name', 'company_email', 'contact_image', 'about_auth_image']
    fields = ['company_address', 'company_number', 'onner_name', 'company_logo_image', 'company_name', 'company_email', 'contact_image', 'about_auth_image']


class MainItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'priority', 'create_date', 'update_date', 'item', 'cms_user', 'department']
    fields = ['priority', 'item', 'cms_user', 'department']


class MainCarouselItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'create_date', 'update_date', 'priority', 'is_active', 'item', 'cms_user', 'department']
    fields = ['image', 'priority', 'is_active', 'item', 'cms_user', 'department']


class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']


class ManualAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'image']
    fields = ['content', 'image']


admin.site.register(Event, EventAdmin)
admin.site.register(EventDetail,EventDetailAdmin)
admin.site.register(Notices, NoticesAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(CompanyData, CompanyDataAdmin)
admin.site.register(MainItem, MainItemAdmin)
admin.site.register(MainCarouselItem, MainCarouselItemAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Manual, ManualAdmin)