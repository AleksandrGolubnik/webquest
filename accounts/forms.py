from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    first_name = forms.CharField(max_length=254)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email','password1', 'password2')
