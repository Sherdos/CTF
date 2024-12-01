from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light border-light'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control bg-dark text-light border-light'}))
    