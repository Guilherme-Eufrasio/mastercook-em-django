from django.contrib import admin
from mastercook.area_administrativa.models import Receita
# Register your models here.

class ReceitaModelAdmin(admin.ModelAdmin):
    list_display = ['nome_prato','imagem','receita','categoria','mestre',]
    search_fields = ('nome_prato',"mestre", "categoria", 'ativa', 'popular')

admin.site.register(Receita, ReceitaModelAdmin)