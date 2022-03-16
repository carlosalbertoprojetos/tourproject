from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Client(models.Model):	
	name = models.CharField('Nome Completo',max_length=20)
	cpf = CPFField(masked=True)  # To enable auto-mask xxx.xxx.xxx-xx
	street = models.CharField('Logradouro', max_length=200)
	number = models.CharField('Número', max_length=30)
	complement = models.CharField('Complemento', max_length=100, blank=True, null=True)
	postal_code = models.CharField('CEP', max_length=11)
	state = models.CharField('Estado', max_length=2)
	city = models.CharField('Cidade',max_length=100, null=True)
	email = models.EmailField('E-mail', max_length=254,unique=True)
	phoneNumber = PhoneNumberField('Telefone',unique = True, null = False, blank = False)	
	is_active = models.BooleanField('Ativar',default=True)

	