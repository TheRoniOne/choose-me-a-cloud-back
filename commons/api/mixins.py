from functools import cached_property

from users.models import User


class UserMixin:
    @cached_property
    def user(self) -> User:
        user = self.request.user

        if isinstance(user, User):
            return user

        return User.objects.get(id=user.id)
