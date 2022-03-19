from django.db import models

# Create your models here.

class Destiny(models.Model):    
    destiny = models.CharField('Destino',max_length=20)    
    state = models.CharField('Estado', max_length=2)
    is_active = models.BooleanField('Ativar',default=True)    
    description = models.TextField('Descrição')
    