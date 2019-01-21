from django.db import models


# Create your models here.

class Products(models.Model):
    pid = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    img = models.ImageField(upload_to='media')
    price = models.IntegerField()


'''create table products(pid varchar(30), name varchar(50), description varchar(150), imgurl varchar(200), price int)'''

'''insert into products(pid,name,description, imgurl, price) values ('111' , 'chair', 'its a red very big chair', 'image ka url', 800);'''