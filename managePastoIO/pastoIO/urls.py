from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pastoIO.views import HomeView, AnimaisListView, FazendasListView, PessoasListView, OrganizacoesListView, EventosListView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("animais/", AnimaisListView.as_view(), name="animais_lista"),
    path("fazendas/", FazendasListView.as_view(), name="fazendas_lista"),
    path("pessoas/", PessoasListView.as_view(), name="pessoas_lista"),
    path("organizacoes/", OrganizacoesListView.as_view(), name="organizacoes_lista"),
    path("eventos/", EventosListView.as_view(), name="eventos_lista"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
