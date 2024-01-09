from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    Index,
    Model,
    UniqueConstraint,
)

from clouds.constants import ProductType
from commons.models import TimeStampedModel


class Vendor(Model):
    class Meta:
        constraints = [UniqueConstraint(fields=["name"], name="unique_vendor_name")]

    name = CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Cloud(Model):
    vendor = ForeignKey(Vendor, on_delete=CASCADE)
    name = CharField(max_length=50)

    def __str__(self):
        return f"{self.vendor} - {self.name}"


class Product(TimeStampedModel):
    class Meta:
        ordering = ["-updated_at"]
        indexes = [
            Index(fields=["id"], name="id_idx"),
            Index(fields=["cloud"], name="cloud_idx"),
            Index(fields=["name"], name="name_idx"),
            Index(fields=["type"], name="type_idx"),
        ]

    cloud = ForeignKey(Cloud, on_delete=CASCADE)
    name = CharField(max_length=100)
    type = CharField(max_length=10, choices=ProductType.choices, default=ProductType.OTHER)

    def __str__(self):
        return f"{self.cloud} - {self.name}"
