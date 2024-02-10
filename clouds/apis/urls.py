from django.urls import include, re_path
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
    re_path("", include(router.urls)),
    re_path("vendor/names", VendorNameListAPIView.as_view(), name="vendor_names"),
    re_path("cloud/names", CloudNameListAPIView.as_view(), name="cloud_names"),
    re_path("product/names", ProductNameListAPIView.as_view(), name="product_names"),
]
