from django.db import models
#from django_cpf_cnpj.fields import CNPJField, CPFField
#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Client(models.Model):

	STATE_CHOICES = (
		('AC','AC'), ('AL','AL'), ('AP','AP'), ('AM','AM'), ('BA','BA'), ('CE','CE'),
		('DF','DF'), ('ES','ES'), ('GO','GO'), ('MA','MA'), ('MT','MT'), ('MS','MS'),
		('MG','MG'), ('PA','PA'), ('PB','PB'), ('PE','PE'), ('PI','PI'), ('PR','PR'), 
		('RJ','RJ'), ('RN','RN'), ('RO','RO'), ('RR','RR'), ('RS','RS'), ('SC','SC'), 
		('SE','SE'), ('SP','SP'), ('TO','TO'),
    
    )
	
	name = models.CharField('Nome Completo',max_length=200)
	#cpf = CPFField(masked=True)  # To enable auto-mask xxx.xxx.xxx-xx
	cpf = models.CharField('Cpf', max_length=14)  # To enable auto-mask xxx.xxx.xxx-xx
	street = models.CharField('Logradouro', max_length=200)
	number = models.CharField('Número', max_length=30)
	complement = models.CharField('Complemento', max_length=100, null=True)
	postal_code = models.CharField('CEP', max_length=11)
	state = models.CharField('Estado', choices=STATE_CHOICES,  max_length=2)
	city = models.CharField('Cidade',max_length=100, null=True)
	email = models.EmailField('E-mail', max_length=254,unique=True)
	phoneNumber = models.CharField('Telefone',max_length=13, unique = True, null = False, blank = False)
	#phoneNumber = PhoneNumberField('Telefone',unique = True, null = False, blank = False)	
	is_active = models.BooleanField('Ativar',default=True)


	def __str__(self):
		return self.name
	