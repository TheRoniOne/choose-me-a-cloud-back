from rest_framework.serializers import ModelSerializer

from clouds.models import Cloud, Product, Vendor


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "name"]


class CloudSerializer(ModelSerializer):
    class Meta:
        model = Cloud
        fields = ["id", "name", "vendor"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "type", "cloud"]
