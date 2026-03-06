# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>¡Bienvenido a Alke Solutions!</h1><p>Esta es la página principal de Alke Web Base.</p>")