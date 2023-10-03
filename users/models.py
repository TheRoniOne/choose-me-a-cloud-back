from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db.models import BooleanField, CharField, EmailField

from commons.models import TimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"

    username = CharField(max_length=255, unique=True)
    first_name = CharField(max_length=255, blank=False, null=False)
    last_name = CharField(max_length=255, blank=False, null=False)
    email = EmailField(max_length=255, null=False, unique=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"
