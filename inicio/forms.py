from django import forms

class CrearZapasForm(forms.Form):
    marca=forms.CharField(max_length=15)
    color = forms.CharField(max_length=15)
    talle = forms.IntegerField()
    precio = forms.IntegerField()
    
class BuscarZapasForm(forms.Form):
    marca=forms.CharField(max_length=15, required=False)
    color = forms.CharField(max_length=15, required=False)
    