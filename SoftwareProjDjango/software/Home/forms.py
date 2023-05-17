from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class registration(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    def clean_email(self):
    
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("User with that email already exists")
        
        return email
    


