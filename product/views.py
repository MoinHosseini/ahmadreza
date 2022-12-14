from django.shortcuts import render
from django.views import View
from .forms import materialForm,kalaForm,cartForm,factorForm,fcartForm
from .models import kala,material,cart,fcart,factor as fucktor
import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def home(request):
    return render(request,"homepage.html")


@login_required
def all(request,type):

    if type == "kala":
        content = kala.objects.all()
        return render(request,"product/all.html",{"content":content , "title" : "کالاها" , "type":"alter"})
    
    elif type == "material":
        content = material.objects.all()
        return render(request,"product/all.html",{"content":content , "title" : "مواد اولیه" , "type":"edit" })    
    
    elif type == "cart":
        content = cart.objects.all()
        return render(request,"product/all.html",{"content":content , "title" : "محتویات سبد" , "type":"remove/cart" })
    
    elif type == "factor":
        content = fucktor.objects.all().order_by("-id")
        return render(request,"product/all.html",{"content":content , "title" : "فاکتورها"  , "type":"view" })
    
    elif type == "fcart":
        content = fcart.objects.all()
        return render(request,"product/all.html",{"content":content , "title" : "مواد اولیه" , "type":"removefcart" })

class add(View):
    def get(self,request):
        form = materialForm()
        return render(request,'add.html',{"form":form})
    
    def post(self,request):
        form = materialForm(request.POST)
        if form.is_valid():
            form.instance.total_value = form.cleaned_data["current_value_instorage"] * form.cleaned_data["current_price"]
            # t = len(form.instance.all_dates)
            a = {}
            a[0] = form.cleaned_data["expire_date"]
            form.instance.all_dates = a             
            b = {}
            b[0] = form.cleaned_data["current_value_instorage"]
            form.instance.all_values = b 

            
            form.save()
            return render(request,"homepage.html")


class CartView(View):
    def get(self,request):
        form = cartForm()
        return render(request,"product/addtocart.html",{"form":form})

    def post(self,request):
        form = cartForm(request.POST)
        if form.is_valid():
            form.save()
        form = cartForm()
        return render(request,"product/addtocart.html",{"form":form})

@login_required
def create(request):
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
            form.instance.price_per_unit = sum
            form.instance.materials = ld
            form.save()
            cart.objects.all().delete()
            return render(request, "homepage.html")
    else:
        form = kalaForm()
        return render(request, "product/create.html",{"form":form})


@login_required
def checkcart(request):
    content = cart.objects.all()
    return render(request,"product/check.html",{"content":content})


@login_required
def remove(request,type,id):
    if type == "cart":
        selected = cart.objects.get(id=id)
           
    elif type == "material":
        selected = material.objects.get(id=id)
    
    elif type == "kala":
        selected = kala.objects.get(id=id) 
    
    if request.method == 'POST':
        selected.delete()
        return render(request,"homepage.html")
    return render(request,'delete.html')

@login_required
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
            return render(request,"homepage.html")        
    else:
        form = materialForm(instance=selected)
        return render(request,'edit.html',{'form': form , "type":"material", "id":id})


@login_required
def alter(request,id):
    selected = kala.objects.get(id=id)
    content = selected.materials
    a = {}
    for k, v in content.items():
        a[str(material.objects.get(id = int(k)))] = str(v)
        
    if request.method == 'POST':
        form = kalaForm(request.POST, instance=selected)
        if form.is_valid():
            form.save()
            return render(request,"homepage.html")
    else:
        form = kalaForm(instance=selected)
        return render(request,'edit.html',{'form': form , "type":"kala", "id":id , "materials":a})


@login_required
def report(request):
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
    columns = ["نام","قیمت فی","تعداد","جمع"]
    return render(request,"report.html",{"mtv":sum, "col":columns,"last":last , "active":True})


@login_required
def report2(request):
    mname = kala.objects.values_list("name")
    names = []
    for name in mname:
        names.append(name[0])
    mvalue = kala.objects.values_list("price_per_unit")
    values = []
    for value in mvalue:
        values.append(value[0])
    mprice = kala.objects.values_list("current_price")
    prices = []
    for price in mprice:
        prices.append(price[0])
    last = []
    for index,item in enumerate(names):
        mytuple = (names[index],prices[index],values[index])
        # price(mytuple)
        last.append(mytuple)
    columns = ["نام","قیمت فی","قیمت تمام شده"]
    return render(request,"report.html",{"mtv":sum, "col":columns,"last":last})


@login_required
def factor(request,type):
    if request.method == "POST":
        if type == "in":
            form = factorForm(request.POST)
            if form.is_valid():
                contents = fcart.objects.values()
                ld = {}
                for item in contents:
                    obj = material.objects.get(id = int(item["element_id"]))
                    ld[  obj.name   ] = "Price : " + str(item["price"]) + " Tedad : " + str(item["tedad"])
                    cp = obj.current_price
                    obj.current_price = int(item["price"])
                    obj.current_value_instorage += item["tedad"]
                    obj.total_value = obj.current_price * obj.current_value_instorage
                    
                    
                    t = int(max((obj.all_dates.keys())))
                    obj.all_dates[t+1] = item["expire_date"]
                    obj.all_values[t+1] = item["tedad"]

                    
                    if (cp != int(item["price"]) ):
                        np =  int(item["price"])
                        np = np - cp
                        data = kala.objects.values_list("materials")
                        names = kala.objects.values_list("name")
                        final = []
                        for n in names:
                            final.append(n[0])
                        for index,va in enumerate(data):
                            op = va[0]
                            if str(item["element_id"]) in op:
                                impact = op[str(item["element_id"])] / 100
                                change = impact * np
                                under_operation_kala = kala.objects.get( name = final[index] )
                                under_operation_kala.price_per_unit += change
                                under_operation_kala.save()
                    obj.save()
                form.instance.content = ld
                form.instance.active_user =  request.user
                form.instance.fact_type = "ورود"
                form.save()
                fcart.objects.all().delete()
                return render(request,"homepage.html")
        elif type == "out":
            form = factorForm(request.POST)
            if form.is_valid():
                contents = fcart.objects.values()
                ld = {}
                for item in contents:
                    obj = material.objects.get(id = int(item["element_id"]))
                    ld[  obj.name   ] = "Price : " + str(item["price"]) + " Tedad : " + str(item["tedad"])
                    obj.current_value_instorage -= item["tedad"]
                    obj.total_value = obj.current_price * obj.current_value_instorage

                    dada = (item["expire_date"]).strftime("%y-%m-%d")
                    
                    for k,v in obj.all_dates.items():
                        if dada in v:
                            obj.all_values[k] -= item["tedad"]
                            if obj.all_values[k] <=0 :
                                obj.all_dates.pop(k)
                                obj.all_values.pop(k)
                            break

                    obj.save()
                form.instance.content = ld
                form.instance.active_user =  request.user
                form.instance.fact_type = "خروج"
                form.save()
                # fcart.objects.all().delete()
                return render(request,"homepage.html")
    elif request.method == "GET":
        form = factorForm()
        content = fcart.objects.all()
        return render(request,"add.html",{"form":form , "content" : content})


@login_required
def factoring(request):
    if request.method=="GET":
        form = fcartForm()
        return render(request,"product/factoring.html",{"form":form})
    else:
        form = fcartForm(request.POST)
        if form.is_valid():
            form.save()
        form = fcartForm()
        return render(request,"product/factoring.html",{"form":form})


@login_required
def checkfactor(request):
    content = fcart.objects.all()
    return render(request,"product/checkfactor.html",{"content":content})


@login_required
def removefcart(request,id):
    selected = fcart.objects.get(id=id)
    if request.method == 'POST':
        selected.delete()
        return render(request,"homepage.html")
    return render(request,'delete.html')


@login_required
def factor_content(request,id):
    obj = fucktor.objects.get(id = id)
    user = getattr(obj, "user")
    content = getattr(obj, "content")
    issue_date = getattr(obj, "issue_date")
    active_user = getattr(obj, "active_user")
    fact_type = getattr(obj, "fact_type")
    return render(request,"product/myview.html",{"user":user , "content" : content ,
     "issue_date" : issue_date, "active_user":active_user , "fact_type":fact_type })


@login_required
def notif(request,type):
    if type == "value":
        box = []
        final = []
        mv = material.objects.values_list("min_value")
        cv = material.objects.values_list("current_value_instorage")
        names = material.objects.values_list("name")
        for name in names:
            final.append(name[0])
        for index,item in enumerate(mv):
            if item >= cv[index]:
                box.append( str(final[index]) + " --- >" + "  مقدار فعلی = " + str(cv[index][0]) )
        return render(request,'product/notif.html',{"title":"اخطار موجودی", "content":box, "datep" : False})        
    
    elif type == "date":
        current_date = datetime.date.today()
        list = material.objects.filter(expire_date = current_date)
        return render(request,'product/notif.html',{"title":"اخطار تاریخ", "content":list , "current_date":current_date, "datep" : True})


@login_required
def editdate(request,item):
    if request.method == "GET":
        selected = material.objects.get(name = item)
        msg=""
        if len(selected.all_dates) == 0:
            msg = "خطایی رخ داده است.. این کالا دارای تاریخ انقضای دیگری نیست ."
        return render(request,'delete.html',{"msg":msg})
    elif request.method == "POST":
        selected = material.objects.get(name = item)
        if len(selected.all_dates) == 0:
            return render(request,"homepage.html")
        temp = selected.all_dates.pop(list(selected.all_dates.keys())[0])
        if len(selected.all_dates) == 0:
            selected.expire_date = temp
        else:
            selected.expire_date = selected.all_dates [ list(selected.all_dates.keys())[0] ]
        selected.save()
        return render(request,"homepage.html")