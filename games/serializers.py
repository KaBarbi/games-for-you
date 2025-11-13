from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    platform_display = serializers.CharField(
        source='get_platform_display', read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'price',
                  'stock', 'platform', 'platform_display', 'cover']
