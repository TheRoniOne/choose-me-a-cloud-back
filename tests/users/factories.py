from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from tests.clouds.factories import ProductFactory
from users.models import ShoppingCart


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


class ShoppingCartFactory(DjangoModelFactory):
    class Meta:
        model = ShoppingCart

    user = SubFactory(UserFactory)
    product = SubFactory(ProductFactory)
    quantity = 1
