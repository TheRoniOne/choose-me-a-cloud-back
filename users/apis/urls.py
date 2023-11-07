from django.urls import path

from users.apis.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
)

app_name = "users"

urlpatterns = [
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="login"),
    path("jwt/refresh/", CustomTokenRefreshView.as_view(), name="refresh"),
    path("jwt/verify/", CustomTokenVerifyView.as_view(), name="verify"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
