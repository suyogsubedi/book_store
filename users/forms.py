# Importing Custom User Model via get_user_model which looks to our AUTH_USER_MODEL config in settings.py
from django.contrib.auth import get_user_model

# Imported UserCreationForm and UserChange form which will be extended
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# creating two new forms CustomUserCreationForm and CustomUserChangeForm and have given it the the data that it will need to change
# Password field is added by default so we dont need to add it

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)