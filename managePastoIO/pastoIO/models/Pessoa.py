from django.db import models
from .Base import TimeStampedModel
from .Organizacao import Organization

class Person(TimeStampedModel):
    PROPRIETARIO = "owner"
    VAQUEIRO = "cowboy"
    VETERINARIO = "vet"
    FUNCAO_CHOICES = [
        (PROPRIETARIO, "Proprietário(a)"),
        (VAQUEIRO, "Vaqueiro/Responsável"),
        (VETERINARIO, "Veterinário(a)"),
    ]

    organizacao = models.ForeignKey(Organization, verbose_name="organização", on_delete=models.CASCADE)
    nome = models.CharField("nome", max_length=120)
    funcao = models.CharField("função", max_length=20, choices=FUNCAO_CHOICES, blank=True)
    telefone = models.CharField("telefone", max_length=30, blank=True)
    observacoes = models.TextField("observações", blank=True)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    # Nome de função em pt-BR (ex.: útil em templates)
    def nome_completo(self):
        return self.nome
    nome_completo.short_description = "Nome completo"
