from rest_framework import viewsets, filters
from .models import Game
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by("-created_at")
    serializer_class = GameSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["price", "created_at"]
