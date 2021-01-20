from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.apps import apps


class ChildInline(admin.TabularInline):
    model = apps.get_model('main', 'BlogPost')


class UserAdminConfig(UserAdmin):
    inlines = (
        ChildInline,
    )
    search_fields = ('email', 'user_name', 'first_name')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'blogposts', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        User.email: {'widget': forms.Textarea(attrs={"class": "form-control"})},
        User.user_name: {'widget': forms.Textarea(attrs={"class": "form-control"})},
        User.first_name: {'widget': forms.Textarea(attrs={"class": "form-control"})},
        User.last_name: {'widget': forms.Textarea(attrs={"class": "form-control"})},
        User.password: {'widget': forms.PasswordInput(attrs={"class": "form-control"})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )



admin.site.register(User, UserAdminConfig)