from django import forms
from .models import material,kala,measure

class materialForm(forms.ModelForm):
    class Meta:
        model = material
        fields = "all"

class kalaForm(forms.ModelForm):
    class Meta:
        model = kala
        fields = "all"
        exclude = ('materials',)

class measureForm(forms.ModelForm):
    class Meta:
        model = measure
        fields = "all"