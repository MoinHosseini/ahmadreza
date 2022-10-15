from django import forms
from .models import material,kala,measurement

class materialForm(forms.ModelForm):
    class Meta:
        model = material
        fields = '__all__'

class kalaForm(forms.ModelForm):
    class Meta:
        model = kala
        fields = '__all__'
        exclude = ('materials',)

class measureForm(forms.ModelForm):
    class Meta:
        model = measurement
        fields = '__all__'