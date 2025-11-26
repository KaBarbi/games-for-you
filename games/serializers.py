from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    platform_display = serializers.CharField(
        source='get_platform_display', read_only=True
    )
    cover = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = [
            'id', 'title', 'description', 'price',
            'stock', 'platform', 'platform_display', 'cover'
        ]

    def get_cover(self, obj):
        # return only the filename of the cover image
        if obj.cover:
            return obj.cover.name.split('/')[-1]
        return None
