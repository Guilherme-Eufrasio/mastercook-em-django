from django.db import models
from mastercook.usuarios.models import Usuario

# Create your models here.
class Receita(models.Model):
    DOCE = "D"
    SALGADA = "S"
    CATEGORIA_CHOICES = {
        DOCE: "Doce",
        SALGADA: "Salgada",        
    }
    # Campos adicionais, se quiser
    nome_prato = models.CharField(verbose_name="Nome do prato",max_length=50, blank=True, null=True)
    receita = models.TextField(max_length=200, blank=True, null=True)
    imagem = models.ImageField(
        upload_to="receitas/",   # pasta dentro de MEDIA_ROOT
        blank=True,
        null=True
    )
    mestre = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    popular = models.BooleanField(default=False)
    tempo_preparo = models.PositiveIntegerField(verbose_name="Tempo de preparo (em minutos)", blank = True, null = True, default=0 )
    categoria = models.CharField(
        max_length=1,
        choices=CATEGORIA_CHOICES,
    )    
    ativa = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Receitas'
        verbose_name = 'Receita'
        ordering = ('nome_prato',  'categoria','mestre')

    def __str__(self):
        return self.nome_prato
