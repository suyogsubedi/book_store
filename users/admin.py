from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.
# get_user_model goes to the settings.py and looks for our custom user model, and we are now storing that value
# in CustomUser
CustomUser= get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display= ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
