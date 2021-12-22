from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import UserManager


class DefaultUserManager(UserManager):

    def create_user(self, *args, **kwargs):
        super().create_user(*args, **kwargs)

    @login_required
    def create_agent_user(self, *args, **kwargs):
        user = self.model(
            email=self.normalize_email(*args, **kwargs),
        )
        user.option = 'Agente'
        user.set_password(*args, **kwargs)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            username=email,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        return user
