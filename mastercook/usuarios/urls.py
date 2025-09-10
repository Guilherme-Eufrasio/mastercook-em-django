from django.urls import path
from . import views


urlpatterns= [
    path('', views.home, name='home'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('area/', views.area_restrita, name='area_restrita'),
]
