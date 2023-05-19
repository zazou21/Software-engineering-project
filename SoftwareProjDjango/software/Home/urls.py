from django.conf import settings
from django.urls import path
from. import views
from .views import childrenproductListView,product_view,babyproductListView,baby_view,accessoriesproductListView,accessories_view,toddlerproductListView,toddler_view
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
    path('product/<str:child_name>/<int:child_price>/<path:child_img>/<str:child_productID>/<int:idd>',views.product_view, name='product-view'),
    
    path('boy', views.Boy, name='boy'),
    path('girl',views.Girl,name='girl'),
    path('children',childrenproductListView.as_view(),name='children'),

    path('',views.logout_user,name='logout'),

    path('baby', babyproductListView.as_view(), name='baby'),
    path('babyproduct/<str:baby_name>/<int:baby_price>/<path:baby_img>/<str:baby_productID>/<int:iddd>',views.baby_view, name='baby-view'),

    path('accessories', accessoriesproductListView.as_view(), name='accessories'),
    path('accessories/<str:accessories_name>/<int:accessories_price>/<path:accessories_img>/<str:accessories_productID>/<int:idddd>',views.accessories_view, name='accessories-view'),

    path('toddler', toddlerproductListView.as_view(), name='toddler'),
    path('toddler/<str:toddler_name>/<int:toddler_price>/<path:toddler_img>/<str:toddler_productID>/<int:iddddd>',views.toddler_view, name='toddler-view'),


    path('add_to_cart',views.addToCart,name='addtocart'),
    path('delete-item',views.removeFromCart,name='removeCart'),
    path('add-to-wishlist',views.addwishlist,name='')


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

