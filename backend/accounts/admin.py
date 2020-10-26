from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_superuser', 'is_access']
    fields = ['username', 'is_access',]


admin.site.register(get_user_model(), UserAdmin)