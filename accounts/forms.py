from django import forms
from django.contrib.auth.forms import UserCreationForm


class SigninForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

