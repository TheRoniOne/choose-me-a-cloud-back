from rest_framework.reverse import reverse

from tests.users.factories import ShoppingCartFactory


def test_shopping_cart_list(api, internal_user):
    ShoppingCartFactory.create_batch(3, user=internal_user)
    ShoppingCartFactory.create_batch(4)

    response = api.get(reverse("users:shopping_cart-list"))

    assert response.status_code == 200
    assert response.json()["count"] == 3
