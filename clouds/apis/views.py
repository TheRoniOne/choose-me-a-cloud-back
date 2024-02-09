from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet

from clouds.apis.serializers import CloudSerializer, ProductSerializer
from clouds.models import Cloud, Product, Vendor
from clouds.tasks.task_refresh_products import task_refresh_products
from commons.api.serializers import NameSerializer


class CloudViewSet(ModelViewSet):
    queryset = Cloud.objects.all()
    serializer_class = CloudSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == "destroy" or self.action == "refresh":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    @action(detail=False)
    def refresh(self, request):
        task_refresh_products.apply_async()

        return Response(status=HTTP_204_NO_CONTENT)


class VendorNameListAPIView(ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = NameSerializer
    pagination_class = None


class CloudNameListAPIView(ListAPIView):
    queryset = Cloud.objects.all()
    serializer_class = NameSerializer
    pagination_class = None


class ProductNameListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = NameSerializer
    pagination_class = None
