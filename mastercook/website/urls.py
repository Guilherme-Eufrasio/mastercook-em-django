from django.urls import path
from . import views


urlpatterns= [
    path('', views.home, name='home'),
    path('pessoas/', views.lista_pessoa, name='lista_pessoa'),
    path('pessoas/<int:id>/', views.detalhe_pessoa, name='detalhe_pessoa'),
    path('login/', views.logar, name='login'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('maispopu/', views.popular, name='maispopu'),
    path('popusimples/', views.simples, name='popusimples'),
    path('salgado/', views.salgados, name='salgado'),
]