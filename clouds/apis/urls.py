from django.urls import include, path
from rest_framework.routers import SimpleRouter

from clouds.apis.views import (
    CloudNameListAPIView,
    CloudViewSet,
    ProductNameListAPIView,
    ProductViewSet,
    VendorNameListAPIView,
    VendorViewSet,
)

app_name = "clouds"

router = SimpleRouter()
router.register("vendor", VendorViewSet, basename="vendor")
router.register("cloud", CloudViewSet, basename="cloud")
router.register("product", ProductViewSet, basename="product")


urlpatterns = [
    path("", include(router.urls)),
    path("vendor/names/", VendorNameListAPIView.as_view(), name="vendor_names"),
    path("cloud/names/", CloudNameListAPIView.as_view(), name="cloud_names"),
    path("product/names/", ProductNameListAPIView.as_view(), name="product_names"),
]
