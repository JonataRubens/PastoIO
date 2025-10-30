from datetime import date
from uuid import uuid4
from django.db import models
import os
from django.utils import timezone
from django.core.exceptions import ValidationError

from .Base import TimeStampedModel
from .Organizacao import Organization
from .Pessoa import Person
from .Lote import PastureLot
from .Raca import Breed

class Animal(TimeStampedModel):
    MACHO = "M"
    FEMEA = "F"
    SEXO_CHOICES = [(MACHO, "Macho"), (FEMEA, "Fêmea")]

    VIVO = "alive"
    VENDIDO = "sold"
    MORTO = "dead"
    DESAPARECIDO = "missing"
    STATUS_CHOICES = [
        (VIVO, "Vivo"),
        (VENDIDO, "Vendido"),
        (MORTO, "Morto"),
        (DESAPARECIDO, "Desaparecido"),
    ]

    NASCIDO = "born"
    COMPRADO = "purchased"
    ORIGEM_CHOICES = [(NASCIDO, "Nascido na fazenda"), (COMPRADO, "Comprado")]

    organizacao = models.ForeignKey(Organization, verbose_name="organização", on_delete=models.CASCADE)
    brinco = models.CharField("brinco/identificador", max_length=50)
    sexo = models.CharField("sexo", max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField("data de nascimento", null=True, blank=True)
    raca = models.ForeignKey(Breed, verbose_name="raça", on_delete=models.SET_NULL, null=True, blank=True)
    pelagem = models.CharField("pelagem/cor", max_length=50, blank=True)

    mae = models.ForeignKey("self", verbose_name="mãe", on_delete=models.SET_NULL, null=True, blank=True, related_name="bezerros")
    pai = models.ForeignKey("self", verbose_name="pai", on_delete=models.SET_NULL, null=True, blank=True, related_name="descendentes")

    dono = models.ForeignKey(Person, verbose_name="dono(a)", on_delete=models.SET_NULL, null=True, related_name="animais_dono")
    responsavel = models.ForeignKey(Person, verbose_name="responsável", on_delete=models.SET_NULL, null=True, blank=True, related_name="animais_responsavel")

    lote_atual = models.ForeignKey(PastureLot, verbose_name="lote atual", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField("status", max_length=12, choices=STATUS_CHOICES, default=VIVO)

    origem = models.CharField("origem", max_length=12, choices=ORIGEM_CHOICES, default=NASCIDO)
    data_compra = models.DateField("data da compra", null=True, blank=True)
    preco_compra = models.DecimalField("preço de compra (R$)", max_digits=12, decimal_places=2, null=True, blank=True)
    fornecedor = models.CharField("fornecedor", max_length=120, blank=True)

    observacoes = models.TextField("observações", blank=True)
    foto = models.ImageField("foto", upload_to="animais/", null=True, blank=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"
        unique_together = ("organizacao", "brinco")
        ordering = ["brinco"]

    def __str__(self):
        return f"{self.brinco} ({self.get_sexo_display()})"

    # ===== funções em pt-BR =====
    @property
    def fazenda(self):
        """Fazenda deduzida do lote atual."""
        return self.lote_atual.fazenda if self.lote_atual else None

    def validar_coerencia_organizacao(self):
        """Valida que todas as FKs pertencem à mesma organização do animal."""
        erros = {}
        if self.lote_atual and self.organizacao_id != self.lote_atual.organizacao_id:
            erros["lote_atual"] = "Lote pertence a outra organização."
        if self.dono and self.organizacao_id != self.dono.organizacao_id:
            erros["dono"] = "Dono pertence a outra organização."
        if self.responsavel and self.organizacao_id != self.responsavel.organizacao_id:
            erros["responsavel"] = "Responsável pertence a outra organização."
        if erros:
            raise ValidationError(erros)

    def clean(self):
        self.validar_coerencia_organizacao()
