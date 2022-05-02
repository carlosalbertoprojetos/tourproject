from django.db import models
from destiny.models import Destiny


class Validity(models.Model):

    year = models.CharField('Ano', max_length=4)
    active = models.BooleanField('Ativo Agência', default=False)
    sell = models.BooleanField('Ativo Venda', default=False)


    YEARS_CHOICES = (
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
    )

    class Meta:
        ordering = ['-year']
        verbose_name = 'Vigência'
        verbose_name_plural = 'Vigências'

    def __str__(self):
        return self.year
    
class Season(models.Model):
    name = models.CharField('Nome', max_length=255)
    destiny = models.ForeignKey(Destiny, on_delete=models.DO_NOTHING, verbose_name='Destino Turístico')
    validity = models.ForeignKey(Validity, on_delete=models.DO_NOTHING, verbose_name='Vigência')
    active_company = models.BooleanField('Ativo Agência', default=False)
    active_sell = models.BooleanField('Ativo Venda', default=False)


    class Meta:
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        return  self.name + ' / ' + str(self.destiny) + ' - ' + str(self.validity)


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

class Event(models.Model):
    name_event = models.CharField(max_length=255)
    date_event = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.name_event      

