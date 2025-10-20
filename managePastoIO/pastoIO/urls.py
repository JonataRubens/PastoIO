from django.urls import path
from pastoIO.views import ViewPadrao

urlpatterns = [
    path('', ViewPadrao.as_view(), name='Index'),
]