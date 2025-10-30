from django.db import models
from django.utils import timezone
from .Base import TimeStampedModel
from .Animal import Animal
from .Lote import PastureLot

class AnimalEvent(TimeStampedModel):
    NASCIMENTO = "birth"
    MOVIMENTACAO = "move"
    VACINA = "vaccine"
    VERMIFUGACAO = "deworm"
    DOENCA = "disease"
    DIAG_PRENHEZ = "preg_check"
    INSEMINACAO = "insemination"
    VENDA = "sale"
    MORTE = "death"
    DESMAMA = "weaning"

    TIPO_CHOICES = [
        (NASCIMENTO, "Nascimento"),
        (MOVIMENTACAO, "Movimentação de lote"),
        (VACINA, "Vacinação"),
        (VERMIFUGACAO, "Vermifugação"),
        (DOENCA, "Doença/Tratamento"),
        (DIAG_PRENHEZ, "Diagnóstico de prenhez"),
        (INSEMINACAO, "Cobertura/Inseminação"),
        (VENDA, "Venda"),
        (MORTE, "Morte"),
        (DESMAMA, "Desmama"),
    ]

    animal = models.ForeignKey(Animal, verbose_name="animal", on_delete=models.CASCADE, related_name="eventos")
    tipo_evento = models.CharField("tipo de evento", max_length=20, choices=TIPO_CHOICES)
    data = models.DateField("data", default=timezone.now)

    lote_origem = models.ForeignKey(PastureLot, verbose_name="lote de origem", on_delete=models.SET_NULL, null=True, blank=True, related_name="saidas")
    lote_destino = models.ForeignKey(PastureLot, verbose_name="lote de destino", on_delete=models.SET_NULL, null=True, blank=True, related_name="entradas")
    produto = models.CharField("produto (vacina/vermífugo/medicamento)", max_length=120, blank=True)
    dose = models.CharField("dose", max_length=60, blank=True)
    resultado = models.CharField("resultado", max_length=120, blank=True)

    comprador = models.CharField("comprador", max_length=120, blank=True)
    preco_venda = models.DecimalField("preço de venda (R$)", max_digits=12, decimal_places=2, null=True, blank=True)

    observacoes = models.TextField("observações", blank=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["-data", "-id"]

    def __str__(self):
        return f"{self.get_tipo_evento_display()} - {self.animal} em {self.data}"

    # função em pt-BR (ex.: útil para admin/listas)
    def descricao_curta(self):
        return f"{self.get_tipo_evento_display()} em {self.data}"
    descricao_curta.short_description = "Descrição"
