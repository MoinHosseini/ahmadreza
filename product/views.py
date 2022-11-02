from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import materialForm,kalaForm,cartForm,userForm,factorForm
from .models import kala,material,cart,fcart

# Create your views here.

def home(request):
    ##### checked
    kc = kala.objects.all()
    mc = material.objects.all()
    return render(request,"homepage.html",{"kala":kc, "material":mc})

def all(request,type):
    ##### checked
    if type == "kala":
        content = kala.objects.all()
        return render(request,"product/all.html",{"content":content , "title" : "کالاها" , "type":"alter"})
    elif type == "material":
        content = material.objects.all()
        return render(request,"product/all.html",{"content":content , "title" : "مواد اولیه" , "type":"edit" })
    elif type == "cart":
        content = cart.objects.all()
        return render(request,"product/all.html",{"content":content , "title" : "سبد" , "type":"remove" , "e":"element" })

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

def remove(request,id):
    selected = cart.objects.get(id=id)
    if request.method == 'POST':
        selected.delete()
        return HttpResponseRedirect("/home")
    return render(request,'product/remove.html')

class factor(View):
    def post(self,request):
        form = factorForm(request.POST)
        if form.is_valid():
            content = fcart.objects.values()
            ld = {}
            for item in content:
                ld[item["element_id"]] = item["price"] * item["tedad"]
                obj = kala.objects.get(id = item["element_id"])
                obj.current_value_instorage -= item["tedad"]
                obj.total_value = obj.current_price * obj.current_value_instorage
                obj.save()
            form.instance.content = ld
            form.save()

    def get(self,request):
        form = factorForm()
        content = fcart.objects.all()
        return render(request,"add.html",{"form":form , "content" : content})


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
    ### for editting materials

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

            selected.total_value = selected.current_value_instorage * selected.current_price
            selected.save()
            
            return render(request,"product/all.html")        
    else:
        form = materialForm(instance=selected)
        return render(request,'change.html',{'form': form})

def alter(request,id):
    selected = kala.objects.get(id=id)
    if request.method == 'POST':
        form = kalaForm(request.POST, instance=selected)
        if form.is_valid():
            form.save()
            selected.total_value = selected.current_value_instorage * selected.current_price
            selected.save()
            return render(request,"product/all.html")        
    else:
        form = kalaForm(instance=selected)
        return render(request,'change.html',{'form': form})

def report(request):

    ## for having the total value of materials in storage
    
    mtv = material.objects.values_list("total_value")
    sum = 0
    for n in mtv:
        sum += n[0]
    mname = material.objects.values_list("name")
    names = []
    for name in mname:
        names.append(name[0])
    mvalue = material.objects.values_list("current_value_instorage")
    values = []
    for value in mvalue:
        values.append(value[0])
    mprice = material.objects.values_list("current_price")
    prices = []
    for price in mprice:
        prices.append(price[0])
    total = []
    for i,v in enumerate(prices):
        total.append(v * values[i])
    last = []
    for index,item in enumerate(names):
        mytuple = (names[index],prices[index],values[index],total[index])
        # price(mytuple)
        last.append(mytuple)
    columns = ["Name","Price","Tedad","Total"]
    return render(request,"report.html",{"mtv":sum, "col":columns,"last":last})