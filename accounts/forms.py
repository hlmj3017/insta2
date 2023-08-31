from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()

        fields = ('username', 'profile_image',)

class AuthForm(AuthenticationForm):
    pass