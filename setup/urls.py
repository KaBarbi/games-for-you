from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from games.views import GameViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet, basename="game")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # rotas da API
]
