from django.urls import path
from. import views
urlpatterns = [
    path('register', views.register_user, name='Register'),
    path('',views.Homepage,name='home'),
    path('aboutus',views.aboutus,name='about-us'),
    path('cart',views.Cart,name='Cart'),
    path('myaccount', views.Myaccount, name='Myaccount'),
    path('forgetpass', views.Forgetpass, name='Forgetpass'),
    path('wishlist', views.Wishlist, name='Wishlist'),
    
    path('boy', views.Boy, name='Boy'),
    path('girl',views.Girl,name='girl'),
    path('children',views.children,name='children'),
    path('product',views.product,name='product'),
    path('',views.logout_user,name='logout_user'),
    path('baby', views.baby, name='baby'),

]