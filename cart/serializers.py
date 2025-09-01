from rest_framework import serializers
from .models import Cart, CartItem
from games.models import Game
from games.serializers import GameSerializer

class CartItemSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(),
        source="game",
        write_only=True
    )

    class Meta:
        model = CartItem
        fields = ["id", "game", "game_id", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "created_at", "items"]
