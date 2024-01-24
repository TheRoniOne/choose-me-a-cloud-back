from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet

from clouds.apis.serializers import CloudSerializer, ProductSerializer
from clouds.models import Cloud, Product
from clouds.tasks.task_refresh_products import task_refresh_products


class CloudViewSet(ModelViewSet):
    queryset = Cloud.objects.all()
    serializer_class = CloudSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False)
    def refresh(self, request):
        task_refresh_products.apply_async()

        return Response(status=HTTP_204_NO_CONTENT)
