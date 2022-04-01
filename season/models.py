from destiny.models import Destiny
from django.db import models


class Validity(models.Model):
    year = models.CharField('Ano', max_length=4)
    active = models.BooleanField('Ativo Agência', default=False)
    sell = models.BooleanField('Ativo Venda', default=False)

    class Meta:
        ordering = ['-year']
        verbose_name = 'Vigência'
        verbose_name_plural = 'Vigências'

    def __str__(self):
        return self.year


class Season(models.Model):
    name = models.CharField('Nome', max_length=255)
    destiny = models.ForeignKey(
        Destiny, on_delete=models.DO_NOTHING, verbose_name='Destino')
    validity = models.ForeignKey(
        Validity, on_delete=models.DO_NOTHING, verbose_name='Vigência')
    active = models.BooleanField('Ativo Agência', default=False)
    sell = models.BooleanField('Ativo Venda', default=False)

    class Meta:
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        return str(self.validity) + ' /' + str(self.destiny) + ' - ' + self.name


class Period(models.Model):
    name = models.CharField('Nome', max_length=255)
    season = models.ForeignKey(
        Season, on_delete=models.DO_NOTHING, verbose_name='Temporada')
    date_start = models.DateField('Data Início')
    date_end = models.DateField('Data Fim')

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'

    def __str__(self):
        return self.name + ' / ' + self.season + ' - ' + self.date_start + ' / ' + self.date_end
