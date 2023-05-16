from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

types=["Baby-boy","Baby-girl","Toddler boy","Toddler girl","Boys","Girls"]


def Homepage(request):
    return render(request,'Home/index.html',{
        "types":types
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
     return redirect('Myaccount')

   
    

            
            
            

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

def register(request):
    render (request,'Home/register.html')
