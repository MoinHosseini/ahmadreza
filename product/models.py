from django.db import models
from jsonfield import JSONField
# Create your models here.

class material(models.Model):
    name = models.CharField(max_length=50)
    current_value_instorage = models.FloatField(default=0)
    current_price = models.IntegerField(default=0)
    total_value = models.IntegerField(default=0)
    min_value = models.IntegerField(default=0)
    expire_date = models.DateField(blank=True)
    all_dates = JSONField()
    
    def __str__(self):
        return self.name


class kala(models.Model):

    name = models.CharField(max_length=50)
    current_price = models.IntegerField(default=0)
    price_per_unit = models.IntegerField(blank = True)
    materials = JSONField()

    def __str__(self):
        return self.name

class cart(models.Model):
    element = models.ForeignKey(material, on_delete=models.CASCADE)
    impact = models.FloatField(default=0)

    def __str__(self):
        return self.element.name

class user(models.Model):
    name = models.CharField(max_length=50)
    nid = models.CharField(max_length = 15)
    phone = models.CharField(max_length=15)
    rank = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class factor(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    content = JSONField()
    issue_date = models.DateField(blank=True)
    active_user = models.CharField(max_length=100)
    fact_type = models.CharField(max_length=10)

    def __str__(self):
        return str(self.pk)

class fcart(models.Model):
    element = models.ForeignKey(material, on_delete=models.CASCADE)
    tedad = models.FloatField(default=0)
    price = models.IntegerField(default=0)
    expire_date = models.DateField()
    def __str__(self):
        return self.element.name

