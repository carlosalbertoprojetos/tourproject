from basics.models import AddressMixin, CompanyMixin
from django.db import models
from user.models import User


class Company(CompanyMixin, AddressMixin):

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='company',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'Empresas'
