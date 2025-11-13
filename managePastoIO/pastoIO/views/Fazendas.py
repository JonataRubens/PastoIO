# pastoIO/views/Fazendas.py
from django.views.generic import ListView, DetailView, UpdateView
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import render_to_string
from django import forms

from pastoIO.models import Farm

class FazendasListView(ListView):
    model = Farm
    template_name = "itensNavBar/fazendas/ListarFazendas.html"   # ajuste se usa outro caminho
    context_object_name = "fazendas"
    paginate_by = 25

    def get_queryset(self):
        qs = Farm.objects.select_related("organizacao").order_by("nome")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(nome__icontains=q) |
                Q(cidade__icontains=q) |
                Q(estado__icontains=q) |
                Q(observacoes__icontains=q)
            )
        return qs

class FazendaForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ["nome", "cidade", "estado", "organizacao", "observacoes"]  # acrescente "foto" se tiver
        widgets = {"observacoes": forms.Textarea(attrs={"rows": 3})}

class FazendaDetailModalView(DetailView):
    model = Farm
    template_name = "itensNavBar/fazendas/_modal_detalhe.html"

    def render_to_response(self, context, **kwargs):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(self.template_name, context, request=self.request)
            return HttpResponse(html)
        return super().render_to_response(context, **kwargs)

class FazendaUpdateModalView(UpdateView):
    model = Farm
    form_class = FazendaForm
    template_name = "itensNavBar/fazendas/_modal_form.html"

    def form_valid(self, form):
        self.object = form.save()
        html = render_to_string("itensNavBar/fazendas/_modal_sucesso.html", {"fazenda": self.object}, request=self.request)
        return HttpResponse(html)

    def form_invalid(self, form):
        html = render_to_string(self.template_name, {"form": form, "fazenda": getattr(self, "object", None)}, request=self.request)
        return HttpResponse(html)

    def render_to_response(self, context, **kwargs):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(self.template_name, context, request=self.request)
            return HttpResponse(html)
        return super().render_to_response(context, **kwargs)
