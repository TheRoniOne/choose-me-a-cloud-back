from django.urls import include, re_path
from rest_framework.routers import SimpleRouter

from users.apis.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    ShoppingCartViewSet,
)

app_name = "users"

router = SimpleRouter()
router.register("shoppingcart", ShoppingCartViewSet, basename="shopping_cart")

urlpatterns = [
    re_path("jwt/create", CustomTokenObtainPairView.as_view(), name="login"),
    re_path("jwt/refresh", CustomTokenRefreshView.as_view(), name="refresh"),
    re_path("jwt/verify", CustomTokenVerifyView.as_view(), name="verify"),
    re_path("logout", LogoutView.as_view(), name="logout"),
    re_path("", include(router.urls)),
]
