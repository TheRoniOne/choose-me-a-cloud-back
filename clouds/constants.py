from django.db.models import TextChoices


class ProductType(TextChoices):
    COMPUTE = "COMPUTE", "Compute"
    STORAGE = "STORAGE", "Storage"
    NETWORK = "NETWORK", "Network"
    OTHER = "OTHER", "Other"
