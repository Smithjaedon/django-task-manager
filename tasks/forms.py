from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Task, User


class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "content"]


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
