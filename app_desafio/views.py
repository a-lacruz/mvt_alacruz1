from ast import Return
from django.http import HttpResponse
from django.template import loader
from app_desafio.models import Familiar

# Create your views here.

def listar_familiar(request):
    family = Familiar.objects.all()
    diccionario = {'app_desafio': family}
    plantilla = loader.get_template('listado_familia.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)