from destiny.models import Destiny
from django.db import models
from django.utils.translation import gettext_lazy as _


class State(models.Model):
    name = models.CharField('Estado', max_length=20)
    acronym = models.CharField('UF', max_length=2)

    class Meta:
        ordering = ['acronym']
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.acronym


class City(models.Model):
    name = models.CharField('Cidade', max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        ordering = ('state__name', 'name',)
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'


    def __str__(self):
        return self.name


# class CompanyAdress(models.Model):
#     name = models.CharField(max_length=100)
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     city = ChainedForeignKey(
#         City, 
#         on_delete=models.CASCADE,
#         chained_field="state",
#         chained_model_field="state",
#         show_all=False,
#         auto_choose=True,
#         )

#     class Meta:
#         ordering = ['name']
#         verbose_name = 'Endereço Empresa'
#         verbose_name_plural = 'Endereço Empresas'

#     def __str__(self):
#         return self.name


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
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
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


class CompanyDestinies(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='company_destiny')
    destiny = models.ForeignKey(Destiny, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('company',)
        verbose_name = 'Destino das empresas'
        verbose_name_plural = 'Destinos das empresas'

    def __str__(self):
        return str(self.company) + ' - ' + str(self.destiny)


# class LocalFlavor(models.Model):
#     cep = models.CharField(_('CEP'), max_length=100)
#     state = models.CharField(_('Estado'), max_length=100)
#     cpf = models.CharField(_('CPF'), max_length=100)
#     cnpj = models.CharField(_('CNPJ'), max_length=100)
#     phone = models.CharField(_('Telefone'), max_length=100)
    

#     def __str__(self):
#         return str(self.cpf) + ' - ' + str(self.cnpj) + ' - ' + str(self.cep) + ' - ' + str(self.state) + ' - ' + str(self.phone)
    