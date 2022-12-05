from ast import Return
from django.http import HttpResponse
from django.template import Template, context, loader
from app_desafio.models import Familiar

# Create your views here.

def listar_familiar(request):
    queryset = Familiar.objects.all()
    diccionario = {'app_desafio': queryset}
    plantilla = loader.get_template('familiar_listado.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)