from django.contrib import admin
from .models import childrenproduct,productAttribute,Color,Cart,Size

# Register your models here.
admin.site.register(childrenproduct)
admin.site.register(productAttribute)
admin.site.register(Color)
admin.site.register(Cart)
admin.site.register(Size)
