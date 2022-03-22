from django.db import models
from season.models import Season


class Destiny(models.Model):

    destiny = models.CharField('Destino', max_length=255,)
    state = models.CharField('Estado', max_length=2)
    city = models.CharField('Cidade',
                            max_length=100,
                            null=True,
                            blank=True,
                            )
    active = models.BooleanField('Active', default=True)

    class Meta:
        ordering = ('destiny',)
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'

    def __str__(self):
        return self.destiny + ': ' + self.city + '/' + self.state


class DestinySeasons(models.Model):

    destiny = models.ForeignKey(Destiny, on_delete=models.DO_NOTHING)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('-season',)
        verbose_name = 'Destino Temporada'
        verbose_name_plural = 'Destino Temporadas'

    # def __str__(self):
    #     return str(self.destiny) + ' - ' + str(self.season) + ' - ' + self.period
