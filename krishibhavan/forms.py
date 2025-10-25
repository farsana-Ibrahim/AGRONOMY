from .models import *
from django import forms



class Prodforms(forms.ModelForm):
    class Meta:
        model =Products
        fields = ['pname', 'pdesc', 'stock', 'price']



