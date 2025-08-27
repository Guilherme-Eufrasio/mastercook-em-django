from django.shortcuts import render, get_object_or_404
from .models import Pessoa

# Create your views here.
def home(request):
    return render(request, 'index.html')

def lista_pessoa(request):
    pessoas= Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def detalhe_pessoa(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request, 'pessoa_detalhe.html', {'pessoa': pessoa})

def logar(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastro.html')

def popular(request):
    return render(request, 'maispopu.html')

def simples(request):
    return render(request, 'popusimples.html')

def salgados(request):
    return render(request, 'salgado.html')