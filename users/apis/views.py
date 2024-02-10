from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from commons.api.filters import IsOwnerFilterBackend
from commons.api.mixins import UserMixin
from config.settings.base import (
    AUTH_COOKIE_HTTP_ONLY,
    AUTH_COOKIE_MAX_AGE,
    AUTH_COOKIE_PATH,
    AUTH_COOKIE_REFRESH_MAX_AGE,
    AUTH_COOKIE_SAMESITE,
    AUTH_COOKIE_SECURE,
)
from users.apis.serialzers import ShoppingCartSerializer
from users.models import ShoppingCart


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get("access")
            refresh_token = response.data.get("refresh")

            response.set_cookie(
                "access",
                access_token,
                max_age=AUTH_COOKIE_MAX_AGE,
                path=AUTH_COOKIE_PATH,
                secure=AUTH_COOKIE_SECURE,
                httponly=AUTH_COOKIE_HTTP_ONLY,
                samesite=AUTH_COOKIE_SAMESITE,
            )
            response.set_cookie(
                "refresh",
                refresh_token,
                max_age=AUTH_COOKIE_REFRESH_MAX_AGE,
                path=AUTH_COOKIE_PATH,
                secure=AUTH_COOKIE_SECURE,
                httponly=AUTH_COOKIE_HTTP_ONLY,
                samesite=AUTH_COOKIE_SAMESITE,
            )

        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh")

        if refresh_token:
            request.data["refresh"] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get("access")

            response.set_cookie(
                "access",
                access_token,
                max_age=AUTH_COOKIE_MAX_AGE,
                path=AUTH_COOKIE_PATH,
                secure=AUTH_COOKIE_SECURE,
                httponly=AUTH_COOKIE_HTTP_ONLY,
                samesite=AUTH_COOKIE_SAMESITE,
            )

        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get("access")

        if access_token:
            request.data["token"] = access_token

        return super().post(request, *args, **kwargs)


class LogoutView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        response = Response(status=HTTP_204_NO_CONTENT)
        response.delete_cookie("access")
        response.delete_cookie("refresh")

        return response


class ShoppingCartViewSet(ModelViewSet, UserMixin):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    filter_backends = [IsOwnerFilterBackend]
