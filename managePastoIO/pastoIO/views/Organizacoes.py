from django.views.generic import ListView
from django.db.models import Q
from pastoIO.models import Organization as Organizacao  # ou from pastoIO.models import Organizacao

class OrganizacoesListView(ListView):
    model = Organizacao
    template_name = "itensNavBar/organizacoes/ListarOrganizacoes.html"
    context_object_name = "organizacoes"
    paginate_by = 25

    def get_queryset(self):
        qs = Organizacao.objects.order_by("nome")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(nome__icontains=q))
        return qs
