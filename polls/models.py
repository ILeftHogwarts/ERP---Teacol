from django.db import models

# Create your models here.


class TheatreInfo(models.Model):
    id = models.AutoField(primary_key = True)
    preformance = models.CharField(max_length = 250)
    places = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)


class CustomerRecord(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15, primary_key = True)
    add_phone = models.CharField(max_length = 15)
    adress = models.CharField(max_length = 150)
    orders = models.ManyToManyField(TheatreInfo)


