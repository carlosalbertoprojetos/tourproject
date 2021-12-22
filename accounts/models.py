from basics.models import AddressMixin, DocumentMixin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import DefaultUserManager


class User(DocumentMixin, AddressMixin, AbstractUser):

    OPTION_CHOICES = (
        ('1', _('Agência')),
        ('2', _('Cliente')),
        ('3', _('Parceiro')),
    )

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

 
