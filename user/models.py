from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import DefaultUserManager

from company.models import Company

class User(AbstractUser):

    OPTION_CHOICES = [
        ('0', _('Admin')),
        ('1', _('Agência')),
        ('2', _('Fornecedor')),
    ]

    email = models.EmailField(
        _('Email'),
        unique=True
    )

    option = models.CharField(
        _('Opção'),
        max_length=8,
        choices=OPTION_CHOICES
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Usuários'

    objects = DefaultUserManager()
