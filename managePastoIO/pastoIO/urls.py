from django.urls import path
from pastoIO.views import (
    HomeView, AnimaisListView, FazendasListView, PessoasListView,
    OrganizacoesListView, EventosListView,
    AnimalDetailModalView, AnimalUpdateModalView,
    FazendaDetailModalView, FazendaUpdateModalView,
    PessoaDetailModalView, PessoaUpdateModalView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("animais/", AnimaisListView.as_view(), name="animais_lista"),
    path("fazendas/", FazendasListView.as_view(), name="fazendas_lista"),
    path("pessoas/", PessoasListView.as_view(), name="pessoas_lista"),
    path("organizacoes/", OrganizacoesListView.as_view(), name="organizacoes_lista"),
    path("eventos/", EventosListView.as_view(), name="eventos_lista"),

    path("animais/<int:pk>/modal/", AnimalDetailModalView.as_view(), name="animal_modal_detalhe"),
    path("animais/<int:pk>/editar/modal/", AnimalUpdateModalView.as_view(), name="animal_modal_editar"),

    path("fazendas/<int:pk>/modal/", FazendaDetailModalView.as_view(), name="fazenda_modal_detalhe"),
    path("fazendas/<int:pk>/editar/modal/", FazendaUpdateModalView.as_view(), name="fazenda_modal_editar"),

    path("pessoas/<int:pk>/modal/", PessoaDetailModalView.as_view(), name="pessoa_modal_detalhe"),
    path("pessoas/<int:pk>/editar/modal/", PessoaUpdateModalView.as_view(), name="pessoa_modal_editar"),
]
