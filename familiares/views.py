from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context, loader
from familiares.models import familiares

# Create your views here.

def familiar_view(request):
    familiar = familiares.objects.all()
    
    template = loader.get_template(r"C:\Users\agust\OneDrive\Documentos\Cursos\Curso python\Django\Entrega desafio\entrega_18\entrega_18\templates\index.html")
    
    info = {"familiar": familiar}     
    
    template = loader.get_template(r"C:\Users\agust\OneDrive\Documentos\Cursos\Curso python\Django\Entrega desafio\entrega_18\entrega_18\templates\index.html")

    documento = template.render(info)

    return HttpResponse(documento)