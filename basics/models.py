from django.db import models
from django.utils.translation import gettext_lazy as _


class DocumentMixin(models.Model):

    document_number = models.CharField(
        _('Documento'),
        max_length=18,
        unique=True
    )

    class Meta:
        abstract = True


class AddressMixin(models.Model):

    postal_code = models.CharField(
        _('CEP'),
        max_length=11
    )

    street = models.CharField(
        _("Endereço"),
        max_length=200
    )

    number = models.CharField(
        _('Número'),
        max_length=30
    )

    complement = models.CharField(
        _('Complemento'),
        max_length=100,
        null=True,
        blank=True
    )

    city = models.CharField(
        _('Cidade'),
        max_length=100
    )

    state = models.CharField(
        _('Estado'),
        max_length=100
    )

    class Meta:
        abstract = True
