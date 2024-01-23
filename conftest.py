from pytest import fixture
from rest_framework.test import APIClient

from tests.users.factories import UserFactory


@fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """This enables db access for all tests"""
    pass


@fixture
def unauthenticated_api():
    return APIClient()


@fixture
def internal_user():
    return UserFactory.create()


@fixture
def api(unauthenticated_api, internal_user):
    unauthenticated_api.force_authenticate(internal_user)

    return unauthenticated_api
