from django.contrib import admin
from .models import kala,material,measurement,cart

# Register your models here.

admin.site.register(kala)
admin.site.register(material)
admin.site.register(measurement)
admin.site.register(cart)