from django.db import models

# Create your models here.


class Destiny(models.Model):    
    destiny = models.CharField('Destino',max_length=20)
    name = models.CharField('Nome', max_length=15)
    state = models.CharField('Estado', max_length=2)
    date_init = models.DateField('Data Inicial')
    date_final = models.DateField('Data Final')
    description = models.TextField('Descrição')
    is_active = models.BooleanField('Ativar',default=True)