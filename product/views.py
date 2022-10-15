from django.shortcuts import render
from django.views import View
from .forms import materialForm,kalaForm
from .models import kala,material

# Create your views here.
def all(request):
    return render(request,"add.html")

class add(View):
    def get(self,request,type):
        
        if type == "kala":
            form = kalaForm()
        elif type == "material":
            form = materialForm()
        return render(request,'add.html',{"form":form})
    
    def post(self,request,type):
        if type == "kala":
            form = kalaForm(request.POST)
        elif type == "material":
            form = materialForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request,"all.html")

def create(request):
    if request.method == "POST":
        pass
    else:
        pass

class CartView(View):
    # for adding items to cart
    
    def get(self,request):
        form = materialForm()
        content = material.objects.values()
        
        a = {}
        b = {}
        c = {}

        for item in content:
            a[str(item["id"])] = item["name"]
            b[str(item["id"])] = item["current_price"]
        return render(request,"product/create.html",{
            "form":form,
            "a" : a,
            "b" : b,
            })

    def post(self,request):
        form = materialForm()(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"product/create.html",{"form":form})
