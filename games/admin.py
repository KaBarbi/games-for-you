from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "platform", "price", "stock", "created_at")
    list_filter = ("platform",)
    search_fields = ("title",)
