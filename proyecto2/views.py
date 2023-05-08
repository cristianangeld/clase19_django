from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
	saludo = "hola proyecto2"
	pagina_html = HttpResponse(saludo) 
	return pagina_html