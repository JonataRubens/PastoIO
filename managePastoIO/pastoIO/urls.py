from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pastoIO.views import HomeView, AnimaisListView, FazendasListView, PessoasListView, OrganizacoesListView, EventosListView, AnimalDetailModalView, AnimalUpdateModalView, FazendaDetailModalView, FazendaUpdateModalView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("animais/", AnimaisListView.as_view(), name="animais_lista"),
    path("fazendas/", FazendasListView.as_view(), name="fazendas_lista"),
    path("pessoas/", PessoasListView.as_view(), name="pessoas_lista"),
    path("organizacoes/", OrganizacoesListView.as_view(), name="organizacoes_lista"),
    path("eventos/", EventosListView.as_view(), name="eventos_lista"),
    
    #detalhes animal em modal
    path("animais/<int:pk>/modal/", AnimalDetailModalView.as_view(), name="animal_modal_detalhe"),
    path("animais/<int:pk>/editar/modal/", AnimalUpdateModalView.as_view(), name="animal_modal_editar"),

    #detalhe fazenda em modal
    path("fazendas/<int:pk>/modal/", FazendaDetailModalView.as_view(), name="fazenda_modal_detalhe"),
    path("fazendas/<int:pk>/editar/modal/", FazendaUpdateModalView.as_view(), name="fazenda_modal_editar"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


