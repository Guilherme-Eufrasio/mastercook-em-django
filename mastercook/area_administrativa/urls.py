from django.urls import path
from . import views

urlpatterns= [
    path('administrativo/', views.adm, name='administrativo'),
]