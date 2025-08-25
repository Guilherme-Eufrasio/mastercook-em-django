from django.shortcuts import render
from .models import Pessoa

# Create your views here.
def home(request):
    return render(request, 'index.html')

def lista_pessoa(request):
    pessoas= Pessoa.objects.all().order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})