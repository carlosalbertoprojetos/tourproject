from django.db import models

from destiny.models import Destiny



class Validity(models.Model):

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

    year = models.CharField('Ano', choices=YEARS_CHOICES, max_length=4)
    # name = models.CharField('Temporada', max_length=255)
    validity = models.CharField('Validade', max_length=255)
    destiny = models.ForeignKey(Destiny, on_delete=models.DO_NOTHING)    
    period = models.CharField('Período', max_length=255)
    active = models.BooleanField('Vigente', default=True)
    
    class Meta:
        ordering = ['-year']
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        return self.validity + ' /' + self.year + ' - ' + self.period
  
    
class OptionsPrices(models.Model):
        
        priceselect = models.CharField('Tipo', max_length=255)
        
        def __str__(self):
            return self.priceselect
        
    
class PricesSeasonsDestinies(models.Model):

    validity = models.ForeignKey(Validity, on_delete=models.DO_NOTHING)
    product = models.CharField('Produto', max_length=255)
    priceselect = models.ForeignKey(OptionsPrices, on_delete=models.DO_NOTHING)
    price = models.CharField('Valor', max_length=9)

        