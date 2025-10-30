from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("PastoIO rodando. Vá para /admin/")
