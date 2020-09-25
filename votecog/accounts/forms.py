from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Person


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        labels  = {
        "bio":"Why do you want to apply?",
        }