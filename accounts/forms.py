from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('support', 'Support Representative')
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','address', 'password1', 'password2','role']
# from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser 
