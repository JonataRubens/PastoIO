from django.db import models
from django.utils import timezone
from .Base import TimeStampedModel
from .Animal import Animal

class AnimalWeight(TimeStampedModel):
    animal = models.ForeignKey(Animal, verbose_name="animal", on_delete=models.CASCADE, related_name="pesagens")
    data = models.DateField("data", default=timezone.now)
    peso_kg = models.DecimalField("peso (kg)", max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "Pesagem"
        verbose_name_plural = "Pesagens"
        unique_together = ("animal", "data")
        ordering = ["-data"]

    def __str__(self):
        return f"{self.animal} - {self.peso_kg} kg em {self.data}"

    # função em pt-BR
    def peso_formatado(self):
        return f"{self.peso_kg} kg"
    peso_formatado.short_description = "Peso"
