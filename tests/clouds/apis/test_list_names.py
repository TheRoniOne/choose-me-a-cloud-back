from rest_framework.reverse import reverse

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


def test_product_names(api):
    ProductFactory.create_batch(3)
    response = api.get(reverse("clouds:product_names"))

    assert response.status_code == 200
    assert len(response.json()) == 3
