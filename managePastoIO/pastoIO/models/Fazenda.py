from datetime import date
import os
from uuid import uuid4
from django.db import models
from .Base import TimeStampedModel
from .Organizacao import Organization

class Farm(TimeStampedModel):
    organizacao = models.ForeignKey(Organization, verbose_name="organização", on_delete=models.CASCADE)
    nome = models.CharField("nome", max_length=120)
    cidade = models.CharField("cidade", max_length=80, blank=True)
    estado = models.CharField("UF", max_length=2, blank=True)
    observacoes = models.TextField("observações", blank=True)
    foto = models.ImageField("foto", upload_to="fazendas/", null=True, blank=True)

    class Meta:
        verbose_name = "Fazenda"
        verbose_name_plural = "Fazendas"
        ordering = ["nome"]

    def __str__(self):
        loc = f"{self.cidade}/{self.estado}" if self.cidade or self.estado else ""
        return f"{self.nome} {loc}".strip()

    # função em pt-BR
    def localizacao_curta(self):
        return f"{self.cidade}/{self.estado}".strip("/ ")
    localizacao_curta.short_description = "Localização"
