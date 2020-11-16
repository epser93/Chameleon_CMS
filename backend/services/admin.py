from django.contrib import admin
from .models import Event, EventDetail, Notices, MainItem, MainCarouselItem
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content','start_date', 'end_date', 'is_active', 'thumbnail_image', 'create_date', 'update_date', 'priority', 'user', 'url']
    fields = ['title', 'start_date', 'content','end_date', 'is_active', 'thumbnail_image', 'priority', 'user', 'url']


class EventDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'priority', 'event', 'user']
    fields = ['image', 'priority', 'event', 'user']
    

class NoticesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'start_date', 'end_date','create_date', 'update_date', 'is_active', 'is_temp', 'user', 'image']
    fields = ['title', 'content', 'is_active', 'user', 'image']


class MainItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'priority', 'create_date', 'update_date', 'item', 'user']
    fields = ['priority', 'is_active', 'item', 'user']


class MainCarouselItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'create_date', 'update_date', 'priority', 'is_active', 'url','user']
    fields = ['image', 'title', 'priority', 'is_active', 'url','user']

admin.site.register(Event, EventAdmin)
admin.site.register(EventDetail,EventDetailAdmin)
admin.site.register(Notices, NoticesAdmin)
admin.site.register(MainItem, MainItemAdmin)
admin.site.register(MainCarouselItem, MainCarouselItemAdmin)