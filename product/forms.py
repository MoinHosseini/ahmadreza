from django import forms
from .models import material,kala,cart,user,factor

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

class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

class factorForm(forms.ModelForm):
    class Meta:
        model = factor
        fields = '__all__'
        exclude = ('content',)