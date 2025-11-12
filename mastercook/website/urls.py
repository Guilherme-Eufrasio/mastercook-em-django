from django.urls import path
from . import views


urlpatterns= [
    path('', views.home, name='home'),
    path('login/', views.logar, name='login'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('receitas/populares/', views.popular, name='populares'),
    path('receitas/simples/', views.simples, name='simples'),
    path('receitas/salgado/', views.salgados, name='salgado'),
    path('receitas/doces/', views.doces, name='doces'),
    path('sobre/', views.criadores, name='sobre'),
    path('homeUsuario/', views.homeUser, name='homeUsuario'),
]