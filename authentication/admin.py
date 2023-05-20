from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.forms import UserFormChange, UserFormCreate
from authentication.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserFormCreate
    form = UserFormChange
    model = User
    list_display = [
        'email', 'first_name', 'last_name',
        'is_active', 'is_staff', 'is_admin'
    ]
    list_filter = [
        'email', 'is_admin', 'is_staff', 'is_active'
    ]
    fieldsets = (
        (
            None, {'fields': ('email', 'password')},
        ),
        (
            'Permissions', {
                'fields': (
                    'is_staff', 'is_active', 'is_admin',
                    'groups', 'user_permissions'
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'last_name',
                    'password1', 'password2', 'is_admin'
                ),
            },
        ),
    )
    search_fields = [
        'email', 'first_name', 'last_name'
    ]
    ordering = [
        'email'
    ]


admin.site.site_header = 'Users Admin'
admin.site.site_title = 'Users Admin Site'
admin.site.index_title = 'Users Admin'
