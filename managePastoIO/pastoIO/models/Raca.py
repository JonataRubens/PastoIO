from django.db import models
from .Base import TimeStampedModel
from .Organizacao import Organization

class Breed(TimeStampedModel):
    organizacao = models.ForeignKey(Organization, verbose_name="organização", on_delete=models.CASCADE)
    nome = models.CharField("nome", max_length=80)

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"
        unique_together = ("organizacao", "nome")
        ordering = ["nome"]

    def __str__(self):
        return self.nome
