from celery import shared_task

from clouds.models import Product
from tests.clouds.factories import ProductFactory


@shared_task
def task_refresh_products():
    Product.objects.all().delete()

    ProductFactory.create_batch(3, cloud__name="AWS")
    ProductFactory.create_batch(3, cloud__name="GCP")
