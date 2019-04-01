from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        #fields = ['__all__']
        fields = ['username', 'email', 'password']

