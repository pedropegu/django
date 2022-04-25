
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import RegModelForm, ContactForm
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
        print(email)
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

def contacto(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        
        email = form.cleaned_data.get("email")
        nombre = form.cleaned_data.get("nombre")
        mensaje = form.cleaned_data.get("mensaje")
        
        asunto = "Django Contacto"
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from,"otroemail@gmail.com"]
        send_mail(asunto,
        mensaje,
        email_from,
        email_to,
        fail_silently=True
        )
        
    context = {
        "form":form
    }
    return render(request,"contact.html",context)