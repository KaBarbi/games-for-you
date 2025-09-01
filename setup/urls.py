from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from games.views import GameViewSet
from cart.views import CartViewSet, CartItemViewSet


router = DefaultRouter()
router.register(r'games', GameViewSet, basename="game")
router.register(r'carts', CartViewSet, basename="cart")
router.register(r'cart-items', CartItemViewSet, basename="cartitem")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
