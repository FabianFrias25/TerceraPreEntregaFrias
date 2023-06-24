from django import forms

class FormsBuscarEquipos(forms.Form):
    nombre = forms.CharField(max_length=100)