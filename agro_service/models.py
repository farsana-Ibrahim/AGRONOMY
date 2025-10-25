from django.db import models

# Create your models here.
class Agro(models.Model):
    agroname=models.CharField(max_length=200)
    image=models.ImageField(default="none")
    email=models.EmailField(max_length=50)
    mobno=models.CharField(max_length=10)
    pwd=models.CharField(max_length=30)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.agroname

class ACateg(models.Model):
    name=models.CharField(max_length=200)
    agro=models.ForeignKey(Agro,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AProducts(models.Model):
    pname = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
    pdesc = models.TextField(blank=True)
    image = models.ImageField(upload_to='image')
    category=models.ForeignKey(ACateg,on_delete=models.CASCADE,default='1')
    agro=models.ForeignKey(Agro,on_delete=models.CASCADE,default='1')

    def __str__(self):
        return self.pname