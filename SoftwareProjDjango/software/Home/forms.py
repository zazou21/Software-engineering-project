from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class registration(UserCreationForm):
    email=forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(registration, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


    def clean_email(self):
    
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("User with that email already exists")
        
        return email