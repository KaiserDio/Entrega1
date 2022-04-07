from django import forms

class buscar_articulos_forms(forms.Form):

    nombre = forms.CharField(max_length=150)