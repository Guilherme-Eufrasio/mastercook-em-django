from django.shortcuts import render, get_object_or_404
from .models import Pessoa
from mastercook.area_administrativa.models import Receita

# Create your views here.
def home(request):
    return render(request, 'index.html')

# def lista_pessoa(request):
#     pessoas= Pessoa.objects.all().order_by('nome')
#     return render(request, 'pessoas.html', {'pessoas': pessoas})

# def detalhe_pessoa(request, id):
#     pessoa = get_object_or_404(Pessoa, id=id)
#     return render(request, 'pessoa_detalhe.html', {'pessoa': pessoa})

def logar(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastro.html')

def popular(request):
    receitas_populares = Receita.objects.filter(popular=True, ativa=True)
    print(receitas_populares)
    return render(request, 'receitas/populares.html', {'receitas_populares': receitas_populares})

def simples(request):

    receitas_simples = Receita.objects.filter(popular=False, ativa=True)
    print(receitas_simples[0].popular)


    return render(request, 'receitas/simples.html', {'receitas_simples': receitas_simples})

def salgados(request):
    receitas_salgadas = Receita.objects.filter(categoria='S', ativa=True)
    return render(request, 'receitas/salgado.html', {'receitas_salgadas': receitas_salgadas})

def doces(request):
    receitas_doces = Receita.objects.filter(categoria='D', ativa=True)
    return render(request, 'receitas/doces.html', {'receitas_doces': receitas_doces})

def criadores(request):
    return render(request, 'sobre.html')

def homeUser(request):
    return render(request, 'homeUsuario.html')