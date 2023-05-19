from django.shortcuts import get_object_or_404, render,redirect
from django import forms
from django.forms.forms import Form  
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import registration
from django.views.generic import ListView
from .models import childrenproduct,Cart

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
    return render(request,'Home/cart.html')

def newcart(request):
    return render(request,'Home/newcart.html')

class cartListView(ListView):
    model=Cart
    # context_object_name='cart'
    template_name = 'Home/newcart.html'

    # def get_queryset(self):
    #     return Cart.objects.all()







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
        'colors': product.product_attributes.first().colors.all(),
        'sizes': product.product_attributes.first().sizes.all(),
    }
    return render(request, 'Home/product.html', context)


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
            Cart.objects.create(user=request.user,product_id=prod_id)
    
    return redirect('home')




       

        
        
        
     
