from django.views.generic import ListView
from django.db.models import Q
from pastoIO.models import AnimalEvent as Evento  # ou from pastoIO.models import AnimalEvent

class EventosListView(ListView):
    model = Evento
    template_name = "itensNavBar/eventos/ListarEventos.html"
    context_object_name = "eventos"
    paginate_by = 25

    def get_queryset(self):
        qs = (Evento.objects
              .select_related("animal", "lote_origem", "lote_destino")
              .order_by("-data", "-id"))
        q = self.request.GET.get("q")
        tipo = self.request.GET.get("tipo")
        if q:
            qs = qs.filter(Q(animal__brinco__icontains=q) | Q(observacoes__icontains=q))
        if tipo:
            qs = qs.filter(tipo_evento=tipo)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["TIPO_CHOICES"] = getattr(self.model, "TIPO_CHOICES", [])
        return ctx
