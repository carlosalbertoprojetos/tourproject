from basics.models import AddressMixin, DocumentMixin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import DefaultUserManager


class User(AddressMixin, DocumentMixin, AbstractUser):

    OPTION_CHOICES = [
        ('0', _('Admin')),
        # ('1', _('Cliente')),
        ('2', _('Agência')),
        ('3', _('Fornecedor')),
        ('4', _('Agente')),
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

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = DefaultUserManager()


# class DocumentImageMixin(models.Model):

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True
#     )

#     document_name = models.CharField(
#         _('Nome documento'),
#         max_length=50,
#     )

#     document_image = models.ImageField(
#         upload_to='images/%d/%m/%Y/', blank=True)


class ContactMixin(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    cel_phone = models.CharField(
        _("Celular"),
        max_length=15
    )


class SocialMediaMixin(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    social_media = models.CharField(
        _("Rede Social"),
        max_length=100
    )
