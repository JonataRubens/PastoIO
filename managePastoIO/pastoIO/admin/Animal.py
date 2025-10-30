from django.contrib import admin
from ..models import Animal, AnimalWeight, AnimalEvent

class PesagemInline(admin.TabularInline):
    model = AnimalWeight
    extra = 0

class EventoInline(admin.TabularInline):
    model = AnimalEvent
    extra = 0
    fields = (
        "tipo_evento", "data",
        "lote_origem", "lote_destino",
        "produto", "dose", "resultado",
        "comprador", "preco_venda", "observacoes"
    )

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("brinco", "sexo", "status", "dono", "responsavel", "lote_atual", "fazenda", "organizacao")
    list_filter = ("status", "sexo", "organizacao", "lote_atual", "dono", "lote_atual__fazenda")
    search_fields = ("brinco", "observacoes")
    autocomplete_fields = ("mae", "pai", "raca", "dono", "responsavel", "lote_atual")
    ordering = ("brinco",)
    inlines = [PesagemInline, EventoInline]

    # otimiza as consultas para evitar N+1 na coluna fazenda
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("lote_atual", "lote_atual__fazenda", "dono", "responsavel")

    def fazenda(self, obj):
        return obj.lote_atual.fazenda if obj.lote_atual else None
    fazenda.short_description = "Fazenda"
    fazenda.admin_order_field = "lote_atual__fazenda__nome"
