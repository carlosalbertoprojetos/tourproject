from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import UserManager


class DefaultUserManager(UserManager):

    def create_user(self, *args, **kwargs):
        super().create_user(*args, **kwargs)

    def create_superuser(self, email, password=None):
        user = self.create_user(
            # username=email,
            email=email,
            password=password,
            option='0',
            is_staff=True,
            is_superuser=True
        )
        return user
