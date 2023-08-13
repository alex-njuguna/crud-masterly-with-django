from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.models import User

from .models import Record


class RegistrationForm(UserCreationForm):
    """Register a user"""
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
        
class LoginForm(AuthenticationForm):
    """Login a user"""
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
            

class CreateRecordForm(forms.ModelForm):
    """create a record"""
    class Meta:
        model = Record
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address','city', 'province', 'country'
            ]
    
class UpdateRecordForm(forms.ModelForm):
    """update a record"""
    class Meta:
        model = Record
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address','city', 'province', 'country'
            ]
    