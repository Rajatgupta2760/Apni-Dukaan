# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from .models import Contact
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff']
    ordering = ['email']

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Contact)