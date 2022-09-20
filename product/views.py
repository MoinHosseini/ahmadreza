from django.shortcuts import render
from django.views import View
# from .forms import materialForm,kalaForm


# Create your views here.

def all(request):
    return render(request,"add.html")

class add(View):
    def get(self,request):
        form = kalaForm()
        return render(request,'add.html',{"form":form})

    def post(self,request):
        form = kalaForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"add.html")