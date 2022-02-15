from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Company(models.Model):

    company_name = models.CharField(
        _('Razão Social'),
        max_length=100,
    )

    document_number = models.CharField(
        _('CPF/CNPJ'),
        max_length=18,
        unique=True,
        blank=True,
        null=True,
    )

    document_image = models.ImageField(
        upload_to='documentos/',
        blank=True,
    )

    street = models.CharField(
        _('Logradouro'),
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

    postal_code = models.CharField(
        _('CEP'),
        max_length=11,
        blank=False,
        null=True,
    )

    city = models.CharField(
        _('Cidade'),
        max_length=100,
        blank=False,
        null=True,
    )

    state = models.CharField(
        _('Estado'),
        max_length=2,
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = 'Empresas'


class Contact(models.Model):

    company = models.ForeignKey(
        Company,
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
        verbose_name_plural = 'Contatos'


class SocialMedia(models.Model):

    company = models.ForeignKey(
        Company,
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
