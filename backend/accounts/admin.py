from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Department, TotalLog
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_superuser', 'is_access', 'is_logger', 'is_eventer', 'is_producter', 'is_marketer']
    fields = ['username', 'is_access','is_logger', 'is_eventer', 'is_producter', 'is_marketer']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name']


class TotalLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'register_ip', 'create_date', 'cms_user', 'department']
    fields = ['type', 'register_ip', 'cms_user', 'department']


admin.site.register(get_user_model(), UserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(TotalLog, TotalLogAdmin)