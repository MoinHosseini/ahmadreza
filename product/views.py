from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import materialForm,kalaForm,cartForm
from .models import kala,material,cart

# Create your views here.

def home(request):
    ##### checked
    content = material.objects.all()
    return render(request,"homepage.html")


def all(request):
    ##### checked
    content = material.objects.all()
    return render(request,"product/all.html",{"content":content})

class add(View):
    ##### checked
    ## adds material ##
    def get(self,request):
        form = materialForm()
        return render(request,'add.html',{"form":form})
    
    def post(self,request):
        form = materialForm(request.POST)
        if form.is_valid():
            form.instance.total_value = form.cleaned_data["current_value_instorage"] * form.cleaned_data["current_price"]
            form.save()
        return render(request,"product/all.html")

class CartView(View):
    ##### checked
    ## adds materials of a complex to the cart ##
    
    def get(self,request):
        form = cartForm()
        return render(request,"product/addtocart.html",{"form":form})

    def post(self,request):
        form = cartForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"product/create.html",{"form":form})

def checkcart(request):
    ##### checked
    content = cart.objects.all()
    return render(request,"product/check.html",{"content":content})

def create(request):
    ##### checked
    ## creates a new complex ##
    if request.method == "POST":
        form = kalaForm(request.POST)
        if form.is_valid():
            content = cart.objects.values()
            ld = {}
            sum = 0
            for item in content:
                ld[item["element_id"]] = item["impact"]
                obj = material.objects.get( id = item["element_id"] )
                price = getattr(obj, "current_price")
                sum = sum + ( (price * item["impact"]) / 100 )
            form.instance.total_value = form.cleaned_data["current_value_instorage"] * form.cleaned_data["current_price"]
            form.instance.price_per_unit = sum
            form.instance.materials = ld
            form.save()
            return render(request, "product/check.html")
    else:
        form = kalaForm()
        return render(request, "product/create.html",{"form":form})

def edit(request,id):
    selected = material.objects.get(id=id)
    cp = selected.current_price
    if request.method == 'POST':
        form = materialForm(request.POST, instance=selected)
        if form.is_valid():
            np = selected.current_price
            if cp != np:
                np = np - cp
                data = kala.objects.values_list("materials")
                names = kala.objects.values_list("name")
                print(names)
                final = []
                for n in names:
                    final.append(n[0])
                for index,item in enumerate(data):
                    op = item[0]
                    if str(id) in op:
                        impact = op[str(id)] / 100
                        change = impact * np
                        under_operation_kala = kala.objects.get( name = final[index] )
                        under_operation_kala.price_per_unit += change
                        under_operation_kala.save()
            form.save()

            selected.total_value = selected.current_value_instorage *selected.current_price
            selected.save()
            
            return render(request,"product/all.html")        
    else:
        form = materialForm(instance=selected)
        return render(request,'change.html',{'form': form})

def report(request,id):
    if id == 1:
        ktv = kala.objects.values_list("total_value")
        mtv = material.objects.values_list("total_value")
    elif id == 2:
        pass
    elif id == 3:
        pass