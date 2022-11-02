from django.contrib import admin
from .models import kala,material,cart,user,factor,fcart

# Register your models here.

admin.site.register(kala)
admin.site.register(material)
admin.site.register(cart)
admin.site.register(user)
admin.site.register(factor)
admin.site.register(fcart)