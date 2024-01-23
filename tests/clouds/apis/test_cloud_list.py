from rest_framework.reverse import reverse

from tests.clouds.factories import CloudFactory


def test_cloud_list(api):
    CloudFactory.create_batch(3)
    response = api.get(reverse("clouds:cloud-list"))

    assert response.status_code == 200
    assert response.json()["count"] == 3
