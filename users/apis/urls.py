from django.urls import re_path

from users.apis.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
)

app_name = "users"

urlpatterns = [
    re_path("jwt/create/", CustomTokenObtainPairView.as_view(), name="login"),
    re_path("jwt/refresh/", CustomTokenRefreshView.as_view(), name="refresh"),
    re_path("jwt/verify/", CustomTokenVerifyView.as_view(), name="verify"),
    re_path("logout/", LogoutView.as_view(), name="logout"),
]
