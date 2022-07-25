from django.db import models
from destiny.models import Destiny


class Validity(models.Model):

    year = models.CharField('Ano', max_length=4, unique=True)
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
        unique_together = [['name','destiny','validity']]
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        return  self.name + ' - ' + str(self.destiny) + ' - ' + str(self.validity)


 
class Event(models.Model):
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, verbose_name='Temporada')
    name_event = models.CharField('Evento:', max_length=255)
    date_init = models.DateField('Data Inicial:')
    date_fin = models.DateField('Data Final:')

    class Meta:
        unique_together = [['name_event','date_init','date_fin']]
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.name_event  
    