from rest_framework.reverse import reverse

from clouds.constants import ProductType
from tests.clouds.factories import CloudFactory, ProductFactory, VendorFactory


def test_vendor_names(api):
    VendorFactory.create_batch(3)
    response = api.get(reverse("clouds:vendor_names"))

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_cloud_names(api):
    CloudFactory.create_batch(3)
    response = api.get(reverse("clouds:cloud_names"))

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_cloud_names_filter_by_name(api):
    CloudFactory.create(name="GCP")
    CloudFactory.create(name="AWS")
    CloudFactory.create(name="AZURE")

    response = api.get(reverse("clouds:cloud_names"), data={"name": "g"})

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "GCP"


def test_product_names(api):
    ProductFactory.create_batch(3)
    response = api.get(reverse("clouds:product_names"))

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_product_names_filter_by_cloud(api):
    ProductFactory.create_batch(3)
    response = api.get(reverse("clouds:product_names"), data={"cloud": 1})

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_product_names_filter_by_type(api):
    ProductFactory.create_batch(3, type=ProductType.NETWORK)
    ProductFactory.create(type=ProductType.COMPUTE)

    response = api.get(reverse("clouds:product_names"), data={"type": ProductType.COMPUTE})

    assert response.status_code == 200
    assert len(response.json()) == 1
