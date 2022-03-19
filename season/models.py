from django.db import models

# Create your models here.

class Season(models.Model):    
    season = models.CharField('Temporada',max_length=20)
    date_init = models.DateField('Data Inicial')
    date_final = models.DateField('Data Final')    
    description = models.TextField('Descrição')
    
