from django.db import models

# Create your models here.

class CustomerOrders(models.Model):
    phone = models.IntegerField(primary_key = True)
    preformance = models.CharField(max_length = 250)
    places = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)

class CustomerRecord(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    phone = models.ForeignKey(CustomerOrders, on_delete = models.CASCADE)
    add_phone = models.IntegerField()
    adress = models.CharField(max_length = 150)

class TheatreInfo(models.Model):
    id = models.AutoField(primary_key = True)
    preformance = models.CharField(max_length = 250)
    places = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)