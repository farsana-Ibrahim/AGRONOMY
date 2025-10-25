from django.db import models
from asyncio.windows_events import NULL
from django.utils import timezone
from farmer.models import *

# Create your models here.
class Clientmanage(models.Model):
    panchayath=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobno=models.CharField(max_length=10)
    pwd=models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Ecart(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()
    image=models.ImageField(upload_to='ecart')
    farmer=models.ForeignKey(farmermanage,on_delete=models.CASCADE,default='1')
    client=models.ForeignKey(Clientmanage,on_delete=models.CASCADE,default='1')
    status=models.BooleanField(default=False)
    date=models.DateField(default=timezone.now)


    def __str__(self):
        return self.name

