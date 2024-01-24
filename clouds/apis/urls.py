from django.urls import include, path
from rest_framework.routers import SimpleRouter

from clouds.apis.views import CloudViewSet, ProductViewSet

app_name = "clouds"

router = SimpleRouter()
router.register("cloud", CloudViewSet, basename="cloud")
router.register("product", ProductViewSet, basename="product")


urlpatterns = [
    path("", include(router.urls)),
]
