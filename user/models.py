# from basics.models import AddressMixin, CompanyMixin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import DefaultUserManager


class User(AbstractUser):

    OPTION_CHOICES = [
        ('0', _('Admin')),
        ('1', _('Agência')),
        ('2', _('Fornecedor')),
        # ('3', _('Agente')),
        # ('4', _('Cliente')),
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

    class Meta:
        verbose_name_plural = 'Usuários'

    objects = DefaultUserManager()


class Contact(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='contact',
        blank=True,
        null=True
    )

    cel_phone = models.CharField(
        _("Celular"),
        max_length=15
    )

    class Meta:
        verbose_name = 'Contato'
        # verbose_name_plural = 'Contatos'


class SocialMedia(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='social_media',
        blank=True,
        null=True
    )

    social_media = models.CharField(
        _("Rede Social"),
        max_length=100
    )

    class Meta:
        verbose_name_plural = 'Redes Sociais'
