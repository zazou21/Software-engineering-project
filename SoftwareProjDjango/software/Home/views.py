from django.shortcuts import render,redirect
from django import forms
from django.forms.forms import Form  
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import registration
# Create your views here.


class NewForm(forms.Form):
    username=forms.CharField(label="username")
    password=forms.CharField(label="password")

     
 


def Homepage(request):
    return render(request,'Home/index.html',{
        
    })

def aboutus(request):
    return render(request,'Home/aboutus.html')


def Cart(request):
    return render(request,'Home/cart.html')

def Myaccount(request):
    if (request.method=="POST") and (not request.user.is_authenticated) :
      
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('home')
       
        else:
           messages.success(request,"log in failed")
           return redirect('Myaccount')
    else:
        
        return render(request, 'Home/myaccount.html')
    
    


        
def logout_user(request):
     logout(request)
     return redirect('home')

   
    

            
            
            

def Forgetpass(request):
    return render(request,'Home/Forgetpass.html')

def Wishlist(request):
    return render(request,'Home/wishlist.html')

def Register(request):
    return render(request, 'Home/register.html')

def Boy(request):
    return render(request, 'Home/boy.html')

def Girl(request):
    return render(request,'Home/girl.html')

def children(request):
    return render(request,'Home/children.html')

def product(request):
    return render(request,'Home/product.html')

def baby(request):
    return render(request, 'Home/baby.html')

def register_user(request):
    if request.method == 'POST':
        Form=registration(request.POST)
        if Form.is_valid():
            Form.save()
            username=Form.cleaned_data['username']
            password=Form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('home')

    else:
        Form=registration()   

    return render(request,'Home/register.html',{'Form':Form})
        
        
        
     
