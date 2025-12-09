# pastoIO/views/Pessoas.py
from django.views.generic import ListView, DetailView, UpdateView
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import render_to_string
from django import forms

from pastoIO.models import Pessoa  # já existe

class PessoasListView(ListView):
    model = Pessoa
    template_name = "itensNavBar/pessoas/ListarPessoas.html"          # ajuste se seu path for outro
    context_object_name = "pessoas"
    paginate_by = 25

    def get_queryset(self):
        qs = Pessoa.objects.select_related("organizacao").order_by("nome")
        q = self.request.GET.get("q")
        func = self.request.GET.get("funcao")
        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(telefone__icontains=q))
        if func:
            qs = qs.filter(funcao=func)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # se tiver choices no modelo
        ctx["FUNCAO_CHOICES"] = getattr(Pessoa, "FUNCAO_CHOICES", [])
        return ctx


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome", "funcao", "telefone", "organizacao", "observacoes"]
        widgets = {
            "observacoes": forms.Textarea(attrs={"rows": 3, "class": "form-control obs-area"}),
        }


class PessoaDetailModalView(DetailView):
    model = Pessoa
    template_name = "itensNavBar/pessoas/_modal_detalhe.html"

    def render_to_response(self, context, **kwargs):
        # responde HTML direto para o modal (AJAX)
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(self.template_name, context, request=self.request)
            return HttpResponse(html)
        return super().render_to_response(context, **kwargs)


class PessoaUpdateModalView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "itensNavBar/pessoas/_modal_form.html"

    def form_valid(self, form):
        self.object = form.save()
        html = render_to_string("itensNavBar/pessoas/_modal_sucesso.html",
                                {"pessoa": self.object}, request=self.request)
        return HttpResponse(html)

    def form_invalid(self, form):
        html = render_to_string(self.template_name,
                                {"form": form, "object": self.object}, request=self.request)
        return HttpResponse(html)

    def render_to_response(self, context, **kwargs):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(self.template_name, context, request=self.request)
            return HttpResponse(html)
        return super().render_to_response(context, **kwargs)
