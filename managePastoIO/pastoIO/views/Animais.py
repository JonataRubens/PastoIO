from django.views.generic import ListView
from django.db.models import Q
from pastoIO.models import Animal

class AnimaisListView(ListView):
    model = Animal
    template_name = "itensNavBar/animais/ListarAnimal.html"
    context_object_name = "animais"
    paginate_by = 25  # ajuste se quiser

    def get_queryset(self):
        qs = (Animal.objects
              .select_related("raca", "dono", "responsavel", "lote_atual__fazenda", "organizacao")
              .order_by("brinco"))
        q = self.request.GET.get("q")
        sexo = self.request.GET.get("sexo")
        status = self.request.GET.get("status")

        if q:
            qs = qs.filter(Q(brinco__icontains=q) | Q(observacoes__icontains=q))
        if sexo:
            qs = qs.filter(sexo=sexo)
        if status:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["SEXO_CHOICES"] = getattr(Animal, "SEXO_CHOICES", [])
        ctx["STATUS_CHOICES"] = getattr(Animal, "STATUS_CHOICES", [])
        return ctx
