from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    # Register the User model to Admin panel.
    #add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # list display controls field items that appear on Admin panel.
    list_display = [
        'name',
        'email',
        'username',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
