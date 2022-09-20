from django.contrib import admin
from .models import kala,material,measure,calc

# Register your models here.

admin.site.register(kala)
admin.site.register(material)
admin.site.register(measure)
admin.site.register(calc)