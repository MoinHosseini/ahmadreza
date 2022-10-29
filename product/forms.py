from django import forms
from .models import material,kala,measurement,cart

class materialForm(forms.ModelForm):
    class Meta:
        model = material
        fields = '__all__'
        exclude = ('total_value',)

class kalaForm(forms.ModelForm):
    class Meta:
        model = kala
        fields = '__all__'
        exclude = ('materials','price_per_unit','total_value',)

class measureForm(forms.ModelForm):
    class Meta:
        model = measurement
        fields = '__all__'

class cartForm(forms.ModelForm):
    class Meta:
        model = cart
        fields = '__all__'