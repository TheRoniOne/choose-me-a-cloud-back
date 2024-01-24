from rest_framework.reverse import reverse

from clouds.models import Product
from tests.clouds.factories import ProductFactory


def test_refresh_products(api):
    ProductFactory.create_batch(3)

    response = api.get(reverse("clouds:product-refresh"))

    assert response.status_code == 204
    assert Product.objects.count() == 6
