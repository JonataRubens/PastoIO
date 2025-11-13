from django.views.generic import ListView, DetailView, UpdateView
from django.http import HttpResponse
from django.db.models import Q
from django.template.loader import render_to_string
from django import forms
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

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "foto",
            "brinco","sexo","status","raca","pelagem",
            "mae","pai","dono","responsavel",
            "lote_atual","origem","data_nascimento",
            "data_compra","preco_compra","fornecedor",
            "observacoes",
        ]
        widgets = {
            "foto": forms.FileInput(attrs={
                "id": "id_foto_input",
                "class": "d-none",           # esconde o input nativo
                "accept": "image/*",
            }),
            "data_nascimento": forms.DateInput(attrs={"type":"date"}),
            "data_compra": forms.DateInput(attrs={"type":"date"}),
            "observacoes": forms.Textarea(attrs={"rows":3, "class": "form-control obs-area"}),
        }

class AnimalDetailModalView(DetailView):
    model = Animal
    template_name = "itensNavBar/animais/_modal_detalhe.html"

    def render_to_response(self, context, **kwargs):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(self.template_name, context, request=self.request)
            return HttpResponse(html)
        return super().render_to_response(context, **kwargs)

class AnimalUpdateModalView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = "itensNavBar/animais/_modal_form.html"

    def form_valid(self, form):
        self.object = form.save()
        html = render_to_string("itensNavBar/animais/_modal_sucesso.html", {"animal": self.object}, request=self.request)
        return HttpResponse(html)

    def form_invalid(self, form):
        html = render_to_string(self.template_name, {"form": form, "animal": self.object}, request=self.request)
        return HttpResponse(html)

    def render_to_response(self, context, **kwargs):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            html = render_to_string(self.template_name, context, request=self.request)
            return HttpResponse(html)
        return super().render_to_response(context, **kwargs)