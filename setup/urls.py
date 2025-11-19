from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from games.views import GameViewSet
from cart.views import CartViewSet, CartItemViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'games', GameViewSet, basename="game")
router.register(r'carts', CartViewSet, basename="cart")
router.register(r'cart-items', CartItemViewSet, basename="cartitem")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
