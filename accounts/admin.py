from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomerUserChangeForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "name"]


admin.site.register(CustomUser, CustomUserAdmin)
