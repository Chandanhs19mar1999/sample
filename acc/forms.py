from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')
        widgets={
                  'username':forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'Email':forms.EmailInput(attrs={'class':'form-control'}),
        }