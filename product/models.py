from unittest.util import _MAX_LENGTH
from django.db import models
from jsonfield import JSONField
# Create your models here.

class material(models.Model):
    name = models.CharField(max_length=50)
    current_value_instorage = models.FloatField(default=0)
    current_price = models.FloatField(default=0)
    total_value = models.FloatField(default=0)
    
    def __str__(self):
        return self.name

class kala(models.Model):

    name = models.CharField(max_length=50)
    current_value_instorage = models.FloatField(default=0)
    current_price = models.FloatField(default=0)
    total_value = models.FloatField(default=0)
    price_per_unit = models.FloatField()
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

class fcart(models.Model):
    element = models.ForeignKey(kala, on_delete=models.CASCADE)
    tedad = models.FloatField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.element.name