from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
	saludo = "hola proyecto2"
	pagina_html = HttpResponse(saludo) 
	return pagina_html

def saludar_con_html(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='control.estudios/base.html',
        context=contexto,
    )
    return http_responde