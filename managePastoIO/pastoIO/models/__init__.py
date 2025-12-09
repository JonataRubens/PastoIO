from .Base import TimeStampedModel

# originais em inglês
from .Organizacao import Organization
from .Pessoa import Person
from .Fazenda import Farm
from .Lote import PastureLot
from .Raca import Breed
from .Animal import Animal
from .Pesagem import AnimalWeight
from .Eventos import AnimalEvent

# aliases em PT-BR (o que as suas views usam)
Organizacao = Organization
Pessoa      = Person
Fazenda     = Farm
Lote        = PastureLot
Raca        = Breed
Pesagem     = AnimalWeight
Evento      = AnimalEvent

__all__ = [
    # se preferir, exponha só PT-BR:
    "TimeStampedModel",
    "Organizacao", "Pessoa", "Fazenda", "Lote", "Raca",
    "Animal", "Pesagem", "Evento",
]
