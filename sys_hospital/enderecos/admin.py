from django.contrib import admin
from .models import Endereco
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep', 'data_criacao',
                    'data_atualizacao')
    search_fields = ('logradouro', 'bairro', 'cidade', 'cep')
    list_filter = ('estado', 'cidade')