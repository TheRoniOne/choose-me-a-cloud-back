from factory import Faker
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = "users.User"

    email = Faker("email")
    password = Faker("password")
    username = Faker("user_name")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    is_active = True
    is_staff = False
    is_superuser = False
