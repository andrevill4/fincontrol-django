from django.contrib import admin
from .models import Transacao, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'tipo', 'categoria', 'data')
    list_filter = ('tipo', 'categoria', 'data')
    search_fields = ('descricao',)