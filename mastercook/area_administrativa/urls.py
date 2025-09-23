from django.urls import path
from . import views

urlpatterns= [
    path('',views.home, name='home_area_restrita'),
    path('administrativo/', views.adm, name='administrativo'),
    path('cadastrar/', views.cadastrar_receita, name="cadastrar_receita"),
    path('editar/<int:id>/', views.editar_receita, name="editar_receita"),
    #path('remover/<int:id>/', views.remover_receita, name="remover_receita"),
    #path('despublicar/<int:id>/', views.despublicar_receita, name="despublicar_receita"),    
]