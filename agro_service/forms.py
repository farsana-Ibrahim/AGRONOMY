from .models import *
from django import forms


class AProdforms(forms.ModelForm):
    class Meta:
        model =AProducts
        fields = ['pname', 'pdesc', 'stock', 'price']
