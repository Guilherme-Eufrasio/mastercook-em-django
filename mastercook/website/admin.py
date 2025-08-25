from django.contrib import admin
from mastercook.website.models import Pessoa
# Register your models here.

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email',)

admin.site.register(Pessoa, PessoaModelAdmin)