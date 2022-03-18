from django.db import models


class Season(models.Model):
 
    year = models.CharField( 'Ano', max_length=4)
    name = models.CharField('Temporada', max_length=255)
    active = models.BooleanField('Active', default=True)

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        return self.name + ' Temporada'