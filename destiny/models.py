from django.db import models
from django.core import serializers

class Destiny(models.Model):
    season = models.CharField('Temporada', max_length=255,)
    destiny = models.CharField('Destino', max_length=255,)
    state = models.CharField('Estado', max_length=2)
    city = models.CharField('Cidade',
        max_length=100,
        null=True,
        blank=True,
    )
    date_start = models.DateField('Data inicial')
    date_finish = models.DateField('Data final')    
    active = models.BooleanField('Active', default=True)
    description = models.TextField('Descrição', 
        null=True,
        blank=True,
    )
    
    class Meta:
        ordering = ('season',)
        verbose_name ='Destino'
        verbose_name_plural ='Destinos'
    
    def __str__(self):
        return self.destiny + ': ' + self.season + ' Temporada - ' + self.city