from django.contrib import admin
from ..models import Farm

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "estado", "organizacao")
    list_filter = ("estado", "organizacao")
    search_fields = ("nome", "cidade")
    ordering = ("nome",)
