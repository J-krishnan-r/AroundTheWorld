from django import forms
from .models import Destination
from django.contrib.auth.models import User

class CreateForm(forms.ModelForm):  
    class Meta:
        model = Destination 
        fields = '__all__'  
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']