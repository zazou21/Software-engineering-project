from django.conf import settings
from django.urls import path
from. import views
from .views import childrenproductListView,product_view
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register_user, name='Register'),
    path('',views.Homepage,name='home'),
    path('aboutus',views.aboutus,name='about-us'),
    path('cart',views.cart,name='Cart'),
    path('myaccount', views.Myaccount, name='Myaccount'),
    path('forgetpass', views.Forgetpass, name='Forgetpass'),
    path('wishlist', views.Wishlist, name='Wishlist'),
    path('h',views.h,name='product'),
    path('product/<str:child_name>/<int:child_price>/<path:child_img>/<str:child_productID>',views.product_view, name='product-view'),
    
    path('boy', views.Boy, name='Boy'),
    path('girl',views.Girl,name='girl'),
    path('children',childrenproductListView.as_view(),name='children'),

    path('',views.logout_user,name='logout_user'),
    path('baby', views.baby, name='baby'),

]

