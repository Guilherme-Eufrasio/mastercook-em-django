from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request, "index-area-restrita.html")

@login_required
def adm(request):
    return render(request, 'administrativo.html')


@login_required
def cadastrar_receita(request):
    return render(request, "receitas/cadastrar.html")

def editar_receita(request, id):
    return render(request, "receitas/editar.html")
