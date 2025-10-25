from .models import *
from django import forms



class EProdforms(forms.ModelForm):
    class Meta:
        model =EchoProducts
        fields = ['pname', 'pdesc', 'stock', 'price']