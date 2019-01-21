from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mobile = models.CharField(max_length=12)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)
    pincode = models.IntegerField()
    location = models.CharField(max_length=500)
    city = models.CharField(max_length=50)


class address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE())
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    pin = models.IntegerField()
    area = models.CharField(max_length=500)
    town = models.CharField(max_length=50)
