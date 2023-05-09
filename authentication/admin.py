from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext_lazy

from authentication.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = [
        '__str__', 'first_name', 'last_name',
        'is_active', 'is_staff'
    ]
    ordering = [
        'email'
    ]
    search_fields = [
        'email', 'first_name', 'last_name'
    ]


admin.site.site_header = 'Users Admin'
admin.site.site_title = 'Users Admin Site'
admin.site.index_title = 'Users Admin'
