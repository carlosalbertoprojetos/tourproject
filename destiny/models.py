from django.db import models


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
