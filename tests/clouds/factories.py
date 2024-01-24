from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from clouds.models import Cloud, Product, Vendor


class VendorFactory(DjangoModelFactory):
    class Meta:
        model = Vendor

    name = Faker("name")


class CloudFactory(DjangoModelFactory):
    class Meta:
        model = Cloud

    vendor = SubFactory(VendorFactory)
    name = Faker("name")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    cloud = SubFactory(CloudFactory)
    name = Faker("name")
