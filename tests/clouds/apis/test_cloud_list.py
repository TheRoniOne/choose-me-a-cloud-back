from factories import CloudFactory
from rest_framework.reverse import reverse


def test_cloud_list(api):
    CloudFactory.create_batch(3)
    response = api.get(reverse("clouds:cloud-list"))

    assert response.status_code == 200
    assert len(response.data) == 3
