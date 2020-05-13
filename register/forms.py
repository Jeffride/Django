from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    #needs to be called meta and its going to change the form
    class Meta:
        model = User

        #This lets you choose the order in which the form is shown
        fields = ["username","email","password1","password2"]

