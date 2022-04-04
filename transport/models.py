from django.db import models
from tinymce.models import HTMLField
from season.models import Season, Destiny
class Transport(models.Model):
    #destiny = models.ForeignKey(Destiny, on_delete=models.DO_NOTHING, verbose_name='Destino')
    stretch = models.CharField('Trecho', max_length=255, unique=True)
    hits = models.PositiveIntegerField('Poltronas')
    is_active = models.BooleanField('Ativar',default=True)
    document = models.FileField('Documento', upload_to='files/')
    description = HTMLField('Descrição', blank=True)    

    class Meta:
        ordering = ('stretch',)
        verbose_name ='Transporte'
        verbose_name_plural ='Transportes'
    
    def __str__(self):
        return self.stretch

class Transport_Type(models.Model):
    transport_type = models.CharField('Tipo de transporte', max_length=255)

    class Meta:
        ordering = ('transport_type',)
        verbose_name ='Tipo de Transporte'
        

    def __str__(self):
        return self.transport_type


class CategoriesPax(models.Model):
    transport_name = models.CharField('Categoria PAX', max_length=255)
    transport_type = models.ForeignKey(Transport_Type, on_delete=models.DO_NOTHING, verbose_name='Tipo de Transporte')
    
    class Meta:
        ordering = ('transport_name',)
        verbose_name ='Categoria de PAX'
    
    def __str__(self):
        return self.transport_name


class TransportPrices(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.DO_NOTHING, verbose_name='Transporte')
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, verbose_name='Temporada')
    cadpax = models.ForeignKey(CategoriesPax, on_delete=models.DO_NOTHING, verbose_name='Cadastro PAX')
    price = models.CharField('Preço', max_length=9)

    
    class Meta:
        ordering = ('transport',)
        verbose_name ='Preço do Transporte'
    
    def __str__(self):
        return self.transport