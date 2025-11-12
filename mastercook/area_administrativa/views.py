from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Receita
from django.contrib import messages
from django.contrib.messages import constants
from django.http import JsonResponse

# Create your views here.
@login_required
def home(request):
    receitas_do_mestre = Receita.objects.filter(mestre=request.user)
    receitas_publicadas =receitas_do_mestre.filter(ativa=True)
    receitas_nao_publicadas =receitas_do_mestre.filter(ativa=False)
    total_receitas = receitas_do_mestre.count()
    return render(request, "index-area-restrita.html", {'minhas_receitas': receitas_do_mestre, 'publicadas': receitas_publicadas, 'despublicadas' : receitas_nao_publicadas, 'total_receitas': total_receitas})

@login_required
def index_receitas(request, t=None):
    receitas_do_mestre = Receita.objects.filter(mestre=request.user)
    #print("ASdasd", receitas_do_mestre, t)
    if t is None:
        t = 't'
    
    if (t=='p'):
        receitas_do_mestre = receitas_do_mestre.filter(ativa=True)
    elif (t=='d'):
        receitas_do_mestre = receitas_do_mestre.filter(ativa=False)
    else:
        pass
    
    return render(request, 'receitas/index.html',  {'minhas_receitas': receitas_do_mestre})

@login_required
def adm(request):
    return render(request, 'administrativo.html')


@login_required
def cadastrar_receita(request):
    if request.method == 'POST':
        nomeReceita = request.POST.get('nomeReceita')
        if request.FILES.get('imagemReceita'):
            img_receita = request.FILES.get('imagemReceita')
        descricaoReceita = request.POST.get('descricaoReceita')
        popularesReceita = request.POST.get('popularesReceita')
        categoria = request.POST.get('categoria')
        tempo_preparo = request.POST.get('tempo_preparo')

        receita  = Receita.objects.create(
                nome_prato=nomeReceita,
                receita=descricaoReceita,
                imagem=img_receita,
                popular=  True if popularesReceita=="Sim" else False,
                mestre = request.user, 
                tempo_preparo = tempo_preparo,
                categoria = categoria,
                ativa = False
        )
        
        receita.save()

        messages.success(request, f'Receita {receita.nome_prato} cadastrato com sucesso!')
        return redirect('home_area_restrita')


    return render(request, "receitas/cadastrar.html")

def editar_receita(request, id):
    return render(request, "receitas/editar.html")

def pesquisar_receita(request, id):
    # Busca a receita pelo ID ou retorna erro 404 se não existir
    receita = get_object_or_404(Receita, pk=id)

    # Cria o dicionário de dados que será convertido em JSON
    dados = {
        "id": receita.id,
        "nome": receita.nome_prato,
        "imagem": receita.imagem.url,
        "receita": receita.receita,
        "mestre": {
            "id": receita.mestre.id,
            "nome": receita.mestre.username,
        },
        "popular": "sim"  if receita.popular else "não",
        "tempo_preparo": receita.tempo_preparo,
        "categoria": receita.categoria,
        "ativa" : "sim" if receita.ativa else "não"
    }

    # Retorna o JSON
    return JsonResponse(dados, json_dumps_params={'ensure_ascii': False})

@login_required
def salvar_edicao_receita(request, id):
    receita_editar = get_object_or_404(Receita, pk=id)

    if request.method == 'POST':
        nomeReceita = request.POST.get('nomeReceitaEditar')
        img_receita = request.FILES.get('imagemReceitaEditar')  # pode ser None
        descricaoReceita = request.POST.get('receitaEditar')
        popularesReceita = request.POST.get('popularEditar')
        categoria = request.POST.get('categoriaEditar')
        tempo_preparo = request.POST.get('tempo_preparoEditar')

        # Atualiza campos
        receita_editar.nome_prato = nomeReceita
        receita_editar.receita = descricaoReceita
        if img_receita:
            receita_editar.imagem = img_receita
        receita_editar.popular = True if popularesReceita == "sim" else False
        receita_editar.tempo_preparo = tempo_preparo
        receita_editar.categoria = categoria

        receita_editar.save()

        messages.success(request, f'Receita "{receita_editar.nome_prato}" atualizada com sucesso!')
        return redirect('index_receitas')

def salvar_publicacao_receita(request, id):
    receita = get_object_or_404(Receita, pk=id)
    
    if request.method == 'POST':
        receita.ativa = not receita.ativa 
        receita.save()
        messages.success(request, f'Receita "{receita.nome_prato}" publicada com sucesso!')
        return redirect('index_receitas')

# @login_required
# def postar_receita(request):
#     return redirect('home_area_restrita')

    # if request.method == 'POST':
    #     # nomeReceita = request.POST.get('nomeReceita')
    #     # if request.FILES.get('imagemReceita'):
    #     #     img_receita = request.FILES.get('imagemReceita')
    #     # descricaoReceita = request.POST.get('descricaoReceita')
    #     # popularesReceita = request.POST.get('popularesReceita')
    #     # categoria = request.POST.get('categoria')
    #     # tempo_preparo = request.POST.get('tempo_preparo')
    #     # messages.success(request, f'Receita {Receita.nomeReceita} cadastrato com sucesso!')
    #     return redirect('home_area_restrita')
