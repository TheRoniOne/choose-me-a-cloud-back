from rest_framework.reverse import reverse

from clouds.models import Cloud
from tests.clouds.factories import VendorFactory


def test_cloud_create(api):
    vendor = VendorFactory.create()

    response = api.post(reverse("clouds:cloud-list"), data={"name": "test", "vendor": vendor.id})

    assert Cloud.objects.count() == 1
