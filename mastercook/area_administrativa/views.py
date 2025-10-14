from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Receita
from django.contrib import messages
from django.contrib.messages import constants


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
    print("ASdasd", receitas_do_mestre, t)
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
