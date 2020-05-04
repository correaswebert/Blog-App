from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # form must pass the information to the User model
        model = User

        # fields to be shown on the form and in what order
        # password1 -> password | password2 -> confirm password
        fields = ['username', 'email', 'password1', 'password2']
