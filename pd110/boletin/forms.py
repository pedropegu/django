from xml.dom import NoModificationAllowedErr
from django import forms

class ReggForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    edad = forms.IntegerField()