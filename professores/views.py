#from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from professores.models import Professor

def index(request):

    context = {"caracteristicas":None}
    if "buscar" in request.GET:
        professores = Professor.objects.all()
        professor_pesquisado = request.GET["buscar"]
        caracteristicas = professores.filter(nome_professor__icontains = professor_pesquisado)
        context = {
            "caracteristicas":caracteristicas
        }

    return render(request,'index.html', context)