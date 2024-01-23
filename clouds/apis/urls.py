from django.urls import include, path
from rest_framework.routers import SimpleRouter

from clouds.apis.views import CloudViewSet

app_name = "clouds"

router = SimpleRouter()
router.register("", CloudViewSet, basename="cloud")


urlpatterns = [
    path("", include(router.urls)),
]
