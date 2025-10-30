from django.contrib import admin
from ..models import Breed

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ("nome", "organizacao")
    list_filter = ("organizacao",)
    search_fields = ("nome",)
    ordering = ("nome",)
