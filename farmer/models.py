from asyncio.windows_events import NULL
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.utils import timezone
from krishibhavan.models import *
from agro_service.models import *

# Create your models here.
class farmermanage(models.Model):
    panchayath=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    image=models.ImageField(default="none")
    email=models.EmailField(max_length=50)
    mobno=models.CharField(max_length=10)
    adharno=models.CharField(max_length=12)
    proof= models.ImageField(upload_to='image',default=NULL)
    pwd=models.CharField(max_length=30)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Acart(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()
    image=models.ImageField(upload_to='acart')
    agro=models.ForeignKey(Agro,on_delete=models.CASCADE,default='1')
    farmer=models.ForeignKey(farmermanage,on_delete=models.CASCADE,default='1')
    category=models.ForeignKey(ACateg,on_delete=models.CASCADE,default='1')
    status=models.BooleanField(default=False)
    date=models.DateField(default=timezone.now)


    def __str__(self):
        return self.name


class Kcart(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()
    image=models.ImageField(upload_to='kcart')
    krishi=models.ForeignKey(krishimanage,on_delete=models.CASCADE,default='1')
    farmer=models.ForeignKey(farmermanage,on_delete=models.CASCADE,default='1')
    category=models.ForeignKey(Categ,on_delete=models.CASCADE,default='1')
    status=models.BooleanField(default=False)
    date=models.DateField(default=timezone.now)


    def __str__(self):
        return self.name

class EchoProducts(models.Model):
    pname = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
    pdesc = models.TextField(blank=True)
    image = models.ImageField(upload_to='image')
    categ = models.TextField(default=0)
    farmer=models.ForeignKey(farmermanage,on_delete=models.CASCADE)




