from django.shortcuts import get_object_or_404, render,redirect
from django import forms
from django.forms.forms import Form  
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import registration
from .models import *
from django.views.generic import ListView
# Create your views here.


class NewForm(forms.Form):
    username=forms.CharField(label="username")
    password=forms.CharField(label="password")

     
 


def Homepage(request):
    return render(request,'Home/index.html',{
        
    })

def aboutus(request):
    return render(request,'Home/aboutus.html')


def cart(request):
    cartobjects=Cart.objects.filter()


    return render(request,'Home/cart.html',{'cartobjects':cartobjects})

def Myaccount(request):
    if (request.method=="POST") and (not request.user.is_authenticated) :
      
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('home')
       
        else:
           messages.success(request,"Login failed")
           return redirect('Myaccount')
    else:
        
        return render(request, 'Home/myaccount.html')
    

class childrenproductListView(ListView):
    model=childrenproduct
    context_object_name='children'

def h(request):
    return render(request,'Home/h.html')

def product_view(request,child_name,child_price,child_img,child_productID):
    product = get_object_or_404(childrenproduct, productID=child_productID)
    context = {
        'child_name': child_name,
        'child_price': child_price,
        'child_img': child_img,
        'product': product,
        'colors': product.product_attributes.first().colors.all()
       
    }
    return render(request, 'Home/product.html', context)
    
    


        
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
        
        
        
     
