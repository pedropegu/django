import email
import re
from types import MethodDescriptorType, MethodType
from django.shortcuts import render
from .forms import ReggForm
from .models import Registrado
# Create your views here.
def inicio(request):
    form = ReggForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        correo = form_data.get("email")
        usuario = form_data.get("nombre")
        obj = Registrado.objects.create(email=correo, nombre=usuario)
    context = {
        "form":form,
    }
    return render(request, "index.html", context)