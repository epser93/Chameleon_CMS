from django.contrib import admin
from .models import Event, EventDetail, Notices, MainItem, MainCarouselItem
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date', 'is_active', 'thumbnail_image', 'create_date', 'update_date', 'priority', 'user']
    fields = ['title', 'start_date', 'end_date', 'is_active', 'thumbnail_image', 'priority', 'user']


class EventDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'content', 'priority', 'event', 'user']
    fields = ['image', 'content', 'priority', 'event', 'user']
    

class NoticesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'create_date', 'update_date', 'is_active', 'user', 'image']
    fields = ['title', 'content', 'is_active', 'user', 'image']

class MainItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'priority', 'create_date', 'update_date', 'item', 'user', 'department']
    fields = ['priority', 'item', 'user', 'department']


class MainCarouselItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'create_date', 'update_date', 'priority', 'is_active', 'item', 'user', 'department']
    fields = ['image', 'priority', 'is_active', 'item', 'user', 'department']

admin.site.register(Event, EventAdmin)
admin.site.register(EventDetail,EventDetailAdmin)
admin.site.register(Notices, NoticesAdmin)
admin.site.register(MainItem, MainItemAdmin)
admin.site.register(MainCarouselItem, MainCarouselItemAdmin)