from django.urls import path
from . import views

urlpatterns= [
    path('',views.home, name='home_area_restrita'),
    path('administrativo/', views.adm, name='administrativo'),
    path('minhas-receitas/', views.index_receitas, name="index_receitas"),
    path('minhas-receitas/<str:t>', views.index_receitas, name="index_receitas"),
    path('pesquisar-receita/<int:id>', views.pesquisar_receita, name="pesquisar_receita"),
    path('cadastrar/', views.cadastrar_receita, name="cadastrar_receita"),
    #path('postar_receita/', views.postar_receita, name="postar_receita"),
    path('editar/<int:id>/', views.editar_receita, name="editar_receita"),
    #path('remover/<int:id>/', views.remover_receita, name="remover_receita"),
    path('salvar-edicao/<int:id>/', views.salvar_edicao_receita, name="salvar_edicao_receita"),
    path('salvar-publicacao/<int:id>/', views.salvar_publicacao_receita, name="salvar_publicacao_receita"),
    
    #path('despublicar/<int:id>/', views.despublicar_receita, name="despublicar_receita"),    
]