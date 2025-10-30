from django.contrib import admin
from ..models import PastureLot

@admin.register(PastureLot)
class PastureLotAdmin(admin.ModelAdmin):
    list_display = ("nome", "fazenda", "eh_alugado", "alugado_de", "capacidade_cabecas", "organizacao")
    list_filter = ("eh_alugado", "organizacao", "fazenda")
    search_fields = ("nome", "alugado_de")
    ordering = ("nome",)

    # deixa o boolean com ícone
    def eh_alugado_bool(self, obj):
        return obj.eh_alugado
    eh_alugado_bool.boolean = True
    eh_alugado_bool.short_description = "Alugado?"
