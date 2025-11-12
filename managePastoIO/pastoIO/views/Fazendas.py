from django.views.generic import ListView
from django.db.models import Q
from pastoIO.models import Farm as Fazenda  # ou from pastoIO.models import Fazenda

class FazendasListView(ListView):
    model = Fazenda
    template_name = "itensNavBar/fazendas/ListarFazendas.html"
    context_object_name = "fazendas"
    paginate_by = 25

    def get_queryset(self):
        qs = Fazenda.objects.select_related("organizacao").order_by("nome")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(cidade__icontains=q) | Q(estado__icontains=q))
        return qs
