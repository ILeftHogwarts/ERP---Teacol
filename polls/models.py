from django.db import models

# Create your models here.


class CustomerRecord(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15, primary_key = True)
    add_phone = models.IntegerField()
    adress = models.CharField(max_length = 150)


class CustomerOrders(models.Model):
    id  = models.AutoField(primary_key = True)
    phone = models.ForeignKey(CustomerRecord, on_delete=models.CASCADE)
    preformance = models.CharField(max_length = 250)
    places = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)

class TheatreInfo(models.Model):
    id = models.AutoField(primary_key = True)
    preformance = models.CharField(max_length = 250)
    places = models.CharField(max_length = 50)
    price = models.CharField(max_length = 50)

    def __str__(self):
        return self.preformance + ' ' + self.places

