from django.db import models
from django.utils.translation import gettext_lazy as _


class DocumentMixin(models.Model):

    company = models.CharField(
        _('Razão Social'),
        max_length=100,
    )

    document_number = models.CharField(
        _('Número do Documento'),
        max_length=18,
        unique=True,
        blank=False,
        null=True,
    )

    document_image = models.ImageField(
        'Documento', blank=True, upload_to='doc/%d/%m/%Y')

    class Meta:
        abstract = True


class AddressMixin(models.Model):

    postal_code = models.CharField(
        _('CEP'),
        max_length=11,
        blank=False,
        null=True,
    )

    street = models.CharField(
        _("Logradouro"),
        max_length=200,
        blank=False,
        null=True,
    )

    number = models.CharField(
        _('Número'),
        max_length=30,
        blank=False,
        null=True,
    )

    complement = models.CharField(
        _('Complemento'),
        max_length=100,
        null=True,
        blank=True
    )

    city = models.CharField(
        _('Cidade'),
        max_length=100,
        blank=False,
        null=True,
    )

    state = models.CharField(
        _('Estado'),
        max_length=100,
        blank=False,
        null=True,
    )

    class Meta:
        abstract = True
