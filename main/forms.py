#from django.contrib.auth import forms
#from django.contrib.admin import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from main.models import Post


class RegisterUserForm(UserCreationForm):
    username=forms.CharField(label='Login',widget=forms.TextInput(attrs={'class':'form-input'}))
    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2=forms.CharField(label='Password again',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1':forms.PasswordInput(attrs={'class':'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('image',)
