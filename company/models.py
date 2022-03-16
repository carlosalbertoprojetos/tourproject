from django.db import models
from django.utils.translation import gettext_lazy as _


class States(models.Model):
    name = models.CharField('Estado', max_length=20)
    initials = models.CharField('UF', max_length=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Cities(models.Model):
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    name = models.CharField('Cidade', max_length=100)

    class Meta:
        ordering = ('state__name', 'name',)


class Company(models.Model):

    responsible = models.CharField(_('Nome Completo'), max_length=100)
    company_name = models.CharField(_('Razão Social'), max_length=100)
    document_number = models.CharField(_('CPF/CNPJ'), 
                                       max_length=18, unique=True,
    )
    street = models.CharField(_('Logradouro'), max_length=200)
    number = models.CharField(_('Número'), max_length=30)
    complement = models.CharField(
        _('Complemento'), max_length=100,
        blank=True, null=True,
    )
    postal_code = models.CharField(_('CEP'), max_length=11)
    state = models.CharField(_('Estado'), max_length=2)
    city = models.CharField(_('Cidade'),
        max_length=100,
        null=True
    )

    class Meta:
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.responsible or self.company_name


class Phone(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        related_name='phone',
    )

    phone = models.CharField(
        _("Telefone"),
        max_length=15,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'


class SocialMedia(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        related_name='social_media',
    )

    socmedia = models.CharField(
        _("Rede Social"),
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = 'Redes Sociais'


