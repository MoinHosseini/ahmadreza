from django import forms
from .models import material,kala,cart,user,factor,fcart
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget



class materialForm(forms.ModelForm):
    class Meta:
        model = material
        fields = '__all__'
        exclude = ('total_value','all_dates','all_values',)
        labels = {
        "name": "نام",
        "current_value_instorage": "مقدار در انبار",
        "current_price": "قیمت فعلی",
        "total_value": "جمع ارزش کل در انبار",
        "min_value" : "کمترین میزان مورد قبول در انبار",
        "expire_date" : "تاریخ انقضا",   

    }
    def __init__(self, *args, **kwargs):
        super(materialForm, self).__init__(*args, **kwargs)
        self.fields['expire_date'] = JalaliDateField( label=('تاریخ انقضا'), widget=AdminJalaliDateWidget )


class kalaForm(forms.ModelForm):
    class Meta:
        model = kala
        fields = '__all__'
        exclude = ('materials','total_value',)
        labels = {
        "name": "نام",
        "current_price": "قیمت فعلی",
        "price_per_unit" : "قیمت تمام شده برای هر واحد",
        "materials" : "موارد تشکیل دهنده",
    }


class cartForm(forms.ModelForm):
    class Meta:
        model = cart
        fields = '__all__'
        labels = {
        "element": "ماده اولیه",
        "impact": "درصد تاثیر",
        }

class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        
        labels = {
        "nid": "کد کاربری",
        "phone": "موبایل",
        "rank": "رده سازمانی",
        }

class factorForm(forms.ModelForm):
    class Meta:
        model = factor
        fields = '__all__'
        exclude = ('content','active_user','fact_type',)
        labels = {
        "user": "ثبت کننده",
        "issue_date" : "تاریخ صدور",
        }
    def __init__(self, *args, **kwargs):
        super(factorForm, self).__init__(*args, **kwargs)
        self.fields['issue_date'] = JalaliDateField( label=('تاریخ صدور'), widget=AdminJalaliDateWidget )

class fcartForm(forms.ModelForm):
    class Meta:
        model = fcart
        fields = '__all__'
        labels = {
        "element": "کالا",
        "tedad": "تعداد",
        "price": "قیمت",
        "expire_date" : "تاریخ انقضا",
        }
    def __init__(self, *args, **kwargs):
        super(fcartForm, self).__init__(*args, **kwargs)
        self.fields['expire_date'] = JalaliDateField( label=('تاریخ انقضا'), widget=AdminJalaliDateWidget )

