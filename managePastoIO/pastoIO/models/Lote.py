from datetime import date
import os
from uuid import uuid4
from django.db import models
from .Base import TimeStampedModel
from .Organizacao import Organization
from .Fazenda import Farm

class PastureLot(TimeStampedModel):
    organizacao = models.ForeignKey(Organization, verbose_name="organização", on_delete=models.CASCADE)
    fazenda = models.ForeignKey(Farm, verbose_name="fazenda", on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField("nome", max_length=120)
    eh_alugado = models.BooleanField("alugado (gado rendido)", default=False)
    alugado_de = models.CharField("alugado de", max_length=120, blank=True)
    aluguel_inicio = models.DateField("início do aluguel", null=True, blank=True)
    aluguel_fim = models.DateField("fim do aluguel", null=True, blank=True)
    aluguel_mensal = models.DecimalField("aluguel mensal (R$)", max_digits=10, decimal_places=2, null=True, blank=True)
    capacidade_cabecas = models.PositiveIntegerField("capacidade (cabeças)", null=True, blank=True)
    observacoes = models.TextField("observações", blank=True)
    foto = models.ImageField("foto", upload_to="lotes/", null=True, blank=True)

    class Meta:
        verbose_name = "Lote de pasto"
        verbose_name_plural = "Lotes de pasto"
        unique_together = ("organizacao", "nome")
        ordering = ["nome"]

    def __str__(self):
        flag = " (alugado)" if self.eh_alugado else ""
        return f"{self.nome}{flag}"

    # função em pt-BR
    def eh_proprio(self):
        return not self.eh_alugado
    eh_proprio.boolean = True
    eh_proprio.short_description = "É próprio?"
