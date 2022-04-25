import email
import re
from types import MethodDescriptorType, MethodType
from django.shortcuts import render
from .forms import ReggForm,RegModelForm
from .models import Registrado
# Create your views here.
def inicio(request):

    titulo = "Hola"
    

    if request.user.is_authenticated:
        titulo = "Bienvenido {}".format(request.user)


    form = RegModelForm(request.POST or None)
    context = {
        "titulo":titulo,
        "form":form,
    }

    if form.is_valid():

        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        
        if not instance.nombre:
            instance.nombre = "persona"
        instance.save()


        if not nombre:
            nombre = "anonimo"

        context = {
            "titulo": "Gracias {}".format(nombre)
        }

        # form_data = form.cleaned_data
        # correo = form_data.get("email")
        # usuario = form_data.get("nombre")
        # obj = Registrado.objects.create(email=correo, nombre=usuario)

    return render(request, "index.html", context)