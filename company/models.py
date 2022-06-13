from django.db import models
from django.utils.translation import gettext_lazy as _

from destiny.models import Destiny
# from trip.models import Trip

class Company(models.Model):

    STATE_CHOICES = [
        ('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'),
        ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'),
        ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'),
        ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'),
        ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'),
        ('SP', 'SP'), ('TO', 'TO'),
    ]

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
    state = models.CharField(_('Estado'), choices=STATE_CHOICES, max_length=2)
    city = models.CharField(_('Cidade'),
                            max_length=100,
                            null=True
                            )

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.company_name


class Phone(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        verbose_name='Telefone',
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
        verbose_name='Rede Social',
    )

    socmedia = models.CharField(
        _("Rede Social"),
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = 'Redes Sociais'


class CompanyDestinies(models.Model):

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='Empresa')
    destiny = models.ForeignKey(Destiny, on_delete=models.DO_NOTHING, verbose_name='Destino')

    class Meta:
        ordering = ('company',)
        verbose_name = 'Destino das empresas'
        verbose_name_plural = 'Destinos das empresas'

    def __str__(self):
        return str(self.company) + ' - ' + str(self.destiny)


# class CompanyTrip(models.Model):
    
#     company = models.ForeignKey(
#         Company, on_delete=models.CASCADE, verbose_name='Empresa')
#     trip = models.ForeignKey(Trip, on_delete=models.DO_NOTHING)

#     class Meta:
#         ordering = ('company',)
#         verbose_name = 'Passeios da empresa'
#         verbose_name_plural = 'Passeios da empresa'

#     def __str__(self):
#         return str(self.company) + ' - ' + str(self.trip)