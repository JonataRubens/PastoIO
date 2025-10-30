from django.contrib import admin
from ..models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("nome", "funcao", "telefone", "organizacao")
    list_filter = ("funcao", "organizacao")
    search_fields = ("nome", "telefone")
    ordering = ("nome",)
