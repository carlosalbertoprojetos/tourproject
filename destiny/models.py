from django.db import models
from season.models import Season


class Destiny(models.Model):

    name = models.CharField('Destino', max_length=255,)
    state = models.CharField('Estado', max_length=2)
    city = models.CharField('Cidade',
                            max_length=100,
                            null=True,
                            blank=True,
                            )
    active = models.BooleanField('Active', default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'

    def __str__(self):
        return self.name + ': ' + self.city + '/' + self.state


class DestinyPeriodSeasons(models.Model):
    
    destiny = models.ForeignKey(Destiny, on_delete=models.DO_NOTHING)
    description = models.CharField('Descrição', max_length=150)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    date_start = models.DateField('Data Inicial')
    date_end = models.DateField('Data Final')

    class Meta:
        ordering = ['-date_start']
        verbose_name = 'Descrição Temporada'
        verbose_name_plural = 'Descrição Temporadas'

    def __str__(self):
        return self.description + ' / ' + str(self.date_start) + ' a ' + str(self.date_end)