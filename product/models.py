from django.db import models
from jsonfield import JSONField
# Create your models here.


class measure(models.Model):
    calc = models.FloatField(default=0)

class material(models.Model):
    name = models.CharField(max_length=50)
    current_value = models.FloatField(default=0)
    current_price = models.FloatField(default=0)

    def str(self):
        return self.name

class kala(models.Model):
    name = models.CharField(max_length=50)
    current_value = models.FloatField(default=0)
    current_price = models.FloatField(default=0)
    last_sell_price = models.FloatField(default=0)
    ingredients = models.ManyToManyField("material")
    share = models.ManyToManyField("measure")
    materials = JSONField()

    def str(self):
        return self.name


class calc(models.Model):
    class type(models.TextChoices):
        doone = "doone"
        geram = "geram" 
    element = models.ForeignKey(material,on_delete=models.CASCADE)
    typee = models.CharField(max_length=10,choices=type.choices,default=type.geram)
    value = models.FloatField(default=0,blank=True)
    name = models.CharField(max_length=10)