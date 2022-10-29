from django import forms
from .models import material,kala,cart

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


class cartForm(forms.ModelForm):
    class Meta:
        model = cart
        fields = '__all__'