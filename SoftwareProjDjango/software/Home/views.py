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
    cartobjects=Cart.objects.filter(user=request.user)


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

def product_view(request,child_name,child_price,child_img,child_productID,idd):
    product = get_object_or_404(childrenproduct, productID=child_productID)
    context = {
        'child_name': child_name,
        'child_price': child_price,
        'child_img': child_img,
        'product': product,
        'idd': idd,
        'colors': product.product_attributes.first().colors.all(),
        'sizes': product.product_attributes.first().sizes.all(),
       
    }
    return render(request, 'Home/product.html', context)



def baby_view(request,baby_name,baby_price,baby_img,baby_productID,iddd):
    product = get_object_or_404(babyproduct, productID=baby_productID)
    context = {
        'baby_name': baby_name,
        'baby_price': baby_price,
        'baby_img': baby_img,
        'product': product,
        'iddd': iddd,
        'colors': product.baby_attributes.first().colors.all(),
        'sizes': product.baby_attributes.first().sizes.all(),
       
    }
    return render(request, 'Home/babyproduct.html', context)
    

class babyproductListView(ListView):
    model=babyproduct
    context_object_name='baby'


def accessories_view(request,accessories_name,accessories_price,accessories_img,accessories_productID,idddd):
    product = get_object_or_404(accessoriesproduct, productID=accessories_productID)
    context = {
        'accessories_name': accessories_name,
        'accessories_price': accessories_price,
        'accessories_img': accessories_img,
        'product': product,
        'idddd': idddd,
        'colors': product.accessories_attributes.first().colors.all(),
        'sizes': product.accessories_attributes.first().sizes.all(),
       
    }
    return render(request, 'Home/accessoriesproduct.html', context)
    

class accessoriesproductListView(ListView):
    model=accessoriesproduct
    context_object_name='accessories'



def toddler_view(request,toddler_name,toddler_price,toddler_img,toddler_productID,iddddd):
    product = get_object_or_404(toddlerproduct, productID=toddler_productID)
    context = {
        'toddler_name': toddler_name,
        'toddler_price': toddler_price,
        'toddler_img': toddler_img,
        'product': product,
        'iddddd': iddddd,
        'colors': product.toddler_attributes.first().colors.all(),
        'sizes': product.toddler_attributes.first().sizes.all(),
       
    }
    return render(request, 'Home/toddlerproduct.html', context)
    

class toddlerproductListView(ListView):
    model=toddlerproduct
    context_object_name='toddler'
    


        
def logout_user(request):
     logout(request)
     return render('Home/index.html')

   
    

            
            
            

def Forgetpass(request):
    return render(request,'Home/Forgetpass.html')

def Wishlist(request):
    wishlistobjects=wishlist.objects.filter(user=request.user)

    return render(request,'Home/wishlist.html',{
        'items':wishlistobjects
    })


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

def addToCart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                 messages.success(request,"already in cart")
            else:     
                Cart.objects.create(user=request.user,product_id=prod_id)
        else:
            messages.success(request,"not logged in")  
              
    
    return redirect('home')

def removeFromCart(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
            cartitem=Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
    return redirect('home')

        



def addwishlist(request):
    if request.method=='POST':
         if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                 messages.success(request,"already in wishlist")
            else:
                wishlist.objects.create(user=request.user,product_id=prod_id)
    return redirect('home')

       

        
        
        
     
