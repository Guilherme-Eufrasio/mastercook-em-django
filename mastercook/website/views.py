from django.shortcuts import render, get_object_or_404
from .models import Pessoa
from mastercook.area_administrativa.models import Receita
from django.db.models import Q
from django.core.paginator import Paginator



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

    termo = request.GET.get("q", "").strip()
    categoria = request.GET.get("categoria", "").strip()

    receitas = Receita.objects.filter(popular=True, ativa=True)

    # FILTRO DE PESQUISA
    if termo:
        receitas = receitas.filter(
            Q(nome_prato__icontains=termo) |
            Q(mestre__username__icontains=termo)
        )

    # FILTRO DE CATEGORIA
    if categoria in ["Salgado", "Doce"]:
        receitas = receitas.filter(categoria=categoria)

    # PAGINAÇÃO
    paginator = Paginator(receitas, 6)  # exibe 8 receitas por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    contexto = {
        "page_obj": page_obj,
        "receitas_populares": page_obj,  # mantém compatibilidade com seu template
        "termo": termo,
        "categoria": categoria,
    }

    return render(request, "receitas/populares.html", contexto)


def simples(request):

    termo = request.GET.get("q", "").strip()
    categoria = request.GET.get("categoria", "").strip()  

    receitas_simples = Receita.objects.filter(popular=False, ativa=True)

    # FILTRO DE PESQUISA
    if termo:
        receitas_simples = receitas_simples.filter(
            Q(nome_prato__icontains=termo) |
            Q(mestre__username__icontains=termo)
        )

    # FILTRO DE CATEGORIA
    if categoria in ["Salgado", "Doce"]:
        receitas_simples = receitas_simples.filter(categoria=categoria)

    contexto = {
        "receitas_simples": receitas_simples,
        "termo": termo,
        "categoria": categoria,
    }

    return render(request, "receitas/simples.html", contexto)

def salgados(request):

    termo = request.GET.get("q", "").strip()

    receitas_salgadas = Receita.objects.filter(Q(categoria='Salgado') | Q(categoria='S'), ativa=True)         

    # FILTRO DE PESQUISA
    if termo:
        receitas_salgadas = receitas_salgadas.filter(
            Q(nome_prato__icontains=termo) |
            Q(mestre__username__icontains=termo)
        )

    contexto = {
        "receitas_salgadas": receitas_salgadas,
        "termo": termo,
    }

    return render(request, 'receitas/salgado.html', contexto)


def doces(request):

    termo = request.GET.get("q", "").strip()

    receitas_doces = Receita.objects.filter(Q(categoria='Doce') | Q(categoria='D'), ativa=True)         

    # FILTRO DE PESQUISA
    if termo:
        receitas_doces = receitas_doces.filter(
            Q(nome_prato__icontains=termo) |
            Q(mestre__username__icontains=termo)
        )

    contexto = {
        "receitas_doces": receitas_doces,
        "termo": termo,
    }

    return render(request, 'receitas/doces.html', contexto)


def criadores(request):
    return render(request, 'sobre.html')

def homeUser(request):
    return render(request, 'homeUsuario.html')