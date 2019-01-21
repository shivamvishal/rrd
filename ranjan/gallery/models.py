from django.db import models


# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    timestamp = models.DateField()
    img = models.ImageField(upload_to='media')


'''create table gallerydata(
    imgid int not null auto_increment,
    image longblob,
    title varchar(50),
    primary key (imgid));
'''

