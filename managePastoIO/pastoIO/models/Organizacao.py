from django.db import models
from .Base import TimeStampedModel

class Organization(TimeStampedModel):
    nome = models.CharField("nome", max_length=120)

    class Meta:
        verbose_name = "Organização"
        verbose_name_plural = "Organizações"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
