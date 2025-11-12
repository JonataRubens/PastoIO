
from django.views.generic import ListView
from django.db.models import Q
from pastoIO.models import Person as Pessoa  # ou from pastoIO.models import Pessoa

class PessoasListView(ListView):
    model = Pessoa
    template_name = "itensNavBar/pessoas/ListarPessoas.html"
    context_object_name = "pessoas"
    paginate_by = 25

    def get_queryset(self):
        qs = Pessoa.objects.select_related("organizacao").order_by("nome")
        q = self.request.GET.get("q")
        funcao = self.request.GET.get("funcao")
        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(telefone__icontains=q))
        if funcao:
            qs = qs.filter(funcao=funcao)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["FUNCAO_CHOICES"] = getattr(self.model, "FUNCAO_CHOICES", [])
        return ctx
